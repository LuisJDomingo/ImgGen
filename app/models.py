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
