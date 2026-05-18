import pdfplumber
from docx import Document


# =====================================================
# PDF EXTRACTION
# =====================================================

def extract_pdf_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text += page.extract_text()

    return text


# =====================================================
# DOCX EXTRACTION
# =====================================================

def extract_docx_text(docx_path):

    doc = Document(docx_path)

    text = "\n".join(

        [para.text for para in doc.paragraphs]
    )

    return text