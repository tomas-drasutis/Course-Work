import glob, os
import csv

def extractFileContent(file):
    with open(file, 'r', encoding='utf-8') as textFile:
        data = textFile.read().replace('\n', '')
        data = data.replace('\t', ' ')
        data = data.replace('\x1f', '')
        data = data.replace('\x1f', '')
        dataArray = data.split()

        for word in dataArray:
            if(word.startswith('_')):
                data = data.replace(word, '')


    dataArray = data.split()
    if(len(dataArray) == 1):
        return None

    return data

def writeToCsv(fileName, filesize, transcript):
    with open(r'dev.csv', 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([fileName, filesize, transcript.lower()])
        #f.write(transcript.lower() + '\n')

path = ""
shortPath = ""

#30
skipableTrain = [
'Z052Ml_066_03.wav', 'Z079Mm_066_03.wav', 'Z132Ml_021_2.wav', 'Z132Ml_021_3.wav', 'Z132Ml_022_1.wav', 'Z132Ml_023_1.wav', 'Z132Ml_023_2.wav', 'Z132Ml_024_1.wav', 'Z240Mn_023.wav',
'Z288Mm_025_05_T.wav', 'Z288Mm_026_04.wav', 'Z288Mm_027_01.wav', 'Z288Mm_027_04.wav', 'Z288Mm_028_02.wav', 'Z288Mm_029_03.wav', 'Z288Mm_032_02.wav', 'Z288Mm_032_04.wav', 'Z288Mm_065_05.wav',
'Z289Vl_025_04.wav', 'Z289Vl_028_01.wav', 'Z289Vl_029_01.wav', 'Z289Vl_029_03.wav', 'Z289Vl_029_04.wav', 'Z289Vl_030_01.wav', 'Z289Vl_030_04.wav', 'Z289Vl_031_04.wav', 'Z289Vl_032_01.wav',
'Z289Vl_032_03.wav', 'Z289Vl_032_06.wav', 'Z289Vl_066_03_T.wav'
]

#21
skipableTest = [
'Z011Vf_060_16.wav', 'Z011Vf_060_17.wav', 'Z011Vf_060_18.wav', 'Z011Vf_060_19.wav', 'Z012Mf_060_13.wav', 'Z012Mf_060_16.wav', 'Z012Mf_060_17.wav', 'Z012Mf_060_18.wav', 'Z012Mf_060_19.wav', 
'Z013Mf_060_13.wav', 'Z013Mf_060_16.wav', 'Z013Mf_060_17.wav', 'Z013Mf_060_18.wav', 'Z013Mf_060_19.wav', 'Z052Ml_065_05_T.wav', 'Z054Vm_030_01.wav', 'Z079Mm_028_05_T.wav', 'Z079Mm_065_05_T.wav',
'Z132Ml_022_2.wav', 'Z132Ml_024_2.wav', 'Z134Mk_024a.wav'
]

#66
skipableDev = [
'Z003Mi_020_07.wav', 'Z003Mi_020_08.wav', 'Z003Mi_020_24.wav', 'Z003Mi_060_13.wav', 'Z003Mi_060_16.wav', 'Z003Mi_060_17.wav', 'Z003Mi_060_18.wav', 'Z003Mi_060_19.wav', 'Z004Vg_020_07.wav',
'Z004Vg_020_08.wav', 'Z004Vg_020_24.wav', 'Z004Vg_060_13.wav', 'Z004Vg_060_16.wav', 'Z004Vg_060_17.wav', 'Z004Vg_060_18.wav', 'Z004Vg_060_19.wav', 'Z005Mf_020_07.wav', 'Z005Mf_020_08.wav',
'Z005Mf_020_24.wav', 'Z005Mf_060_13.wav', 'Z005Mf_060_16.wav', 'Z005Mf_060_17.wav', 'Z005Mf_060_18.wav', 'Z005Mf_060_19.wav', 'Z006Mg_020_07.wav', 'Z006Mg_020_08.wav', 'Z006Mg_020_24.wav',
'Z006Mg_060_13.wav', 'Z006Mg_060_16.wav', 'Z006Mg_060_17.wav', 'Z006Mg_060_18.wav', 'Z006Mg_060_19.wav', 'Z007Mg_020_07.wav', 'Z007Mg_020_08.wav', 'Z007Mg_020_24.wav', 'Z007Mg_060_13.wav',
'Z007Mg_060_16.wav', 'Z007Mg_060_17.wav', 'Z007Mg_060_18.wav', 'Z007Mg_060_19.wav', 'Z008Mh_020_07.wav', 'Z008Mh_020_08.wav', 'Z008Mh_020_24.wav', 'Z008Mh_060_13.wav', 'Z008Mh_060_16.wav',
'Z008Mh_060_17.wav', 'Z008Mh_060_18.wav', 'Z008Mh_060_19.wav', 'Z009Mh_020_07.wav', 'Z009Mh_020_08.wav', 'Z009Mh_020_24.wav', 'Z009Mh_060_13.wav', 'Z009Mh_060_16.wav', 'Z009Mh_060_17.wav', 
'Z009Mh_060_18.wav', 'Z009Mh_060_19.wav', 'Z010Mi_020_07.wav', 'Z010Mi_020_08.wav', 'Z010Mi_020_24.wav', 'Z010Mi_060_13.wav', 'Z010Mi_060_16.wav', 'Z010Mi_060_17.wav', 'Z010Mi_060_18.wav',
'Z010Mi_060_19.wav', 'Z011Vf_020_07.wav', 'Z011Vf_020_08.wav', 'Z011Vf_020_24.wav', 'Z011Vf_060_13.wav', 'Z012Mf_020_07.wav', 'Z012Mf_020_08.wav', 'Z012Mf_020_24.wav', 'Z013Mf_020_07.wav',
'Z013Mf_020_08.wav', 'Z013Mf_020_24.wav'
]

os.chdir(path)
for file in glob.glob("*.txt"):
    if(file == "vocabulary.txt"):
        continue

    wavName = file[:-3] + "wav"
    print(wavName)

    if(wavName in skipableDev):
        print("SKIP")
        continue

    wavSize = os.path.getsize(wavName)
    cleanData = extractFileContent(file)

    if(cleanData is None):
        print("SKIP")
        continue

    writeToCsv(wavName, wavSize, cleanData)


