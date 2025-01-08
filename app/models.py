import os
import requests
from PIL import Image, ImageDraw, ImageFont
print("incio models")


def save_profile(data, db):
    print("save_profile")
    """Guarda un perfil de persona en la base de datos."""
    try:
        profiles_collection = db["profiles"]
        profiles_collection.insert_one(data)
        return {"status": "success", "message": "Perfil guardado exitosamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_profile(name, db):
    print("get_profile")
    """Obtiene un perfil por nombre."""
    profiles_collection = db["profiles"]
    profile = profiles_collection.find_one({"name": name})
    print(profile)
    return profile

def generate_image(data, db):
    """
    Genera una imagen basada en la descripción y la guarda en local.
    """
    print("generate_image")
    try:
        # Obtener la descripción y la escena
        description = data.get("description", "default_description")
        scene = data.get("scene", "default_scene")
        
        # Simulación de generación de imagen (en este caso, un fondo de color con texto usando Pillow)
        img = Image.new("RGB", (800, 600), color=(73, 109, 137))
        draw = ImageDraw.Draw(img)
        font_size = 20
        font = ImageFont.load_default()  # Puedes usar una fuente más elegante si lo deseas

        # Añadir texto a la imagen
        draw.text((10, 10), f"Description: {description}", fill="white", font=font)
        draw.text((10, 50), f"Scene: {scene}", fill="white", font=font)

        # Definir el nombre del archivo
        output_dir = "generated_images"
        os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
        file_path = os.path.join(output_dir, f"{description}_{scene}.png")
        
        # Guardar la imagen en local
        img.save(file_path)
        print(f"Imagen guardada en: {file_path}")

        return file_path

    except Exception as e:
        return str(e)

print("inocio imgGen")

from diffusers import StableDiffusionPipeline
import torch
import os
from PIL import Image

print("\n\t incio imgGen: importacin de librerias correcta")

def generate_image_with_model(data):
    
    print("\n\t incio imgGen: importacin de librerias correcta")

    """
    Usa un modelo de Stable Diffusion para generar una imagen basada en la descripción.
    """
    model_id = "CompVis/stable-diffusion-v1-4"
    print("antes de cargar el modelo")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    print("despues de cargar el modelo")
    print(pipe)
    pipe = pipe.to("cuda")  # Usa GPU si está disponible
    print("despues de pipe.to")
    description = data.get("description", "default_description")
    print("descripcion: ", description) 
    scene = data.get("scene", "default_scene")
    print("escena: ", scene)
    
    prompt = f"{scene}"
    print("prompt: ", prompt)
    image = pipe(prompt).images[0]


    # Definir el nombre del archivo
    output_dir = "generated_images"
    os.makedirs(output_dir, exist_ok=True)  # Crear el directorio si no existe
    output_path = os.path.join(output_dir, f"{description}_{scene}.png")
    image.save(output_path)
    print("se ha generdo una imagen")
    print("imagen guardada en: ", output_path)
    return output_path
