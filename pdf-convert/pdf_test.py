import pdfplumber as pdpl

pdf_loc = input("Provide the path to the pdf : ")
with pdpl.open(pdf_loc) as pdf:
    for page in pdf.pages:
        print(page.extract_text())

