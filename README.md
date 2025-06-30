# Workshop OpenAI API Example

This project demonstrates how to use the OpenAI API in Python with environment variables for configuration.

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```sh
   cp .env.example .env
   # Then edit .env to add your key
   ```
2. (Recommended) Create and activate a virtual environment:
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the example:
   ```sh
   python example.py
   ```

## Files
- `example.py`: Example script using OpenAI API
- `.env.example`: Template for environment variables
- `requirements.txt`: Python dependencies
- `.gitignore`: Standard Python and environment ignores

## Requirements
- Python 3.8+
- OpenAI API key (get one at https://platform.openai.com/)
