from numpy import asarray
from PIL import Image

gs_to_char = list(".^,:;Il!i><~+_-?][{}1)(\\/tfjrxnuvczXYUCLQ0OZmwqpdbkhao*#MW&8%B@$")


def transform(file):
    with open("ascii.txt", "w") as f:
        with Image.open(file) as img:
            # resize the image
            aspect_ratio = img.width / img.height
            print(
                "=================\n" "image loaded\n" f"size: {img.width}x{img.height}"
            )
            img = img.resize((200, int(img.height * 0.22 * aspect_ratio)))
            print(f"resized to: {img.width}x{img.height}")
            data = asarray(img.convert("L"))
            for y in data:
                for x in y:
                    f.write(gs_to_char[x // 4])
                f.write("\n")

            f.close()
            print("done\n=================")


if __name__ == "__main__":
    transform("lenna.png")
