import random
import time

from opentelemetry.sdk.trace.id_generator import IdGenerator, RandomIdGenerator


class G360XRayIdGenerator(IdGenerator):

    random_id_generator = RandomIdGenerator()

    def generate_span_id(self) -> int:
        print("Really?")
        return self.random_id_generator.generate_span_id()

    @staticmethod
    def generate_trace_id() -> int:
        trace_time = int(time.time())
        trace_identifier = random.getrandbits(96)
        return 0
