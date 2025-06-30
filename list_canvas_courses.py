import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
canvas_api_key = os.getenv("CANVAS_API_KEY")
canvas_api_url = os.getenv("CANVAS_API_URL")

headers = {
    "Authorization": f"Bearer {canvas_api_key}"
}

# List all courses for the current user
list_courses_url = f"{canvas_api_url}/api/v1/courses"
response = requests.get(list_courses_url, headers=headers)
if not response.ok:
    print("Error listing courses:")
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    response.raise_for_status()

courses = response.json()
print("Your available courses:")
for course in courses:
    print(f"ID: {course['id']}, Name: {course.get('name', 'No Name')}")
