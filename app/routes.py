print("inocio routes")

from flask import Blueprint, request, jsonify, current_app
from .models import save_profile, generate_image
from .imgGen import generate_image_with_model
from flask import send_from_directory
from flask import render_template

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route("/save_profile", methods=["POST"])
def save_profile_route():
    data = request.json
    response = save_profile(data, current_app.db)
    return jsonify(response)

@main_bp.route("/generate_image", methods=["POST"])
def generate_image_route():
    data = request.json
    image = generate_image(data, current_app.db)
    return jsonify({"image_url": image})

@main_bp.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@main_bp.route('/generate_image_with_model', methods=['POST'])
def generate_image_with_model_route():
    """
    Ruta para generar una imagen con Stable Diffusion.
    """
    try:
        # Obtener datos del cuerpo de la solicitud
        data = request.get_json()
        print("data: ", data)
        description = data.get("user_description")
        print("descripcion: ", description)
        scene = data.get("scene")
        print("escena: ", scene)

        '''
        if not description: #or not scene:
            return jsonify({"error": "Faltan 'description' o 'scene' en la solicitud"}), 400
        '''
        
        print("antes de llamar a la función de generación de imágenes")
        # Llamar a la función de generación de imágenes
        image_path = generate_image_with_model(scene)
        print("path imagen generada: ", image_path)
        # Devolver la ruta del archivo generado
        return jsonify({"message": "Imagen generada con éxito", "image_path": image_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

