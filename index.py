    
from flask import Flask, jsonify
import base64
import os

app = Flask(__name__)

API_KEY = "123"

@app.route('/get-images', methods=['GET'])
def get_images():
    # auth_header = request.headers.get('Authorization')
    # if not auth_header or auth_header.split(" ")[1] != API_KEY:
    #     return jsonify({"error": "Unauthorized"}), 401
    try:
        # Path to the images folder
        images_folder = os.path.join(os.path.dirname(__file__), "images")

        # Check if the folder exists
        if not os.path.exists(images_folder):
            return jsonify({"error": "Images folder not found"}), 404

        # Iterate through all files in the folder
        images_data = []
        for filename in os.listdir(images_folder):
            file_path = os.path.join(images_folder, filename)

            # Check if the file is a valid image
            if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                with open(file_path, "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read()).decode('utf-8')
                
                # Append each image's data as a dictionary
                images_data.append({
                    "filename": filename,
                    "image": b64_string,
                    "format": filename.split('.')[-1]  # Get file format
                })

        # If no images were found
        if not images_data:
            return jsonify({"message": "No images found in the folder"}), 200

        # Return all images in JSON format
        return jsonify({
            "message": "Images retrieved successfully",
            "images": images_data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)
