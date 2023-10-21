import contextlib
import os
import pathlib
import sys

import coverage
import logging
from typing import Any, List, Optional, Union

import coverage
from coverage.files import FnmatchMatcher, prep_patterns
from coverage.misc import CoverageException, NoSource, NotPython
from coverage.python import PythonFileReporter
from coverage.results import Analysis

import pytest

log = logging.getLogger("coverage_lcov.converter")


class Converter:
    """
    Fork from coverage-lcov without outdated click. Project is stale so we need to maintain our own.
    """

    def __init__(
        self,
        relative_path: bool,
        config_file: Union[str, bool],
        data_file_path: str,
    ):
        self.relative_path = relative_path

        self.cov_obj = coverage.coverage(data_file=data_file_path, config_file=config_file)  # type: ignore
        self.cov_obj.load()
        self.cov_obj.get_data()

    def get_file_reporters(self) -> List[Union[PythonFileReporter, Any]]:
        file_reporters: List[
            Union[PythonFileReporter, Any]
        ] = self.cov_obj._get_file_reporters(  # pylint: disable=protected-access
            None
        )
        config = self.cov_obj.config

        if config.report_include:
            matcher = FnmatchMatcher(  # pylint: disable=too-many-function-args
                prep_patterns(config.report_include), "report_include"  # type: ignore
            )
            file_reporters = [fr for fr in file_reporters if matcher.match(fr.filename)]

        if config.report_omit:
            matcher = FnmatchMatcher(  # pylint: disable=too-many-function-args
                prep_patterns(config.report_omit), "report_omit"  # type: ignore
            )
            file_reporters = [fr for fr in file_reporters if not matcher.match(fr.filename)]

        if not file_reporters:
            raise CoverageException("No data to report.")

        return file_reporters

    def get_lcov(self) -> str:
        """Get LCOV output

        This is shamelessly adapted from https://github.com/nedbat/coveragepy/blob/master/coverage/report.py

        """
        output = ""

        file_reporters = self.get_file_reporters()

        config = self.cov_obj.config

        for file_reporter in sorted(file_reporters):
            try:
                analysis = self.cov_obj._analyze(file_reporter)  # pylint: disable=protected-access
                token_lines = analysis.file_reporter.source_token_lines()
                if self.relative_path:
                    filename = file_reporter.relative_filename()
                else:
                    filename = file_reporter.filename
                output += "TN:\n"
                output += f"SF:{filename}\n"

                lines_hit = 0
                for i, _ in enumerate(token_lines, 1):
                    hits = get_hits(i, analysis)
                    if hits is not None:
                        if hits > 0:
                            lines_hit += 1
                        output += f"DA:{i},{hits}\n"

                output += f"LF:{len(analysis.statements)}\n"
                output += f"LH:{lines_hit}\n"
                output += "end_of_record\n"

            except NoSource:
                if not config.ignore_errors:
                    raise

            except NotPython:
                if file_reporter.should_be_python():
                    if config.ignore_errors:
                        msg = "Couldn't parse Python file '{}'".format(file_reporter.filename)
                        self.cov_obj._warn(msg, slug="couldnt-parse")  # pylint: disable=protected-access

                    else:
                        raise

        return output

    def print_lcov(self) -> None:
        """Print LCOV output

        Print out the LCOV output

        """
        lcov_str = self.get_lcov()
        print(lcov_str)

    def create_lcov(self, output_file_path: str) -> None:
        lcov_str = self.get_lcov()

        with open(output_file_path, "w", encoding="ascii") as output_file:
            output_file.write(lcov_str)


def get_hits(line_num: int, analysis: Analysis) -> Optional[int]:
    if line_num in analysis.missing:
        return 0

    if line_num not in analysis.statements:
        return None

    return 1


@contextlib.contextmanager
def coverage_decorator():
    if os.getenv("COVERAGE", None) == "1":
        coverage_dir = pathlib.Path(os.getenv("COVERAGE_DIR"))
        coverage_file = coverage_dir / ".coverage"
        print(coverage_file, "testing cover config path")
        coverage_manifest = pathlib.Path(os.getenv("COVERAGE_MANIFEST"))
        coverage_sources = coverage_manifest.read_text().splitlines()
        # @TODO: Handle config stuff
        cov = coverage.Coverage(
            data_file=str(coverage_file),
            include=coverage_sources,
            omit=[
                "*/site-packages/*",
                "*/dist-packages/*",
            ],
            branch=True,
        )
        cov.start()

    try:
        yield
    finally:
        if os.getenv("COVERAGE", None) == "1":
            cov.stop()
            cov.save()

            # @TODO: Handle config stuff
            Converter(
                relative_path=True,
                config_file=False,
                data_file_path=str(coverage_file),
            ).create_lcov(os.getenv("COVERAGE_OUTPUT_FILE"))


if __name__ == "__main__":
    with coverage_decorator():
        sys.exit(pytest.main(sys.argv[1:]))
