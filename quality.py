import cv2
import numpy as np


# Read Uploaded Image
def read_image(uploaded_file):
    uploaded_file.seek(0)
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return image


# Blur Detection
def check_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    return blur_score


# Brightness Detection
def check_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    return brightness


# Contrast Detection
def check_contrast(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contrast = np.std(gray)
    return contrast


# Noise Detection
def check_noise(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    noise = np.mean(cv2.absdiff(gray, blur))
    return noise


# Overall Quality Score
def overall_score(blur, brightness, contrast, noise):

    score = 100

    # Blur
    if blur < 150:
        score -= 30

    # Brightness
    if brightness < 80 or brightness > 180:
        score -= 20

    # Contrast
    if contrast < 50:
        score -= 20

    # Noise
    if noise > 15:
        score -= 30

    if score >= 90:
        status = "🌟 Excellent"

    elif score >= 75:
        status = "✅ Good"

    elif score >= 50:
        status = "⚠️ Average"

    else:
        status = "❌ Poor"

    return score, status