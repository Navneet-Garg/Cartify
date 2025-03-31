from flask import Blueprint, request, jsonify
import os
from sklearn.metrics.pairwise import cosine_similarity
from app.models.anomaly_model import extract_features, calculate_ssim

bp = Blueprint('anomaly', __name__)

@bp.route('/upload', methods=['POST'])
def upload_images():
    try:
        if 'image1' not in request.files or 'image2' not in request.files:
            return jsonify({'error': 'No images provided'}), 400

        image1 = request.files['image1']
        image2 = request.files['image2']

        # Save images temporarily
        image1_path = "image1.jpg"
        image2_path = "image2.jpg"
        image1.save(image1_path)
        image2.save(image2_path)

        # Extract features from both images
        features1 = extract_features(image1_path)
        features2 = extract_features(image2_path)

        if features1 is None or features2 is None:
            return jsonify({'error': 'Error extracting features from one or both images'}), 500

        # Calculate Cosine Similarity
        similarity_cosine = cosine_similarity([features1], [features2])[0][0]

        # Calculate SSIM
        similarity_ssim = calculate_ssim(image1_path, image2_path)

        # Combined similarity score (weighted average)
        final_similarity = (0.7 * similarity_cosine) + (0.3 * similarity_ssim)

        # Set decision threshold
        if final_similarity > 0.85:
            decision = "✅ Match Confirmed"
        elif final_similarity > 0.6:
            decision = "⚠️ Review Needed"
        else:
            decision = "❌ Possible Anomaly - Reupload Required"

        # Clean up saved images
        os.remove(image1_path)
        os.remove(image2_path)

        return jsonify({
            'similarity_score': float(similarity_cosine),
            'ssim_similarity': float(similarity_ssim),
            'final_similarity': float(final_similarity),
            'decision': decision
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
