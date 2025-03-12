import os
import random

import numpy as np


def seed_everything(seed: int):
    """seed値を固定する関数

    Args:
        seed (int): seed値
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
