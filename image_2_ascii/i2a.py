import sys
import typer
from pathlib import Path
from typing import Tuple
from numpy import asarray
from PIL import Image, UnidentifiedImageError

gs_to_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\\()1}{[]?-_+~<>i!lI;:,^.")


def open_image(img_path: Path) -> Image:
    try:
        img = Image.open(img_path)
    except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError) as err:
        print(err)
        sys.exit(1)
    return img


def img_to_ascii(
    img: Image,
    output_size: Tuple[int, int],
    reversed_chars: bool,
    filename: str,
):
    if reversed_chars:
        gs_to_char.reverse()
    output_width, output_height = output_size
    with open(f"{filename}.txt", "w") as f:
        # resize the image
        print("=================\n" "image loaded\n" f"size: {img.width}x{img.height}")
        if output_width > img.width or output_height > img.height:
            raise ValueError(
                "Upscaling not allowed. Please set custom output width and height "
                "to be smaller than source image resolution.\n"
                f"\tTried resize: {img.size} to {output_size}"
            )

        img = img.resize(output_size)
        print(f"resized to: {img.width}x{img.height}")
        data = asarray(img.convert("L"))
        for line in data:
            for pixel in line:
                f.write(gs_to_char[pixel // 4])
            f.write("\n")

        f.close()
        print("done\n=================")


def main(
    image: Path = typer.Argument(..., help="Path to image"),
    output_size: Tuple[int, int] = typer.Option(
        (100, 100), help="Set custom output width and height"
    ),
    reverse: bool = typer.Option(
        False,
        "--reverse",
        "-r",
        help="Reverse the order of chars used in convertion",
    ),
    output_filename: str = typer.Option(
        "output", help="Set name of the txt file where output will be saved"
    ),
):
    """
    Image to ASCII convertion

    By default uses those chars (black --> white)
    $@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\\()1}{[]?-_+~<>i!lI;:,^.
    """
    img = open_image(image)
    img_to_ascii(img, output_size, reverse, output_filename)


if __name__ == "__main__":
    typer.run(main)
