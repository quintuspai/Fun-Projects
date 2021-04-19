import os, zipfile
from tkinter import *   
from tkinter import filedialog


def makeZip(path):
    """
        Zips the contents of directories.

                Parameters:
                        path (str) : path to directory to be zipped
                        
                Returns:
                        path (str) : path to the zip file
    """
    backup = zipfile.ZipFile(os.path.join(os.getcwd(),os.path.basename(path)+".zip"),"w")
    for foldername, _ , filenames in os.walk(os.path.basename(path)):
        backup.write(foldername)
        for filename in filenames:
            backup.write(os.path.join(foldername,filename))
    backup.close()
    return "Zip created at {}".format(os.path.join(os.getcwd(),os.path.basename(path)+".zip"))


def browseFiles():
    """
        function for filedialog. 
    """
    global path
    path = filedialog.askdirectory()
    if path:
        print(makeZip(path))
  
top = Tk()
top.geometry("200x100")  
b = Button(top,text = "Browse Files",command = browseFiles)  
b.place(relx=0.5, rely=0.5, anchor=CENTER)  
top.mainloop()