from source import processFile
from source import populateDictionary
from pathlib import Path
import os

dict = {
    "BT-BS"       : {"AE": [], "BSBE": [], "CE": [], "CHE": [], "CSE": [], "EE": [], "ES": [],  "ME": [], "PHY": [], "CHM": [], "MTH": [], "ECO": []},
    "MT"          : {"AE": [], "BSBE": [], "CE": [], "CHE": [], "CSE": [], "EE": [], "ES": [],  "ME": [], "IME": []},
    "DoubleMajor" : {"AE": [], "BSBE": [], "CE": [], "CHE": [], "CSE": [], "EE": [], "ES": [],  "ME": [], "PHY": [], "CHM": [], "MTH": [], "ECO": []},
    "dual"        : {"AE": [], "BSBE": [], "CE": [], "CHE": [], "CSE": [], "EE": [], "ES": [],  "ME": [], "PHY": [], "CHM": [], "MTH": [], "ECO": []},
    "dualB"       : {"AE": [], "BSBE": [], "CE": [], "CHE": [],  "ME": [], "PHY": [], "CHM": [], "MTH": [], "ECO": [], "IME": []},
    "dualC"       : {"IME": []},
    "Mdes"        : {"DES": []},
    "MBA"         : {"IME": []},
    "Phd"         : {"AE": [], "BSBE": [], "CE": [], "CHE": [], "CSE": [], "EE": [], "ES": [],  "ME": [], "PHY": [], "CHM": [], "MTH": [], "ECO": [], "HSS": []},
    "Msc"         : {"PHY": [], "CHM": [], "MTH": [], "ECO": []}
    }


def processs_pdf(filename):
    path = Path()
    # filename = "llamasoft-llc_data-science-intern.pdf"
    df = processFile(filename=filename)
    populateDictionary(df, dict, filename)
    # print(df)

folder_path = "./"
for filename in os.listdir(path=folder_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        # print(pdf_path)
        processs_pdf(pdf_path)

# print(dict)