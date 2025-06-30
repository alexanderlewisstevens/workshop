import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

canvas_api_key = os.getenv("CANVAS_API_KEY")
canvas_api_url = os.getenv("CANVAS_API_URL")

# Set your course ID here
course_id = "196655"  # Replace with your actual course ID

if not canvas_api_key or not canvas_api_url:
    raise ValueError("CANVAS_API_KEY or CANVAS_API_URL not found in environment variables.")

headers = {
    "Authorization": f"Bearer {canvas_api_key}"
}

try:
    # Test: Get current user profile
    response = requests.get(f"{canvas_api_url}/api/v1/users/self/profile", headers=headers)
    response.raise_for_status()
    profile = response.json()
    print("Canvas API key is valid. User profile:")
    print(json.dumps(profile, indent=2))
except Exception as e:
    print("Failed to use Canvas API:", e)

try:
    # Get course info
    response = requests.get(f"{canvas_api_url}/api/v1/courses/{course_id}", headers=headers)
    response.raise_for_status()
    course_info = response.json()
    print("Course info:")
    print(json.dumps(course_info, indent=2))
except Exception as e:
    print("Failed to get course info:", e)
