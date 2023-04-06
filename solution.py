import pandas as pd
import numpy as np


chat_id = 501141319 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = x/(90**2)
    return a.mean()
