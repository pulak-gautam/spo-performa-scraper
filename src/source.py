import pdfplumber
import pandas as pd

def processFile(filename):
    # filename = "ab-inbev_technology-intern.pdf"
    # Open the file and create a pdf object.
    pdf = pdfplumber.open(filename)

    # Get the number of pages.
    numPages = len(pdf.pages)

    # Iterate over each page and extract the text of each page.
    flag = 0
    text = ""
    for number, pageText in enumerate(pdf.pages):
        if "Program" in pageText.extract_text() or flag == 1:
            text += (pageText.extract_text())
            flag = 1

    lines = text.split('\n')

    flag = 0
    filtered_lines = []
    for line in lines:
        if "Program" in line:
            flag = 1
        if "MSR" in line:
            filtered_lines.append(line)
            break
        if "Eligibilty" in line:
            continue
        if flag == 1:
            filtered_lines.append(line)
        else:
            continue

    return  populateDataFrame(df = formDataFrame(), filtered_lines = filtered_lines)

def formDataFrame():
    df = pd.DataFrame({
    "BT-BS": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "MT": ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "DoubleMajor" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "dual" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "dualB" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "dualC" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Mdes" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "MBA" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Phd" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "Msc" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    "MSR" : ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
    }, index=["AE", "BSBE", "CE", "CHE", "CSE", "EE", "ES", "ME", "MSE", "PHY", "CHM", "MTH", "ECO", "DES", "IME", "HSS"])

    return df


def populateDataFrame(df, filtered_lines):
    col_indices=["BT-BS", "MT", "DoubleMajor", "dual", "dualB", "dualC", "Mdes", "MBA", "Phd", "Msc", "MSR"]
    row_indices=["AE", "BSBE", "CE", "CHE", "CSE", "EE", "ES", "ME", "MSE", "PHY", "CHM", "MTH", "ECO", "DES", "IME", "HSS"]

    index = 0
    for col_index in col_indices: 
        char_idx = len(col_index)
        row_index = 0

        while row_index < len(df.index):
            if filtered_lines[index + 1][char_idx] == " ":
                char_idx +=1
                pass

            elif filtered_lines[index + 1][char_idx] == "Y":
                df[col_index][row_index] = "Yes"
                char_idx += 3
                row_index += 1
                pass

            elif filtered_lines[index + 1][char_idx] == "N":
                df[col_index][row_index] = "No"
                char_idx += 2
                row_index += 1
                pass

            elif filtered_lines[index + 1][char_idx] == "-":
                df[col_index][row_index] = "N/A"
                char_idx += 2
                row_index += 1
                pass
        index += 1

    return df

def populateDictionary(df, dict, filename):
    for index, row in df.iterrows():
        for column_name, cell_value in row.items():
            if(cell_value == "Yes"):
                try:
                    dict[column_name][index].append((filename.replace(".pdf", "")).replace("./", ""))
                except:
                    pass
            # print(f"Cell at row: {index}, column: {column_name} has value: {cell_value}")
    return

def write_to_txt_file(file_path, text_to_write):
    try:
        with open(file_path, 'w') as file:
            file.write(text_to_write)
        print("Text has been written to the file successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")