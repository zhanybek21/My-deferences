import shutil
import os
shutil.copy("test.txt", "test_2.txt")
if os.path.exists("test_2.txt"):
    os.remove("test_2.txt")