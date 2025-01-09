import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HUGGING_FACE_API_TOKEN = os.environ.get('HUGGING_FACE_API_TOKEN') or 'your-secret-key-here'
    REPLICATE_API_TOKEN = os.environ.get('REPLICATE_API_TOKEN') or 'your-secret-key-here'