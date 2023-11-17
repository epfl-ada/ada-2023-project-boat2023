import gdown as gd
import os
import json


def download_data(file_id, local_file_name):
    """
    Download a file from Google Drive using its file ID.

    Parameters:
    - file_id (str): The Google Drive file ID.
    - local_file_name (str): The local file name to save the downloaded file.

    Returns:
    - None

    Note:
    - This function checks if the file already exists locally before attempting to download.

    """

    download_link = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(local_file_name):
        gd.download(download_link, local_file_name, quiet=False)
    else:
        print("file already exists")


# def extract_year(date_string):
#     """
#     Extract the year from a date

#     Parameters:
#     - date string

#     Returns:
#     - year string
#     """
#     return date_string.split("-")[0] if "-" in date_string else date_string


def is_empty_json(json_str):
    try:
        json_obj = json.loads(json_str)
        return isinstance(json_obj, dict) and not bool(json_obj)
    except (json.JSONDecodeError, TypeError):
        return False


def extract_countries(json_str):
    countries = set()
    try:
        json_obj = json.loads(json_str)
        for country in json_obj.values():
            countries.add(country)
    except (json.JSONDecodeError, TypeError):
        pass
    return countries


def extract_countries_from_dictionary(json_string):
    try:
        countries_dict = json.loads(json_string)
        # Extract country names from the values in the dictionary
        country_names = [value for value in countries_dict.values()]
        return country_names
    except (json.JSONDecodeError, KeyError):
        return []
