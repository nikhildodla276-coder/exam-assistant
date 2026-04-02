# Exam Assistant

A Python tool that reads PDF study material and uses 
a Large Language Model (LLM) to generate prioritized 
exam notes automatically.

---

## What It Does

1. Accepts a PDF file as input
2. Extracts all text from the PDF using PyMuPDF
3. Sends the extracted text to Groq LLM API
4. Receives prioritized exam notes back from the LLM
5. Displays the notes to the user

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core language |
| PyMuPDF (fitz) | PDF text extraction |
| Groq API | LLM for generating study notes |
| python-dotenv | Secure API key management |

---

## Project Status

Complete. Tested with real university exam PDFs.
Pylint score: 10/10 

---

## Setup and Usage

### 1. Clone the repository
```bash
git clone https://github.com/nikhildodla276-coder/exam-assistant.git
cd exam-assistant
```
### 2. Create virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create your .env file
```
GROQ_API_KEY=your_api_key_here
```
### 4. Run with a PDF
```bash
python assistant.py yourfile.pdf
```

---

## Author

Nikhil Dodla — BTech CSE AIML, Kalinga University