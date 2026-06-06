import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_zoom(img: np.ndarray) -> np.ndarray:
    """Crop a 400x400 square region and keep a single channel."""
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("Input must be a numpy array")
        if img.size == 0:
            raise ValueError("Image array is empty")
        if img.ndim != 3:
            raise ValueError("Image must be a 3D array (H, W, C)")
        zoomed = img[184:584, 412:812, :1]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        return zoomed
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def main():
    """Load animal.jpeg, zoom in and display it."""
    try:
        img = ft_load("animal.jpeg")
        if img.size == 0:
            return
        zoomed = ft_zoom(img)
        if zoomed.size == 0:
            return
        plt.imshow(zoomed, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
