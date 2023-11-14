**Impact of terrorism on the movie industry**

# Abstract
Throughout history, humans have used violence and intimidation, especially against civilians, in the pursuit of political and ideological aims. This idea defines terrorism, which has had a significant impact on society and culture. It is fair to assume that cinema portrays diverse cultures, lifestyles and issues, reflecting society, its joys, struggles, and complexities. Through films, we witness stories that resonate with our own experiences, making us feel connected and understood, and allowing us to learn more about what is happening in our world. In this context, terrorism has been portrayed in multiple movies. It is interesting to investigate the impact that terrorism has had on cinema, using the CMU Movie corpus dataset and focusing on emotional depiction, genre association, topic patterns, as well as popularity across continents and countries.

# Research questions
The research questions we would like to answer in our analysis are the following:
**1) Emotional depiction:** How do movies emotionally depict terrorism, and are there identifiable patterns in the portrayal of emotions like fear, anger, empathy, or sadness? Additionally, do the emotional tones in the cinematic representation of terrorism differ between specific countries/regions?
**2) Genre association:** Are there specific genres associated to terrorism movies?
**3) Topic patterns:** Are there noticeable topics patterns in terrorism movies? If so, do different countries/regions differ in the specific topics/patterns of their cinematic representation of terrorism?
**4) Popularity analysis:** How popular are terrorism-related movies in comparison to others?

# Additional datasets

# Methodology
**Data wrangling and prepocessing**
Preporcessing text:
    Tokenization: nltk.tokenize.word_tokenize() to split raw text into individual words.
    Stop words: nltk.corpus.stopwords() to remove words such as "and", "the", "of", "it" since they are unlikely to convey any kind of emotion and could cause noise. NLTK provides a built-in list of stop words, which we will use to filter out these words from the movie plots.
    Stemming and lemmatization: nltk.stem.WordNetLemmatizer() to reduce words to their root forms.

**Sentiment analysis**
The goal is to extract the general sentiment of movie plots related to terrorism and see whether or not the prevalent sentiments vary from one region or country to another. the sentiment analysis will be conducted on the plots as well as on the reviews extracted from the IMDb dataset.
To do this, we will use the NLTK library, specifically Vader (pre-trained sentiment analyzer) to evalutate emotions in movies. VaderSentimentAnalyzer will be used on each sentence, which will provide us with a sentiment score for each movie (positive, neutral or negative). Once these results obtained, we will aggregate the scores by sentiment and by country/Region.


**Topic modelling**
The goal is to identify common topics in movies related to terrorism. To do this, we will use algorithms such as Latent Dirichlet Allocation (LDA) 

# Tools and libraries
- 