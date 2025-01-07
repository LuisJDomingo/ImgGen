print("inocio utils")

from io import BytesIO
import base64

# Función para guardar la imagen generada en la base de datos
def save_generated_image(image, scene):
    # Guardar la imagen en formato JPG o PNG
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    # Guardar la imagen en la base de datos
    scene.generated_image = img_str
    scene.save()

# Ruta para crear una persona y generar su imagen
def create_person_and_generate_image(person_data, scene_data):
    # Guardar la persona en la base de datos
    person = save_person(person_data)
    
    # Crear el prompt para la imagen
    prompt = f"Una persona con {person_data['appearance']} y ropa {person_data['clothing']} con expresión {person_data['facial_expression']} en un lugar {scene_data['location']} con iluminación {scene_data['lighting']}."

    # Generar la imagen
    image = generate_image(prompt)

    # Guardar la escena
    scene = save_scene(scene_data, person)
    
    # Guardar la imagen generada en la base de datos
    save_generated_image(image, scene)
    
    return scene
