import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# CORS settings
ALLOWED_ORIGINS = ["http://localhost:3000"]

# File paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FINAL_FILE_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\Cartify\final_file.csv')

class Config:
    # MongoDB Configuration
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://navneetg050:805020@firstmongo.izcl1mo.mongodb.net/testdb?retryWrites=true&w=majority')
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Create a config instance
config = Config() 