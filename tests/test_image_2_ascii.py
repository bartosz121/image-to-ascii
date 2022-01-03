import os
import unittest
import numpy as np
from PIL import Image

from image_2_ascii import i2a

TESTDATA_DEFAULT_TXT = os.path.join(os.path.dirname(__file__), "logo_default.txt")
TESTDATA_NORESIZE_TXT = os.path.join(os.path.dirname(__file__), "logo_noresize.txt")
TESTDATA_REVERSED_TXT = os.path.join(os.path.dirname(__file__), "logo_reversed.txt")
TESTDATA_IMG = os.path.join(os.path.dirname(__file__), "logo.jpg")


def get_default_output() -> np.ndarray:
    with open(TESTDATA_DEFAULT_TXT, "r", encoding="utf-8") as f:
        file_data = [list(line.strip()) for line in f]
    return file_data


def get_noresize_output() -> np.ndarray:
    with open(TESTDATA_NORESIZE_TXT, "r", encoding="utf-8") as f:
        file_data = [list(line.strip()) for line in f]
    return file_data


def get_reversed_output() -> np.ndarray:
    with open(TESTDATA_REVERSED_TXT, "r", encoding="utf-8") as f:
        file_data = [list(line.strip()) for line in f]
    return file_data


def get_img() -> Image:
    img = Image.open(TESTDATA_IMG)
    return img


class CustomAssertion:
    def assertLists(self, first, second):
        """
        Unittest 'self.assertLists' took way too long when failed
        because of difference logging, this 'fails' faster
        """
        for a, b in zip(first, second):
            if a != b:
                raise AssertionError(f"Lists not equal; {a!r} != {b!r}")


class TestConvertion(unittest.TestCase, CustomAssertion):

    maxDiff = 1

    def setUp(self) -> None:
        self.img = get_img()

    def test_default_convertion(self) -> None:
        correct_data = get_default_output()
        default_resize_img = self.img.resize((100, 40))
        result = i2a.convert(default_resize_img)
        self.assertLists(correct_data, result.tolist())

    def test_no_resize_convertion(self) -> None:
        correct_data = get_noresize_output()
        result = i2a.convert(self.img)
        self.assertLists(correct_data, result.tolist())

    def test_reverse_chars_convertion(self) -> None:
        correct_data = get_reversed_output()
        default_resize_img = self.img.resize((100, 40))
        i2a.gs_to_char.reverse()
        result = i2a.convert(default_resize_img)
        self.assertLists(correct_data, result.tolist())


if __name__ == "__main__":
    unittest.main()
