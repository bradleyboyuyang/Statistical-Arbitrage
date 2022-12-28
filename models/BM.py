from typing import Optional
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np


def get_dW(T: int, random_state: Optional[int] = None) -> np.ndarray:
    """
    Sample T times from a normal distribution,
    to simulate discrete increments (dW) of a Brownian Motion.
    Optional random_state to reproduce results.
    """
    np.random.seed(random_state)
    return np.random.normal(0.0, 1.0, T)


def get_W(T: int, random_state: Optional[int] = None) -> np.ndarray:
    """
    Simulate a Brownian motion discretely samplet at unit time increments.
    Returns the cumulative sum
    """
    dW = get_dW(T, random_state)
    # cumulative sum and then make the first index 0.
    dW_cs = dW.cumsum()
    return np.insert(dW_cs, 0, 0)[:-1]


if __name__ == "__main__":
    dW = get_dW(T=1_000)
    W = get_W(T=1_000)
    fig = plt.figure(figsize=(15, 5))

    title = "Brownian motion increments"
    plt.subplot(1, 2, 1)
    plt.plot(dW)
    plt.gca().set_title(title, fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    title = "Brownian motion path"
    plt.subplot(1, 2, 2)
    plt.plot(W)
    plt.gca().set_title(title, fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)