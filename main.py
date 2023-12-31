# * Imports *
import zstandard as zstd
import glob
import os
import sarc
from msbt import msbt_to_json
import json
from modifyText import modifyText

# * Confirm that the user wants to begin *
def askBegin():
    begin = input('Hi! Have you read the `readme.md` and want begin the modifications? (y/n)')
    
    if (begin == 'y' or begin == 'yes' or begin == 'Yes' or begin == 'YES'):
        print('Ok, let\'s begin!')
    elif (begin == 'n' or begin == 'no' or begin == 'No' or begin == 'NO'):
        exit()
    else:
        print('Please, enter `y` or `n`!')
        askBegin()

askBegin()

# * Decrypt the translation file *
print('Decrypting the translation file...')

# Variables
zstdCompressionLevel = 20
zstdInputFolder = '../original/'
zstdInputFile = glob.glob(zstdInputFolder + '*.zs')[0].split('\\')[-1]
zstdInputPath = zstdInputFolder + zstdInputFile
zstdOutputFolder = '../original/decrypted/'
zstdOutputFile = zstdInputFile.split('.zs')[0]
zstdOutputPath = zstdOutputFolder + zstdOutputFile

# Create the output folder if it doesn't exist
if not os.path.exists(zstdOutputFolder):
    os.makedirs(zstdOutputFolder)

# Decompress the file
with open(zstdInputPath, 'rb') as encryptedFile:
    with open(zstdOutputPath, 'wb') as decryptedFile:
        decompressor = zstd.ZstdDecompressor()
        with decompressor.stream_reader(encryptedFile) as reader:
            while True:
                chunk = reader.read(1024)
                if not chunk:
                    break
                decryptedFile.write(chunk)

print('Done!')

# * Extract the content of the `.sarc` file *
print('Extracting the content of the `.sarc` file...')

# Variables
sarcOutputFolder = '../original/extracted/'

# Create a SARC object
with open(zstdOutputPath, 'rb') as sarcFile:
    sarcObject = sarc.read_file_and_make_sarc(sarcFile)

# Extract to dir
sarcObject.extract_to_dir(sarcOutputFolder)

print('Done!')

# * Convert `.msbt` files to JSON *
print('Converting `.msbt` files to JSON...')

# Variables
jsonOutputFolder = '../original/json/'

# Create the output folder if it doesn't exist
if not os.path.exists(jsonOutputFolder):
    os.makedirs(jsonOutputFolder)

# Convert to JSON
for root, dirs, files in os.walk(sarcOutputFolder):
    for file in files:
        if file.endswith('.msbt'):
            msbtFilePath = os.path.join(root, file)
            
            msbt_to_json(msbtFilePath, jsonOutputFolder)

print('Done!')

# * Modify the JSON files *
print('Modifying the JSON files...')

# Varisbles
modifiedJsonFolder = '../modified/json/'

# Create the output folder if it doesn't exist
if not os.path.exists(modifiedJsonFolder):
    os.makedirs(modifiedJsonFolder)

# Modify the JSON files
for root, dirs, files in os.walk(jsonOutputFolder):
    for file in files:
        if file.endswith('.json'):
            jsonFilePath = os.path.join(root, file)
            
            with open(jsonFilePath, 'r', encoding='utf-8') as jsonFile:
                jsonData = jsonFile.read()
            
            dictData = json.loads(jsonData)

            for key in dictData:
                dictData[key] = modifyText(dictData[key])

            with open(jsonFilePath.replace('original', 'modified', 1), 'w', encoding='utf-8') as modifiedJsonFile:
                json.dump(dictData, modifiedJsonFile, indent=2, ensure_ascii=False)

print('Done!')