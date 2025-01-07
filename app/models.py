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
    print("generate_image")
    """
    Genera una imagen basada en la descripción usando un modelo de IA.
    """
    try:
        # Aquí va la lógica de generación de imágenes con el motor de IA
        description = data.get("description", "")
        scene = data.get("scene", "")

        # Ejemplo ficticio: Retornar una URL de imagen generada
        image_url = f"https://fake.image.service/{description}_{scene}.png"
        print(image_url)
        return image_url
    except Exception as e:
        return str(e)
