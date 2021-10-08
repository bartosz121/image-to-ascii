import sys
import typer
from pathlib import Path
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


def img_to_ascii(img: Image, reversed_chars: bool):
    if reversed_chars:
        gs_to_char.reverse()
    with open("ascii.txt", "w") as f:
        # resize the image
        aspect_ratio = img.width / img.height
        print("=================\n" "image loaded\n" f"size: {img.width}x{img.height}")
        img = img.resize((200, int(img.height * 0.22 * aspect_ratio)))
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
    reverse: bool = typer.Option(
        False,
        "--reverse",
        "-r",
        help="Reverse the order of chars used in convertion",
    ),
):
    """
    Image to ASCII convertion

    By default uses those chars (black --> white)
    $@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\\()1}{[]?-_+~<>i!lI;:,^.
    """
    img = open_image(image)
    img_to_ascii(img, reverse)


if __name__ == "__main__":
    typer.run(main)
