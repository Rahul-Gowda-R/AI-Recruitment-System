import fitz  # PyMuPDF

def extract_text_from_resume(uploaded_file):
    try:
        text = ""
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        return "Error extracting text: " + str(e)
