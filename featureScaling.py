import struct
import csv
from pathlib import Path
from utilityProc import utilityProc
import torch

class featureScaling():
    
    PDW_TOA_list: list = []
    PDW_FREQ_list: list = []
    PDW_PW_list: list = []
    PDW_AOA_list: list = []
    PDW_PA_list: list = []
    PDW_SIGTYPE_list: list = []
    PDW_DTOA_list: list = []
    PDW_data_tensor: torch.tensor

    def __init__(self):
        super().__init__()
        utilityProc.logPrint("featureScaling init")
        self.PDW_TOA_list: list = []
        self.PDW_FREQ_list: list = []
        self.PDW_PW_list: list = []
        self.PDW_AOA_list: list = []
        self.PDW_PA_list: list = []
        self.PDW_SIGTYPE_list: list = []
        self.PDW_DTOA_list: list = []
        self.PDW_data_tensor = None

    def CSVFileProc(self, tFilePath : Path)-> int:        
        #with open('example.csv', 'r', encoding='cp949') as file:
        # 파일 객체를 csv.reader의 인자로 전달해 새로운 reader 객체 생성
        #csv_reader = csv.reader(utilityProc.load_file(tFilePath)) 
        csv_reader = csv.DictReader(utilityProc.load_file(tFilePath))

        next(csv_reader) # 첫 행 건너뛰기 
        utilityProc.logPrint("TOA, DTOA, FREQ, PW, AOA, PA, SIGTYPE")
        for row in csv_reader: # 파일 행별로 읽기
            self.PDW_TOA_list.append(int(row["TOA"]))
            self.PDW_FREQ_list.append(int(row["FREQ"]))
            self.PDW_PW_list.append(int(row["PW"]))
            self.PDW_AOA_list.append(int(row["AOA"]))
            self.PDW_PA_list.append(int(row["PA"]))
            self.PDW_SIGTYPE_list.append(int(row["SIGTYPE"]))
            if(len(self.PDW_TOA_list) <= 1):
                self.PDW_DTOA_list.append(0)
            else:
                self.PDW_DTOA_list.append(self.PDW_TOA_list[-1] - self.PDW_TOA_list[-2])

            utilityProc.logPrint(str(self.PDW_TOA_list[-1]) +", "+ str(self.PDW_DTOA_list[-1]) +", "+ str(self.PDW_FREQ_list[-1])
                                 +", "+ str(self.PDW_PW_list[-1]) +", "+ str(self.PDW_AOA_list[-1]) +", "+ str(self.PDW_PA_list[-1])
                                 +", "+ str(self.PDW_SIGTYPE_list[-1]))

    def readPDWData(self, ReadMode : int, tFilePath : Path ) -> None:
        #CSV Read
        match ReadMode:
            case 1:
                utilityProc.logPrint("CSV File Proc")
                self.CSVFileProc(tFilePath)
            case 2:
                utilityProc.logPrint("Binary File Proc")
            case 3:
                utilityProc.logPrint("Binary Data Proc")
            case _:  # default 역할
                utilityProc.logPrint("CSV File Proc")



