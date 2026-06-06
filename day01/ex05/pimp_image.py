import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert the colors of the image."""
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array")
        result = 255 - array
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel of the image."""
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array")
        result = array * [1, 0, 0]
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel of the image."""
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array")
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 2] = 0
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of the image."""
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array")
        result = array.copy()
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the image to greyscale."""
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("Input must be a numpy array")
        result = array.copy()
        result[:, :] = array.sum(axis=2, keepdims=True) / 3
        plt.imshow(result)
        plt.show()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])
