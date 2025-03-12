import time
from contextlib import contextmanager


@contextmanager
def timer(name: str):
    """処理の実行時間を計測. with構文で使う.

    Args:
        name (str): 処理名
    """
    t0 = time.time()
    print(f"[{name}] start")
    yield
    print(f"[{name}] done in {time.time() - t0:.0f} s")
