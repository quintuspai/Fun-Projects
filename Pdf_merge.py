# dirloc contains the path to the directory where all the pdfs are kept
# the final pdf will be saved in the same directory

import os
import PyPDF2


def pdf_merge(loc):
    pdfs = [file for file in os.listdir(loc) if file.endswith('.pdf')]
    #pdfs.sort()
    pdf_write = PyPDF2.PdfFileWriter()
    for file in pdfs:
        obj = open(os.path.join(loc, file), 'rb')
        read = PyPDF2.PdfFileReader(obj)
        for page in range(0,read.numPages):
            pgo = read.getPage(page)
            pdf_write.addPage(pgo)
    with open(os.path.join(loc, 'output.pdf'), "wb") as output_file:
        pdf_write.write(output_file)

if __name__ == "__main__":
    dirloc = 'path to the directory where the pdfs are kept'
    pdf_merge(dirloc)