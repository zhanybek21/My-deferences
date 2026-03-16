import shutil
import os

os.makedirs("1folder", exist_ok=True)
os.makedirs("2folder", exist_ok=True)


with open("1folder/simple.txt", "w") as f:
    f.write("This is a test file")


shutil.copy("1folder/simple.txt", "2folder/simple.txt")



shutil.move("2folder/simple.txt", "2folder/moved_simple.txt")