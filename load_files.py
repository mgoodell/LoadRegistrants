from os import path
import pandas as pd
from openpyxl import Workbook


class LoadFiles:
    pass

    # Create File for Storing API Information
    def create_text_file(self, file_reg_path, file_name):
        if path.exists(file_reg_path):
            try:
                file_reg = open(f"{file_reg_path}{file_name}", "x")
            except FileExistsError:
                print("File already exist")
        else:
            print("File directory does not exist")

    def create_excel_file(self, file_reg_path, file_name):
        if path.exists(file_reg_path):
            try:
                file_reg = open(f"{file_reg_path}{file_name}", "x")
            except FileExistsError:
                print("File already exist")
        else:
            print("File directory does not exist")

    # Write registrants to text file
    def write_reg_to_text_file(self, file_reg_path, file_name, result):
        with open(f"{file_reg_path}{file_name}", "w") as convert_file:
            convert_file.write(result)
        print("Dictionary converted into text...")

    # Write registrants to excel file
    def write_reg_to_excel_file(self, file_reg_path, file_name, result):
        wb = Workbook(write_only=True)
        sheet = wb.create_sheet()

        headers = list(result[0])
        sheet.append(headers)

        for x in result:
            sheet.append(list(x.values()))

        wb.save(f"{file_reg_path}{file_name}")
        print("Dictionary converted into excel...")
