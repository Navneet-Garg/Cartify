from flask import Blueprint, request, jsonify
from app.models.recommendation_model import extract_features, get_link_by_id
from app.config.settings import EMBEDDINGS_PATH, FILENAMES_PATH
import numpy as np
import pickle

bp = Blueprint('recommendation', __name__)

# Load precomputed feature list and filenames
feature_list = np.array(pickle.load(open(EMBEDDINGS_PATH, "rb")))
filenames = pickle.load(open(FILENAMES_PATH, "rb"))

@bp.route('/recommend', methods=['POST'])
def recommend():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    image_file = request.files['file']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        query_features = extract_features(image_file)
        similarities = np.matmul(query_features, feature_list.T)  # Compute similarity
        indices = np.argsort(similarities)[-5:][::-1]  # Get top 5 similar images
        
        # Convert indices to corresponding numbers
        recommended_numbers = [int(filenames[i].split("\\")[-1].split(".")[0]) for i in indices]
        
        # Get corresponding links from CSV
        recommended_links = [get_link_by_id(num) for num in recommended_numbers]

        return jsonify({"recommended_numbers": recommended_numbers, "recommended_links": recommended_links})
    except Exception as e:
        return jsonify({'error': str(e)}), 500 