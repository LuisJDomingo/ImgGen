print("inocio routes")

from flask import Blueprint, request, jsonify, current_app
from .models import save_profile, generate_image
from flask import send_from_directory
from flask import render_template

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')  # Asegúrate de tener un archivo index.html en templates
    #return("hola")

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
