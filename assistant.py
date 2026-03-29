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


def build_prompt(text):
    instructions = """you are an exam preparation assistant for a university student. 
    Analyze the provided study material and respond in this exact structure:
1. OVERVIEW
provide a brief summary of the PDF. list each main topic and subtopic with one line of explanation each.

2. CATEGORIZED TOPICS
Divide all the topics into two categories:
- Real World Value: concepts useful for projects, internships, and career development
- Exam Only: concepts relevant purely for scoring marks in semester exams
- If a topic belongs to both, mention them and prioritize explaining them first

3. NOTES
Provide concise notes proportional to the content.
One file worth of content should produce notes that cover that file only - not more.
prioritize depth over quantity.
If multiple files cover similar or overlapping topics, do not repeat - merge and present once only.

4. EXAM PATTERN ANALYSIS(only if exam papers are provided)
If previous semester papers and class test papers are included, identify which topics appear most frequently'
and highlight them as high priority for exam preparation.

Study Material:
"""
    full_text = instructions + text
    return full_text