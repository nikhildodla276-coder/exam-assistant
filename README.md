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

Currently in development. Core logic being built.

---

## Author

Nikhil Dodla — BTech CSE AIML, Kalinga University