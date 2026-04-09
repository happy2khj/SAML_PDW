import struct
import csv
from pathlib import Path
from utilityProc import utilityProc
import torch

class PDWDataProc():
    
    PDW_list: list = []
    PDW_TOA_list: list = []
    PDW_FREQ_list: list = []
    PDW_PW_list: list = []
    PDW_AOA_list: list = []
    PDW_PA_list: list = []
    PDW_SIGTYPE_list: list = []
    PDW_DTOA_list: list = []
    PDW_data_tensor: torch.tensor
    PDW_ParseMOde: str = 'NORMAL' #NORMAL : SAVE PDW_List, ALL : SAVE ALL List
    PDW_TOA_Past: float = 0.0
    PDW_TOA_Now: float = 0.0
    PDW_DTOA: float = 0.0
    PDW_FREQ: float = 0.0
    PDW_PW: float = 0.0
    PDW_AOA: float = 0.0
    PDW_PA: float = 0.0
    PDW_SIGTYPE: float = 0.0

    def __init__(self):
        super().__init__()
        utilityProc.logPrint("featureScaling init")
        self.PDW_list: list = []
        self.PDW_TOA_list: list = []
        self.PDW_FREQ_list: list = []
        self.PDW_PW_list: list = []
        self.PDW_AOA_list: list = []
        self.PDW_PA_list: list = []
        self.PDW_SIGTYPE_list: list = []
        self.PDW_DTOA_list: list = []
        self.PDW_data_tensor = None
        self.PDW_TOA_Past: float = 0.0
        self.PDW_TOA_Now: float = 0.0
        self.PDW_DTOA: float = 0.0
        self.PDW_FREQ: float = 0.0
        self.PDW_PW: float = 0.0
        self.PDW_AOA: float = 0.0
        self.PDW_PA: float = 0.0
        self.PDW_SIGTYPE: float = 0.0

    def CSVFileProc(self, tFilePath : Path)-> int:        
        #with open('example.csv', 'r', encoding='cp949') as file:
        # 파일 객체를 csv.reader의 인자로 전달해 새로운 reader 객체 생성
        #csv_reader = csv.reader(utilityProc.load_file(tFilePath)) 
        csv_reader = csv.DictReader(utilityProc.load_file(tFilePath))

        next(csv_reader) # 첫 행 건너뛰기 
        utilityProc.logPrint("TOA, DTOA, FREQ, PW, AOA, PA, SIGTYPE")
        for row in csv_reader: # 파일 행별로 읽기
            self.TOA_Past = self.PDW_TOA_Now
            self.PDW_TOA_Now = float(row["TOA"]) 
            if(len(self.PDW_list) < 1):
                self.PDW_DTOA = 0.0
            else:                
                self.PDW_DTOA = self.PDW_TOA_Now - self.TOA_Past

            self.PDW_FREQ = float(row["FREQ"])
            self.PDW_PW = float(row["PW"])
            self.PDW_AOA = float(row["AOA"])
            self.PDW_PA = float(row["PA"])
            self.PDW_SIGTYPE = float(row["SIGTYPE"])
            self.PDW_list.append([self.PDW_TOA_Now,self.PDW_DTOA,self.PDW_FREQ,self.PDW_PW,self.PDW_AOA,self.PDW_PA,self.PDW_SIGTYPE])
                
            if(self.PDW_ParseMOde == 'ALL'):
                self.PDW_TOA_list.append(self.PDW_TOA_Now)
                self.PDW_FREQ_list.append(self.PDW_FREQ)
                self.PDW_PW_list.append(self.PDW_PW)
                self.PDW_AOA_list.append(self.PDW_AOA)
                self.PDW_PA_list.append(self.PDW_PA)
                self.PDW_SIGTYPE_list.append(self.PDW_SIGTYPE) 

            utilityProc.logPrint(self.PDW_list[-1])

    def readPDWData(self, ReadMode : str, tFilePath : Path ) -> None:
        #CSV Read
        match ReadMode:
            case 'CSV':
                utilityProc.logPrint("CSV File Proc")
                self.CSVFileProc(tFilePath)
            case 'Binary File':
                utilityProc.logPrint("Binary File Proc")
            case 'Binary Data':
                utilityProc.logPrint("Binary Data Proc")
            case _:  # default 역할
                utilityProc.logPrint("CSV File Proc")
        self.PDW_data_tensor = torch.tensor(self.PDW_list, dtype=torch.float32)
        torch.set_printoptions(threshold=float('inf'),linewidth=200,precision=6,sci_mode=False)
        utilityProc.logPrint(self.PDW_data_tensor)
        utilityProc.logPrint(self.PDW_data_tensor.shape)
        utilityProc.logPrint(self.PDW_data_tensor.dtype)

