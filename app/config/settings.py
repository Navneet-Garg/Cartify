import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

# Debugging (Remove in production)
print(f"Loading environment variables from: {dotenv_path}")

# API Keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# CORS settings
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# File paths
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Model paths
EMBEDDINGS_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\embeddings.pkl')
FILENAMES_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\filenames.pkl')
RECOMMEND_DATA_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\recommend_data.csv')
FINAL_FILE_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\final_file.csv')

class Config:
    """Application Configuration"""

    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://navneetg050:805020@firstmongo.izcl1mo.mongodb.net/testdb?retryWrites=true&w=majority')

    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

# Create a config instance
config = Config()

# Debugging (Remove in production)
print("GOOGLE_API_KEY Loaded:", GOOGLE_API_KEY)
print("SECRET_KEY Loaded:", config.SECRET_KEY)
print("FLASK_DEBUG Mode:", config.DEBUG)
print("MongoDB URI Loaded:", config.MONGO_URI)

# Export all necessary variables
__all__ = ['GOOGLE_API_KEY', 'ALLOWED_ORIGINS', 'FINAL_FILE_PATH', 'RECOMMEND_DATA_PATH', 'EMBEDDINGS_PATH', 'FILENAMES_PATH', 'config']
