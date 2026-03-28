"""
Exam Assistant - Project 2
Author: Nikhil Dodla
Purpose: Read PDF study material notes and generates priotrized exam notes
"""

# Standard libraries
import sys

# Third-Party libraries
import fitz
from dotenv import load_dotenv

load_dotenv()

def extract_text(filepath):
    pdf = fitz.open(filepath)
    text = ""
    for page in pdf:
        text+= page.get_text()
    return text