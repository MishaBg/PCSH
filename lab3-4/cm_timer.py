import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f'cm1: time: {self.end_time - self.start_time:.2f}')


@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print(f'cm2: time: {end_time - start_time:.2f}')


def main():
    with cm_timer_1():
        time.sleep(0.7)

    with cm_timer_2():
        time.sleep(0.5)


if __name__ == '__main__':
    main()
