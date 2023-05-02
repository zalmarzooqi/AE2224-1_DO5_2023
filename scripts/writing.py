from commonimports import *


# Writing a new Excel file (or wiping before writing) ("write" mode)
def writer_new(path, df, sheet):
    writer = pd.ExcelWriter(path, engine="openpyxl", mode="w")
    df.to_excel(writer, sheet_name=sheet)
    writer.close()


# Writing to an extra sheet in an Excel file ("append" mode)
def writer_add(path, df, sheet):
    writer = pd.ExcelWriter(path, engine="openpyxl", mode="a", if_sheet_exists="replace")
    df.to_excel(writer, sheet_name=sheet)
    writer.close()


# Writing to a csv file ("write" mode)
def csv_writer(path, df, headers):
    df.to_csv(path, index=False, mode="w", header=headers)

