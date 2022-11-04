import cv2
from test_code.functions.add_alpha_channel import add_alpha_channel_255
from test_code.functions.convert_green_to_black import convert_green_to_black
from test_code.functions.transparent_black_ground import transparent_black_ground


def main():
    image_wo_alpha = cv2.imread("./test_code/functions/normal.png")
    after_convert = convert_green_to_black(
        image_wo_alpha, 50, 100, 130, 255, False, 204, 255
    )
    after_convert = add_alpha_channel_255(after_convert)
    transparent_image = transparent_black_ground(after_convert)
    cv2.imwrite("after_transparent.png", transparent_image)


if __name__ == "__main__":
    main()
