import glob, os
import csv

def getSubfolderPaths(path):
    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]

    return list_subfolders_with_paths

def extractFileContent(file):
    with open(file, 'r', encoding='utf-8') as textFile:
        data = textFile.read().replace('\n', '')

    return data

def anlyzeFileContent(data, fileName, valuesDict):
    print("Analyzing " + fileName)
    dataArray = data.split()

    for word in dataArray:
        if word in valuesDict:
            valuesDict[word].append(fileName)
        else:
            valuesDict[word] = [fileName]



basePath= ""
basePathSubFolders = getSubfolderPaths(basePath)

valuesDict = {}

for path in basePathSubFolders:
    subFolderPaths = getSubfolderPaths(path)
    
    for subPath in subFolderPaths:
        os.chdir(subPath)
        for file in glob.glob("*.txt"):
            fileContent = extractFileContent(file)
            anlyzeFileContent(fileContent, file, valuesDict)

os.chdir("")
with open('output.csv', 'w+', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in valuesDict.items():
        print(key)
        writer.writerow([len(value), key, value])

