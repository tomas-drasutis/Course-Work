import glob, os

path = ""

os.chdir(path)

for file in glob.glob("*.txt"):
    print(file)
    os.remove(file)