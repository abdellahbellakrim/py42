import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate BMI from height (m) and weight (kg) lists."""
    try:
        h = np.array(height)
        w = np.array(weight)
        if h.shape != w.shape:
            raise ValueError("Lists must be the same size")
        if not (np.issubdtype(h.dtype, np.number)
                and np.issubdtype(w.dtype, np.number)):
            raise TypeError("Lists must contain numbers")
        return (w / (h ** 2)).tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI value above the given limit."""
    try:
        arr = np.array(bmi)
        return (arr > limit).tolist()
    except Exception as e:
        print(f"Error: {e}")
        return []
