import os
import platform
import socket
from pathlib import Path
from utilityProc import utilityProc
from PDWDataProc import PDWDataProc

if __name__ == "__main__":
    utilityProc.logPrint("MAIN -> START")
    PDWDataProcgRun = PDWDataProc() 
    PDWDataProcgRun.readPDWData('CSV',Path(r"C:\Users\admin2\Documents\TestData\pdw.csv"))

# from pathlib import Path
# import pandas as pd

# folder = Path("data")

# for file in sorted(folder.glob("*.csv")):
#    print("reading:", file)

#    df = pd.read_csv(file)