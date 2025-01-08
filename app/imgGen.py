print("inocio imgGen")

from diffusers import StableDiffusionPipeline
import torch
import os
from PIL import Image

print("\n\t incio imgGen: importacin de librerias correcta")

def generate_image_with_model(scene):
    
    print("\n\t incio imgGen: importacin de librerias correcta")

    """
    Usa un modelo de Stable Diffusion para generar una imagen basada en la descripción.
    """
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Usa GPU si está disponible

    prompt = f"{scene}"
    image = pipe(prompt, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale, generator=generator).images[0]

    # Definir el nombre del archivo
    output_dir = "generated_images"
    os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
    output_path = os.path.join(output_dir, f"{description}_{scene}.png")
    image.save(output_path)
    print("se ha generdo una imagen")
    print("imagen guardada en: ", output_path)
    return output_path
