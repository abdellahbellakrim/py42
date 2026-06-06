import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_transpose(img: np.ndarray) -> np.ndarray:
    """Transpose a 2D numpy array manually without any library."""
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("Input must be a numpy array")
        if img.ndim != 2:
            raise ValueError("Input must be a 2D array")

        rows = img.shape[0]  # 400
        cols = img.shape[1]  # 400

        # new array with flipped shape
        transposed = np.empty((cols, rows), dtype=img.dtype)

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = img[i][j]
                # swap row and col index

        return transposed

    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_zoom(img: np.ndarray) -> np.ndarray:
    """Crop a 400x400 square and keep a single channel."""
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("Input must be a numpy array")
        if img.size == 0:
            raise ValueError("Image array is empty")
        if img.ndim != 3:
            raise ValueError("Image must be a 3D array (H, W, C)")

        # same crop as ex03, squeeze removes the (... ,1) dimension
        # giving us a clean 2D array for transpose
        zoomed = img[184:584, 312:712, :1].squeeze()
        # squeeze() removes dimensions of size 1
        # (400, 400, 1) → (400, 400)

        print(f"The shape of image is: {zoomed.shape}")
        print(zoomed)
        return zoomed

    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def main():
    """Load animal.jpeg, crop, transpose and display."""
    try:
        img = ft_load("../animal.jpeg")
        if img.size == 0:
            return

        zoomed = ft_zoom(img)
        if zoomed.size == 0:
            return

        transposed = ft_transpose(zoomed)
        if transposed.size == 0:
            return

        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        plt.imshow(transposed, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
