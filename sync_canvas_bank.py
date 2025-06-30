import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
canvas_api_key = os.getenv("CANVAS_API_KEY")
canvas_api_url = os.getenv("CANVAS_API_URL")
course_id = "162259"  # Updated to your Discrete Structures in CS course

headers = {
    "Authorization": f"Bearer {canvas_api_key}"
}

# Path to your local JSON file
json_path = "testing_bank/sample_bank_all_types.json"

# Load local question bank
with open(json_path, "r") as f:
    bank = json.load(f)

title = "testing_bank"
description = bank.get("description", "")

# Check if the question bank already exists
list_banks_url = f"{canvas_api_url}/api/v1/courses/{course_id}/question_banks"
list_response = requests.get(list_banks_url, headers=headers)
if not list_response.ok:
    print("Error listing question banks:")
    print("Status code:", list_response.status_code)
    print("Response text:", list_response.text)
    list_response.raise_for_status()

banks = list_response.json()
canvas_bank_id = None
for b in banks:
    if b.get("title") == title:
        canvas_bank_id = b["id"]
        print(f"Found existing Canvas question bank '{title}' with id {canvas_bank_id}")
        break

# If not found, create it
if not canvas_bank_id:
    create_bank_url = f"{canvas_api_url}/api/v1/courses/{course_id}/question_banks"
    create_bank_data = {"title": title, "description": description}
    response = requests.post(create_bank_url, headers=headers, data=create_bank_data)
    if not response.ok:
        print("Error creating question bank:")
        print("Status code:", response.status_code)
        print("Response text:", response.text)
        response.raise_for_status()
    canvas_bank = response.json()
    canvas_bank_id = canvas_bank["id"]
    print(f"Created Canvas question bank '{title}' with id {canvas_bank_id}")

# Add each question to the bank
for q in bank["questions"]:
    question_data = {
        "question": {
            "question_name": q["question_name"],
            "question_text": q["question_text"],
            "question_type": q["question_type"],
            "answers": q.get("answers", []),
            "general_feedback": q.get("general_feedback", "")
        }
    }
    add_q_url = f"{canvas_api_url}/api/v1/courses/{course_id}/question_banks/{canvas_bank_id}/questions"
    q_response = requests.post(add_q_url, headers=headers, json=question_data)
    q_response.raise_for_status()
    print(f"Added question: {q['question_name']}")

print("Sync complete.")
