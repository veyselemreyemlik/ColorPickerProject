import json
import cv2
import numpy as np
from math import sqrt

# JSON dosyasını yükleyin
with open('colors.json', 'r') as f:
    color_data = json.load(f)

# En yakın rengi bulma fonksiyonu
def closest_color(rgb_input):
    closest_color_name = None
    min_distance = float('inf')
    
    for color_key, color_info in color_data.items():
        r, g, b = color_info['rgb']
        distance = sqrt((rgb_input[0] - r) ** 2 + (rgb_input[1] - g) ** 2 + (rgb_input[2] - b) ** 2)
        
        if distance < min_distance:
            min_distance = distance
            closest_color_name = color_info['name']
            
    return closest_color_name

# OpenCV ile baskın rengi tespit eden fonksiyon
def detect_dominant_color(image):
    pixels = np.float32(image.reshape(-1, 3))
    n_colors = 1
    
    _, labels, palette = cv2.kmeans(
        pixels, n_colors, None, 
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.2), 
        10, cv2.KMEANS_RANDOM_CENTERS
    )
    dominant_color = palette[0].astype(int)
    return dominant_color
