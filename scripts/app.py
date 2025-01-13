import gradio as gr

def process_image(image):
    # Placeholder function to process the image
    return image

with gr.Blocks() as demo:
    with gr.Row():
        input_image = gr.Image(label="Input Image")
        output_image = gr.Image(label="Output Image")
    
    input_image.change(fn=process_image, inputs=input_image, outputs=output_image)

demo.launch()