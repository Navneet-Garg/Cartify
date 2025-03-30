import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Configuration
MONGO_URI = "mongodb+srv://navneetg050:805020@firstmongo.izcl1mo.mongodb.net/testdb?retryWrites=true&w=majority"

# File paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Model paths
import gdown

EMBEDDINGS_PATH = os.path.join(DATA_DIR, r"E:\E_commerce\virtual_env\FLASK\embeddings.pkl")
# gdown.download("https://drive.google.com/uc?id=1PajhKnHhrAkSfclx-ZbvX_8vVvegfqMl", EMBEDDINGS_PATH, quiet=False)
FILENAMES_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\filenames.pkl')
RECOMMEND_DATA_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\recommend_data.csv')
FINAL_FILE_PATH = os.path.join(DATA_DIR, r'E:\E_commerce\virtual_env\FLASK\final_file.csv')

# API Keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# CORS settings
ALLOWED_ORIGINS = ["http://localhost:3000"] 