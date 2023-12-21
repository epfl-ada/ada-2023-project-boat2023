import gdown as gd
import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px


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

# Sentiment analysis: classifying into 3 classes (positive, negative, neutral)
def classify(score: float):
    #positive
    if score >= 0.05:
        return 1
    #negative
    elif score <= -0.05:
        return -1
    #neutral
    return 0

# given a list of sentences, the function returns the result of the analyzer
def analyse_text(text, classify_discrete = True): 
    # Initialize the analyzer
    analyzer = SentimentIntensityAnalyzer()
    res = []
    for sentence in text:
        sentiment_result = analyzer.polarity_scores(sentence)
        if classify_discrete:
            res.append(classify(sentiment_result['compound']))
        else:
            res.append(sentiment_result['compound'])
    
    return res

def plot_interactive_pie(df, column, title, n, color_palette):
    counts = df[column].value_counts()
    # Keep the top n and sum the rest under "Others"
    top_counts = counts[:n]
    top_counts['Others'] = counts[n:].sum()
    fig = px.pie(values=top_counts, names=top_counts.index, title=title, 
                 color_discrete_sequence=color_palette)
    fig.update_traces(textinfo='percent+label')
    fig.show()
    

def has_keyword(summary, keywords):
    for word in keywords:
        if word in summary.lower():  # Perform a case-insensitive check
            return True
    return False

#Define a function that checks whether a list of countries contains at least one of the 10 countries we are interested in
def contains_countries_of_interest(lst):
    # List of countries of interest
    countries_of_interest = [
        "United States of America", "United Kingdom", "India", "Japan",
        "France", "Germany", "Canada", "Italy", "Hong Kong", "Australia"]
    return any(country in countries_of_interest for country in lst)

#Define a function that checks whether a list of genres contains at least one of the 10 genres we are interested in
def contains_genres_of_interest(lst):
    # List of countries of interest
    genres_of_interest = ['Drama', 'Action', 'Thriller', 'Comedy', 'Action/Adventure', 'Horror',
                          'Adventure', 'World cinema', 'Crime Fiction', 'Science Fiction']
    return any(genre in genres_of_interest for genre in lst)