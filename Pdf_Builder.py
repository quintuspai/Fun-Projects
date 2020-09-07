# The output.pdf will be stored in the samed directory as that of the images

import os
import img2pdf

def build_pdf(loc):
    with open(os.path.join(loc, 'output.pdf'), 'wb') as f:
        f.write(img2pdf.convert([os.path.join(loc,i) for i in os.listdir(loc) if i.endswith(".jpg")]))
        
if __name__ == "__main__":
    dirloc = "path to the directory where the files are stored"
    build_pdf(dirloc)