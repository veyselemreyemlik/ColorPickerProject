from flask import Blueprint, jsonify, request
import cv2
import numpy as np
from utils import closest_color, detect_dominant_color, color_data

# Blueprint oluşturma
api_bp = Blueprint('api', __name__)

# Renk tespiti için API endpoint
@api_bp.route('/detect-color', methods=['POST'])
def detect_color():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    dominant_color = detect_dominant_color(image)
    closest_color_name = closest_color(dominant_color)
    
    return jsonify({"closest_color": closest_color_name, "rgb": dominant_color.tolist()}), 200

# Tüm renk veri setini döndüren API endpoint
@api_bp.route('/colors', methods=['GET'])
def get_colors():
    return jsonify(color_data), 200
