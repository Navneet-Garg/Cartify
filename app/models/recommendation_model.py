import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
import numpy as np
from io import BytesIO
import pandas as pd
from app.config.settings import RECOMMEND_DATA_PATH

# Load CSV file
df = pd.read_csv(RECOMMEND_DATA_PATH)

# Load the pre-trained ResNet50 model (without classification layer)
model = models.resnet50(pretrained=True)
model = nn.Sequential(*list(model.children())[:-1])  # Remove last FC layer
model.eval()  # Set to evaluation mode

# Image preprocessing transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def extract_features(image_file):
    """Extracts features from an image using ResNet50 (PyTorch)"""
    img = Image.open(BytesIO(image_file.read())).convert('RGB')  # Open image
    img = transform(img).unsqueeze(0)  # Apply transformations and add batch dim
    
    with torch.no_grad():
        features = model(img)  # Get features
    features = features.view(-1).numpy()  # Flatten
    features /= np.linalg.norm(features)  # Normalize

    return features

def get_link_by_id(index):
    """Fetches the corresponding link from the CSV using the given ID"""
    result = df[df['id'] == index]['link']
    return result.values[0] if not result.empty else None 