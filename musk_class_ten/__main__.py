import cv2

from .functions.add_alpha_channel import add_alpha_channel_255
from .functions.convert_green_to_black import convert_green_to_black
from .functions.transparent_black_ground import transparent_black_ground


def main():
    image_wo_alpha = cv2.imread("gorugo.png")
    after_convert = convert_green_to_black(image_wo_alpha)
    after_convert = add_alpha_channel_255(after_convert)
    transparent_image = transparent_black_ground(after_convert)
    cv2.imwrite("test.png", transparent_image)


if __name__ == "__main__":
    main()
