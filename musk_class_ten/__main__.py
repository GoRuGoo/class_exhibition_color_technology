import cv2

from .functions.add_alpha_channel import add_alpha_channel_255
from .functions.convert_green_to_black import convert_green_to_black


def main():
    image_w_alpha = add_alpha_channel_255("girl.png")
    after_convert = convert_green_to_black(image_w_alpha)
    cv2.imwrite("test.png", after_convert)


if __name__ == "__main__":
    main()
