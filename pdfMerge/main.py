import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()
directory = '/Users/kashyapkanumuri/Downloads/PDFs'

for file in os.listdir(directory):
    if file.endswith(".pdf"):
        merger.append(f'{directory}/{file}')
merger.write(f"{directory}/mergedDocument.pdf")