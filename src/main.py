from source import processFile
from source import populateDictionary
from cli import input_cli 
from cli import output_cli 
from pathlib import Path
import os
from rich.console import Console

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

if __name__ == "__main__":
    console = Console()
    folder_path, selected_stream, selected_branch = input_cli(console)

    for filename in os.listdir(path=folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            # print(pdf_path)
            processs_pdf(pdf_path)

    output_cli(dict, selected_stream, selected_branch, console)
# print(dict)
