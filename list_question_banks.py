import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
canvas_api_key = os.getenv("CANVAS_API_KEY")
canvas_api_url = os.getenv("CANVAS_API_URL")
course_id = "162259"  # Update to your course ID if needed

headers = {
    "Authorization": f"Bearer {canvas_api_key}"
}

# List all question banks for the course
list_banks_url = f"{canvas_api_url}/api/v1/courses/{course_id}/question_banks"
response = requests.get(list_banks_url, headers=headers)
if not response.ok:
    print("Error listing question banks:")
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    response.raise_for_status()

banks = response.json()
print("Question Banks for course", course_id)
for bank in banks:
    print(f"ID: {bank['id']}, Title: {bank['title']}")
