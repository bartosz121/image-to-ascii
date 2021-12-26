import sys
import typer
from math import ceil
from pathlib import Path
from tqdm import tqdm
from typing import Tuple
from numpy import asarray
from PIL import Image, UnidentifiedImageError

gs_to_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\\()1}{[]?-_+~<>i!lI;:,^.")
divide_by = ceil(256 / len(gs_to_char))


def open_image(img_path: Path) -> Image:
    typer.echo(f"Opening {img_path}")
    try:
        img = Image.open(img_path)
    except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError) as err:
        print(err)
        sys.exit(1)
    return img


def img_to_ascii(
    img: Image,
    output_size: Tuple[int, int],
    filename: str,
    reversed_chars: bool,
    no_resize: bool,
):
    if reversed_chars:
        typer.echo("Reversing chars...")
        gs_to_char.reverse()

    if no_resize:
        typer.echo("No resize enabled...")
        output_size = img.size

    output_width, output_height = output_size
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        if output_width > img.width or output_height > img.height:
            raise ValueError(
                "Upscaling not allowed. Please set custom output width and height "
                "to be smaller than source image resolution.\n"
                f"\tTried resize: {img.size} to {output_size}"
            )

        img = img.resize(output_size)
        typer.echo(f"ASCII size set to {img.size}")
        data = asarray(img.convert("L"))
        for line in tqdm(
            data,
            desc="Converting",
            bar_format="{desc}... {percentage:3.0f}%|{bar:35}{r_bar}",
        ):
            for pixel in line:
                f.write(gs_to_char[pixel // divide_by])
            f.write("\n")

        f.close()
        typer.echo(f"Output saved to {filename}.txt!")


def main(
    image: Path = typer.Argument(..., help="Path to image"),
    output_size: Tuple[int, int] = typer.Option(
        (100, 40), help="Set custom output width and height"
    ),
    output_filename: str = typer.Option(
        "output", help="Set name of the txt file where output will be saved"
    ),
    reverse: bool = typer.Option(
        False,
        "--reverse",
        "-r",
        help="Reverse the order of chars used in convertion",
    ),
    no_resize: bool = typer.Option(
        False, "--no-resize", help="Output width and height are the same as the image"
    ),
):
    """
    Image to ASCII convertion

    By default uses those chars (black --> white)
    $@B%8&WM#*oahkbdpqwmZO0QLCUYXzcvunxrjft/\\()1}{[]?-_+~<>i!lI;:,^.
    """
    typer.echo("======IMAGE=2=ASCII======")
    img = open_image(image)
    typer.echo("Image loaded!")
    img_to_ascii(img, output_size, output_filename, reverse, no_resize)
    typer.echo("==========DONE===========")


if __name__ == "__main__":
    typer.run(main)
