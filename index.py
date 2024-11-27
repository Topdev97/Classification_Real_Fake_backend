from flask import Flask, jsonify, request, send_file
import base64
import os

app = Flask(__name__)

API_KEY = "123"


@app.route('/get-image', methods=['GET'])
def get_image():
    
    # auth_header = request.headers.get('Authorization')
    # if not auth_header or auth_header.split(" ")[1] != API_KEY:
    #     return jsonify({"error": "Unauthorized"}), 401
    try:
        image_path = "example.jpeg"

        if not os.path.exists(image_path):
            return jsonify({"error": "Image file not found"}), 404

        with open(image_path, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read()).decode('utf-8')

        return jsonify({
            "message": "Image retrieved successfully",
            "image": b64_string,
            "format": "jpg"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000, debug=True)