print("inocio imgGen")

from diffusers import StableDiffusionPipeline
import torch
import os
from PIL import Image

print("\t incio imgGen: importacion de librerias correcta")

def generate_image_with_model(scene, description="default_description"):
        
    print("disponibilidad: ", torch.cuda.is_available())
    """
    Usa un modelo de Stable Diffusion para generar una imagen basada en la descripción.
    """
    model_id = "CompVis/stable-diffusion-v1-4"
    
    # Verificar si CUDA está disponible y usarla, de lo contrario usar CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cuda":
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        pipe = pipe.to(device)
        print("cuda disponible")
    else:
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        print("cuda no disponible")
        print(pipe)
                
    
    # description = data.get("description", "default_description")
    print("descripcion: ", description) 
    # scene = data.get("scene", "default_scene")
    print("escena: ", scene)
    
    prompt = f"{scene}"
    print("prompt: ", prompt)
    image = pipe(prompt).images[0]

    print("imagen generada")
    # Definir el nombre del archivo
    output_dir = "generated_images"
    os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
    output_path = os.path.join(output_dir, f"{description}_{scene}.png")
    image.save(output_path)
    print("se ha generdo una imagen")
    print("imagen guardada en: ", output_path)
    return output_path
