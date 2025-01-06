import sys
print(sys.executable)
print(sys.path)

import os
from flask import Flask, request, jsonify, render_template
import torch
from torchvision import transforms
from PIL import Image
from io import BytesIO
from multilingual_translation import translate # Hypothetical module for multi-language support
from image_generation_engine import ImageGenerator # Hypothetical custom model for image generation

app = Flask(__name__)

# Initialize the custom image generation engine
generator = ImageGenerator(model_path="path_to_trained_model")
translator = translate(languages=['en', 'es'])

# Define a route for generating an image
@app.route('/generate_image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt', '')
    person_profile = data.get('person_profile', None)
    scene_details = data.get('scene_details', '')
    customization_options = data.get('customization_options', {})

    if not prompt and not scene_details:
        return jsonify({"error": "A prompt or scene details are required."}), 400

    try:
        # Translate prompt to English for processing if necessary
        prompt_en = translator.translate_to_english(prompt)
        scene_details_en = translator.translate_to_english(scene_details)

        # Combine person profile and scene details into a single description
        complete_prompt = f"{person_profile}: {scene_details_en}" if person_profile else scene_details_en

        # Generate the image
        generated_image = generator.generate_image(
            prompt=complete_prompt,
            customization_options=customization_options
        )

        # Save the generated image in-memory
        image_buffer = BytesIO()
        generated_image.save(image_buffer, format="PNG")
        image_buffer.seek(0)

        # Send the image back as a response
        return send_file(image_buffer, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to save a person's profile
@app.route('/save_person_profile', methods=['POST'])
def save_person_profile():
    data = request.json
    profile_name = data.get('profile_name', '')
    description = data.get('description', '')

    if not profile_name or not description:
        return jsonify({"error": "Profile name and description are required."}), 400

    try:
        profile_path = os.path.join("profiles", f"{profile_name}.txt")
        with open(profile_path, 'w') as profile_file:
            profile_file.write(description)

        return jsonify({"message": "Profile saved successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve the web interface
@app.route('/interface', methods=['GET'])
def interface():
    return render_template('interface.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
