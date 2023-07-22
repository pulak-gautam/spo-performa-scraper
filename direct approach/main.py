from source import processFile
from pathlib import Path
from zipfile import ZipFile

zips = {}
path = Path()
filename = "llamasoft-llc_data-science-intern.pdf"
df = processFile(filename=filename)

print(df)
