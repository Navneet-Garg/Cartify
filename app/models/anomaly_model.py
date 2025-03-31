import numpy as np
import cv2
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from skimage.metrics import structural_similarity as ssim

# Load pre-trained ResNet50 model (without classification layers)
model = ResNet50(weights="imagenet", include_top=False, pooling="avg")

def enhance_image(image_path):
    """Preprocesses the image to improve quality before feature extraction."""
    image = cv2.imread(image_path)

    # Convert to grayscale & apply histogram equalization
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced = cv2.equalizeHist(gray)

    # Apply Gaussian blur for noise reduction
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)

    # Convert back to 3 channels for ResNet50
    enhanced_image = cv2.merge([blurred, blurred, blurred])
    return enhanced_image

def extract_features(image_path):
    """Extracts features using ResNet50 after image enhancement."""
    try:
        # Enhance image quality
        enhanced_img = enhance_image(image_path)
        cv2.imwrite("enhanced.jpg", enhanced_img)  # Save temp image

        # Load and resize image for ResNet50
        image = load_img("enhanced.jpg", target_size=(224, 224))
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        processed_image = preprocess_input(image_array)

        # Extract features using the model
        features = model.predict(processed_image)
        return features.flatten()  # Convert to 1D vector
    except Exception as e:
        print(f"Error in extract_features: {str(e)}")
        return None 

def calculate_ssim(image1_path, image2_path):
    """Computes Structural Similarity Index (SSIM) between two images."""
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize to the same shape
    img1 = cv2.resize(img1, (224, 224))
    img2 = cv2.resize(img2, (224, 224))

    score, _ = ssim(img1, img2, full=True)
    return score
