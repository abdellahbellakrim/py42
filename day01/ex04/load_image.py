import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """Load an image from the given path and return it as a NumPy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")
        ext = os.path.splitext(path)[1].lower()
        if ext not in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
            raise ValueError(
                "Only JPG/JPEG/PNG/BMP/WEBP formats are supported"
            )
        img = np.array(Image.open(path))
        if img.size == 0:
            raise ValueError("Image is empty")
        print(f"The shape of image is: {img.shape}")
        print(img)
        return img
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])
