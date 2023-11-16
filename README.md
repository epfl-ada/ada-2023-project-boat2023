**Impact of terrorism on the movie industry**

# Abstract
Throughout history, humans have used violence and intimidation, especially against civilians, in the pursuit of political and ideological aims. This idea defines terrorism, which has had a significant impact on society and culture. It is fair to assume that cinema portrays diverse cultures, lifestyles and issues, reflecting society, its joys, struggles, and complexities. Through films, we witness stories that resonate with our own experiences, making us feel connected and understood, and allowing us to learn more about what is happening in our world. In this context, terrorism has been portrayed in multiple movies. It is interesting to investigate the impact that terrorism has had on cinema, using the CMU Movie corpus dataset and focusing on emotional depiction, genre association, topic patterns, as well as popularity across continents and countries.

# Research questions
The research questions that we would like to address in our analysis are the following:  

- **Emotional depiction:** How do movies emotionally depict terrorism, and are there identifiable patterns in the portrayal of emotions like fear, anger, empathy, or sadness? Additionally, do the emotional tones in the cinematic representation of terrorism differ between specific countries/regions?
- **Genre association:** Are there specific genres associated to terrorism movies?
- **Topic patterns:** Are there noticeable topic patterns in terrorism movies? Do terrorism movies tend to focus on specific themes? If they do, do different countries or regions portray different themes in their cinematic representation of terrorism?
- **Popularity analysis:** How popular are terrorism-related movies in comparison to others?

# Additional datasets
   [IDMB Movies](https://developer.imdb.com/non-commercial-datasets/) Besides defining a movie's success based on financial criteria, we aim to broaden the definition by incorporating measures of success in terms of ratings. We've acquired two datasets from IMDb: one **title.basic.tsv** facilitates merging with our movie data, and the other **title.ratings.tsv** allows us to extract average ratings.

# Methodology
**Sentiment analysis**
The goal is to extract the general sentiment of movie plots related to terrorism and see whether or not the prevalent sentiments vary from one region or country to another. The sentiment analysis will be conducted on the movies' plots.
To do this, we will use the ***NLTK*** library, specifically ***Vader*** (pre-trained sentiment analyzer) to evalutate emotions in movies. [***VaderSentimentAnalyzer***](https://github.com/cjhutto/vaderSentiment) will be used on each sentence of the plots, which will provide us with a sentiment score (between -1 and 1 where -1 represents the most negative emtion and 1 the most positive) for each movie (positive, neutral or negative). Once these results obtained, we will aggregate the scores by sentiment and by country/Region. Since ***Vader*** only provides general sentiments, we will push our analysis further and include more complex emotions like fear or terror, potentially by using other pre-trained models like [***BERT***](https://huggingface.co/bert-base-uncased). 


**Topic modelling**
The goal is to identify common topics in terrorism-related movies. This can be partly done using ***LDA*** for topic modelling. The first step is to clean the data by tokenizing and stemming it. The second step is to convert the text into a numerical model suitable for modelling and finally we can apply the ***LDA*** algorithm to extract topics. We can identify the recurring themes found in our summary plots and then plot word clouds to visually represent the different themes and gain insight into the different subjects depending on the time period/country/regions.

**Genres analysis**
The genre of a movie is a way to categorize it, allowing audiences and film-makers to understand the type of content they can expect from the movie. In our analysis, we were interested in investigating the potential association between movie genre and terrorism-related movies. In particular, we realize two frequency analyses and one ***chi-squared*** independence test. We first look at how often each genre appears in terrorism vs non-terrorism movies, then the frequency of genres of terrorism-related movies between different countries, and finally we perform a ***chi-squared*** independence test aiming at testing whether there is a significant association between movie genres and their portrayal of terrorism.

**T-Tests**  
In order to determine if there is significant difference between the means (box office revenue mean, average rating mean) of terrorism-related movies and others (non terrorism-related movies), we employ t-tests.   
- **T-test on box office revenue:** The distribution of box office revenue demonstrates a heavy tail. Therefore, we initially apply a log-transformation to the revenue data. Subsequently, we employ t-tests on the transformed data. To calculate statistical power, we conduct 10,000 simulations of the t-tests. Additionally, we employ bootstrap with 10,000 draws to compute the 95% confidence interval
- **T-test on rating:** Similar to the box office analysis, we utilize t-tests for average ratings. However, since the distribution of average ratings does not exhibit a heavy tail, we apply standard rating values without log-transformation.

# Tools and libraries
- 