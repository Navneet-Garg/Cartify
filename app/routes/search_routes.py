from flask import Blueprint, request, jsonify
import pandas as pd
from app.config.settings import FINAL_FILE_PATH

bp = Blueprint('search', __name__)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(FINAL_FILE_PATH)

@bp.route('/get_data', methods=['POST'])
def get_data():
    try:
        # Get JSON data from the request
        data = request.get_json()

        if not data or 'articleType' not in data:
            return jsonify({"error": "Missing 'articleType' in request body"}), 400

        article_type = data['articleType'].strip().lower()

        if not article_type:
            return jsonify({"error": "Invalid articleType"}), 400

        # Ensure column values are strings before applying str.lower()
        df['articleType'] = df['articleType'].astype(str).str.lower()

        # Filter DataFrame based on the articleType (case-insensitive search)
        filtered_data = df[df['articleType'].str.contains(article_type, na=False, regex=False)]

        if filtered_data.empty:
            return jsonify({"message": "No items found for the given article type."}), 404

        # Convert DataFrame to JSON response
        return jsonify(filtered_data.to_dict(orient='records'))

    except Exception as e:
        return jsonify({"error": str(e)}), 500 