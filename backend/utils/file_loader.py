from pypdf import PdfReader
import re

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    text = re.sub(r'\b(\w\s)+\w\b', lambda m: m.group().replace(" ", ""), text)

    return text