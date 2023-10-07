import os
import struct
import json

class Msbt2Json:
    def __init__(self):
        self.buff = None
        self.isLE = False
        self.offset = 0
        self.labelList = []
        self.messageList = []

    def convert(self, msbtFileName, jsonOut):
        with open(msbtFileName, 'rb') as file:
            self.buff = file.read()

            # check MSBT magic.
            msbtMagic = self.buff[0:8].decode()
            if msbtMagic != 'MsgStdBn':
                raise Exception('Invalid MSBT Header.')

            # endian.
            self.isLE = self.buff[0x08] == 0xff

            # number of blocks.
            blockNum = self.readUInt16(0x0e)

            # current offset.
            self.offset = 0x20

            for _ in range(blockNum):
                blockType = self.buff[self.offset:self.offset + 4].decode()
                blockSize = self.readUInt32(self.offset + 0x04)

                self.offset += 0x10

                if blockType == 'LBL1':
                    self.parseLabelBlock()
                elif blockType == 'TXT2':
                    self.parseTextBlock(blockSize)

                self.offset += ((blockSize + 0xf) // 0x10) * 0x10

            if self.labelList and self.messageList:
                # create json.
                json_dict = {}
                for label, message in zip(self.labelList, self.messageList):
                    json_dict[label] = message

                # output json.
                outDir = jsonOut
                baseName = os.path.basename(msbtFileName)
                baseName = os.path.splitext(baseName)[0]
                outPath = os.path.join(outDir, baseName + '.json')

                with open(outPath, 'w', encoding='utf-8') as json_file:
                    json.dump(json_dict, json_file, indent=2, ensure_ascii=False)

                return outPath

    def parseLabelBlock(self):
        tableCount = self.readUInt32(self.offset)
        self.labelList = []
        tableOffset = self.offset + 0x04

        for _ in range(tableCount):
            labelCount = self.readUInt32(tableOffset)
            labelOffset = self.offset + self.readUInt32(tableOffset + 0x04)

            for _ in range(labelCount):
                labelLen = self.buff[labelOffset]
                start = labelOffset + 0x01
                end = start + labelLen
                label = self.buff[start:end].decode()
                labelIndex = self.readUInt32(end)
                self.labelList.insert(labelIndex, label)
                labelOffset += 0x01 + labelLen + 0x04

            tableOffset += 0x08

    def parseTextBlock(self, blockSize):
        messageCount = self.readUInt32(self.offset)
        self.messageList = []
        tableOffset = self.offset + 0x04

        for _ in range(messageCount):
            messageOffset = self.offset + self.readUInt32(tableOffset)
            end = -1

            if _ + 1 < messageCount:
                end = self.offset + self.readUInt32(tableOffset + 0x04) - 2
            else:
                end = self.offset + blockSize - 2

            message = self.buff[messageOffset:end].decode('utf-16-le')
            self.messageList.append(message)
            tableOffset += 0x04

    def readUInt16(self, offset):
        if self.isLE:
            return struct.unpack('<H', self.buff[offset:offset + 2])[0]
        else:
            return struct.unpack('>H', self.buff[offset:offset + 2])[0]

    def readUInt32(self, offset):
        if self.isLE:
            return struct.unpack('<I', self.buff[offset:offset + 4])[0]
        else:
            return struct.unpack('>I', self.buff[offset:offset + 4])[0]

def msbt_to_json(msbtFileName, jsonOut):
    return Msbt2Json().convert(msbtFileName, jsonOut)

# Usage example, MSBT two JSON:
# result = msbt_to_json('./battleHill.msbt', ./json/)
# print('JSON file converted:', result)