import os

def rename_files(loc):
    files = os.listdir(loc)
    for index, file in enumerate(files):
        os.rename(os.path.join(loc, file), os.path.join(loc, ''.join([str(index), '.jpg'])))

if __name__ == "__main__":
    dirloc = "path to the diretory where the image files are stored"
    rename_files(dirloc)