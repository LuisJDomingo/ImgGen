print("inocio imgGen")

from diffusers import StableDiffusionPipeline
import torch
import os
from PIL import Image

print("\n\t incio imgGen: importacin de librerias correcta")

def generate_image_with_model(description, scene):
    """
    Usa un modelo de Stable Diffusion para generar una imagen basada en la descripción.
    """
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Usa GPU si está disponible

    prompt = f"{description}, {scene}"
    image = pipe(prompt).images[0]

    # Guardar la imagen localmente (puedes modificar la ruta según sea necesario)
    output_path = f"generated_images/{description.replace(' ', '_')}.png"
    image.save(output_path)
    print("se ha generdo una imagen")
    print(output_path)
    return output_path
