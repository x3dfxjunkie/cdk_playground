"""
    Source Local
"""
import os

from app.src.load_testing.app.sources.source import Source


class LocalSource(Source):
    """
    Subclass. Implements a sources for sample records for local directories
    locust "users" will need to instatiate this to read sample data
    """

    def __init__(self, samples_dir) -> None:
        self.samples_dir = samples_dir  # Setting the bucket path

    def get_sample_data(self):
        sample_data = []
        files = self.get_file_names()
        for file in files:
            data_file = self.read_content_from_file(file)
            sample_data.extend(data_file)
        return sample_data

    def get_file_names(self):
        file_names = [os.path.join(self.samples_dir, path) for path in os.listdir(self.samples_dir)]
        file_names = [file_name for file_name in file_names if os.path.isfile(file_name)]
        return file_names

    def read_content_from_file(self, file_name):
        with open(file_name, "r", encoding="utf8") as file_obj:
            return file_obj.read().splitlines()
