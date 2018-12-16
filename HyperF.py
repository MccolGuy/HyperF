import shutil
import os
import glob
from tkinter import filedialog
import tkinter as tk
root = tk.Tk()
root.withdraw()
def fileorganizer():
    os.chdir(file_path)
    file_list = glob.glob("*.*")
    for i in file_list:
        fname,extwithdot = os.path.splitext(i)
        ext = extwithdot[1:]
        file_list = glob.glob(file_path + "/*%s"%i)
        if os.path.isdir(file_path + "/%s"%ext +"파일"):
            for i in file_list:
                shutil.move(i, file_path + "/%s"%ext+ "파일")
        else:
            os.mkdir(file_path + "/%s"%ext + "파일")
            for i in file_list:
                shutil.move(i, file_path + "/%s"%ext +"파일")
file_path = filedialog.askdirectory()
print(file_path)
if file_path:
    fileorganizer()
else:
    print("프로그램을 종료합니다")
