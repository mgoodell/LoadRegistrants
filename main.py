import requests
import json
import ast
from LoadRegistrants.load_files import LoadFiles


def main():
    pass


if __name__ == '__main--':
    pass

# Create File for Storing API Information
file_reg_path = "/Users/michaelgoodell/Downloads/"
file_name_text = "regfile.txt"
file_name_excel = "regfile.xlsx"

# API Information
base_url = "https://api.webinar.net/v1"
api_Key = "791e1850-95f0-4514-b243-e17c85e7fb79"
api_secret = "3Aper1XJoVB"
webinar_id = "62d0409e16a10a5408fc1060"

session = requests.Session()
# these are sent along for all requests
session.headers['X-API-KEY'] = api_Key
session.headers['X-API-SECRET'] = api_secret
session.headers['Accept'] = "application/json; charset=UTF-8"

# Get Webinar
get_webinar_url = f"{base_url}/webinars"

# Get Webinar Registrants
get_registrant_url = f"{base_url}/webinars/{webinar_id}/registrants"

response = session.get(get_registrant_url)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
else:
    # Load Dictionary
    data = json.dumps(response.json())

    # Find Total Count
    total_count_length = len(data) - 2
    total_count = data[total_count_length]

    # Format JSON
    data = data.removeprefix('{"registrants": [')
    remove_suffix_text1 = '], "'
    remove_suffix_text2 = f'totalCount": {total_count}'
    remove_suffix_text3 = '}'
    remove_suffix_text4 = remove_suffix_text1 + remove_suffix_text2 + remove_suffix_text3
    data = data.removesuffix(remove_suffix_text4)

    # using ast.literal_eval()
    # convert dictionary string to dictionary
    res_dictionary = ast.literal_eval(data)

    # convert dictionary into string
    # using json.dumps()
    result_string = json.dumps(res_dictionary)

    i = 0
    while i < int(total_count):
        for key, val in res_dictionary[i].items():
            print("{} : {}".format(key, val))
        print("---------")
        i = i + 1

    # Does Registrants Text Exist, If Not, Create It
    text_file = LoadFiles().create_text_file(file_reg_path, file_name_text)
    # Write Registrants to Text File
    write_text_file = LoadFiles().write_reg_to_text_file(file_reg_path, file_name_text, result_string)

    # Does Registrants Text Exist, If Not, Create It
    excel_file = LoadFiles().create_excel_file(file_reg_path, file_name_excel)
    # Write Registrants to Excel File
    write_excel_file = LoadFiles().write_reg_to_excel_file(file_reg_path, file_name_excel, res_dictionary)

