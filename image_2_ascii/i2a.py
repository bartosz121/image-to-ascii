import sys
from numpy import asarray
from PIL import Image, UnidentifiedImageError

gs_to_char = list(".^,:;Il!i><~+_-?][{}1)(\\/tfjrxnuvczXYUCLQ0OZmwqpdbkhao*#MW&8%B@$")


def open_image(img_path: str):
    try:
        img = Image.open(img_path)
    except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError) as err:
        print(err)
        sys.exit(1)
    return img


def img_to_ascii(img: Image):
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


def main(file: str):
    img = open_image(file)
    img_to_ascii(img)


if __name__ == "__main__":
    main("/home/bartosz/code/image-2-ascii/image_2_asci/lenna.png")
