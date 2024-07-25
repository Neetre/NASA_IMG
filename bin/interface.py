import gradio as gr
from api_module import get_apod, search_asteroids, create_plot, save_data


def interface():
    with gr.Blocks() as demo:
        gr.Markdown('# NASA API Interface')
        
        with gr.Tab('APOD', 'Get Astronomy Picture of the Day'):
            gr.Markdown('Get the Astronomy Picture of the Day from NASA.')
            count = gr.Slider(minimum=1, maximum=10, value=1, label='Number of images')
            get_apod_button = gr.Button('Get APOD')
            image_data = gr.Text('text', type='text', label='APOD Data')
            image = gr.Image('image', type='pil', label='APOD Image')
            save_img = gr.Button('Download image')

            get_apod_button.click(get_apod, inputs=[count], outputs=[image_data, image])

        with gr.Tab('Asteroids', 'Search Asteroids'):
            gr.Markdown('Search for asteroids using NASA API.')
            asteroids_data = gr.Text('text', type='text', label='Asteroids Data')
            asteroid_img = gr.Image('image', type='pil', label='Asteroid Image')
            save_button = gr.Button('Save Data')

        with gr.Tab('Plot', 'Create Plot'):
            gr.Markdown('Create a plot using NASA data.')
            gr.Image('plot', type='pil', label='Plot')
            save_button = gr.Button('Save Plot')

    demo.launch(inbrowser=True)
    
if __name__ == "__main__":
    interface()