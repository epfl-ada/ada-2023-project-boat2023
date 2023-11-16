import gdown as gd
import os



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
    
    download_link = f'https://drive.google.com/uc?id={file_id}'
    if not os.path.exists(local_file_name):
        gd.download(download_link, local_file_name, quiet=False)
    else:
        print("file already exists")