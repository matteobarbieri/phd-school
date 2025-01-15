import gradio as gr

import numpy as np

import cv2  # This imports the OpenCV library

from PIL import Image

from phd_school.utils.data_preprocessing import (
    pre_process_image,
    find_corners_of_largest_polygon,
    crop_and_warp,
    remove_stuff,
)

from phd_school.models.lightning import LitClassification
from phd_school.models.model_wrapper_complete import TrainedTorchModelWrapper

from phd_school.utils.drawing import fill_in_img

from phd_school.utils.classifier import smart_classify

from phd_school.utils.sudoku import solve_array


def process_image(img):

    # Unclear why this is needed inside the function
    def slice_grid(grid, i, j, W):
        """
        Assuming grid is an array representing the image, return a single square
        based on its coordinates (which start from 0).
        """

        i_start = i * W
        i_end = i_start + W

        j_start = j * W
        j_end = j_start + W

        aa = grid[i_start:i_end, j_start:j_end]
        return aa

    def convert(d: str) -> int:
        return 0 if d == " " else int(d)

    #####

    # Convert to grayscale
    # TODO maybe check the color format beforehand? [RGB/RGBA/GRAY]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pre_preocessed = pre_process_image(img_gray)

    # Find the 4 corners of the external grid
    corners = find_corners_of_largest_polygon(pre_preocessed)

    # Crop the image and compensate for warp
    cropped = crop_and_warp(pre_preocessed, corners)

    w, _ = cropped.shape

    W = w // 9

    model = LitClassification.load_from_checkpoint(
        "home/models/best_candidate.ckpt"
    ).model

    wrapped_classifier_torch = TrainedTorchModelWrapper(model, conf_threshold=0.1)

    # We call the `smart_classify` function on all 81 cells, and we save the results in a list
    digits = list()

    for i in range(9):
        for j in range(9):

            test_cell = slice_grid(cropped, i, j, W)
            cleaned = remove_stuff(test_cell)
            resized = cv2.resize(cleaned, (28, 28), interpolation=cv2.INTER_AREA)

            digits.append(smart_classify(resized, wrapped_classifier_torch))

    digits_int = np.array([convert(d) for d in digits])
    digits_int = digits_int.reshape((9, 9))
    digits_list = [list(ll) for ll in list(digits_int)]

    original_digits_arr = np.array(digits_list)

    solve_array(digits_list)

    resized = cv2.resize(255 - cropped, (512, 512), interpolation=cv2.INTER_AREA)
    resized_pil = Image.fromarray(resized)

    filled_in_img = fill_in_img(
        resized_pil.copy(), original_digits_arr, np.array(digits_list)
    )

    return filled_in_img


with gr.Blocks() as demo:

    with gr.Row():
        process_button = gr.Button("Process Image")

    with gr.Row():
        input_image = gr.Image(label="Input Image")
        output_image = gr.Image(label="Output Image")

    process_button.click(fn=process_image, inputs=input_image, outputs=output_image)


demo.launch()
