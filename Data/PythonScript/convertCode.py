
#pip install tabula-py
import tabula

def convert_pdf_to_csv(file, name):
    tabula.convert_into(file + name,  file + "\\dt.csv", pages=1)

