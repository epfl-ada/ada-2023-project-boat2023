---
layout: page
title: Explosive Narratives - Terrorism through the Cinematic Lens
subtitle: Investigating the impact of Terrorism on World Cinema
cover-img: /assets/img/main_img.jpg
thumbnail-img: /assets/img/main_img.jpg
share-img: /assets/img/main_img.jpg
use-site-title: true
---

Throughout history, humans have used violence and intimidation, especially against civilians, in the pursuit of political and ideological aims. This idea defines terrorism, which has had a significant impact on society and culture. It is fair to assume that cinema portrays diverse cultures, lifestyles and issues, reflecting society, its joys, struggles, and complexities. Through films, we witness stories that resonate with our own experiences, making us feel connected and understood, and allowing us to learn more about what is happening in our world. In this context, terrorism has been portrayed in multiple movies. It is interesting to investigate the impact that terrorism has had on cinema, using the CMU Movie corpus dataset and focusing on emotional depiction, genre association, topic patterns, as well as popularity across continents and countries.

## Introduction
Welcome to "Explosive Narratives: Terrorism through the Cinematic Lens" – where we light the fuse on the dynamite topic of terrorism in movies, without any real explosions, of course! Picture this: you're sitting in your comfy chair, popcorn in hand, ready to dive deep into the world of cinema where the only thing more thrilling than a car chase is our data-driven analysis. 
So, grab your 3D glasses, because we're about to embark on a cinematic journey that's part data, part drama, and totally explosive – metaphorically speaking, of course! 🍿🎬💥

Let's start by visualizing the counts of terrorism-related movies through time:

![My Image](/assets/img/terrorism_movies_time_series.png)

We can observe a growing trend in the production of terrorism-related movies over the years. This could suggest a growing interest in terrorism movies in cinema, but it could however be related to the smaller number of movies provided by the CMU dataset in the 1907-1940s period. There is a dramatic increase in the early 21st century period, where the bars reach their highest points. This could be reflective of global events and the increased prevalence of terrorism in news media, telling us about the role of terrorism in the public consciousness during these times, which may have influence the film industry.

![My Image](/assets/img/terrorism_movies_countries.png)
**figure out how to insert interactive plots**

As we can see, the US, followed by India, United Kingdom and Japan, are the most important countries when it comes to producing terrorism-related movies. This plot is of course a little biased, since the Hollywood and Bollywood are the most important movie production industries in the world, and they by nature produce more movies than other countries.

![My Image](/assets/img/terrorism_movies_per_country.png)

This plot offers a sight into how many terrorism-related movies were produced in each country.

-----------------
## 1. Popularity Analysis - The Box Office Boom
##### Are terrorism-themed movies the box office's best friend or its awkward acquaintance? 

-----------------
## 2. Genre Association - The Movie Genre Cocktail

Think of genre as secret agents; they've got all the gear - narrative elements, thematic content, stylistic approach, and the emotional response they aime to evoke in the audience. They help categorize films so that you don't end up in a rom-com when you were ready for a story high in suspense and plot twists about a hero saving thousands of people from the action of terrorists.

And when it comes to terrorism movies, they sneak up on you with action, disguise themselves in drama, and occasionally, they even wear the mask of comedy before the big kaboom! Our mission is to dissect the relationship between genres and terrorism movies.

So buckle up data nerds, as we dive bomb into the world of movie genres. It's going to be a blast! (pun intented) 🎥💣🔍

### 2.1 How often does each genre appear in terrorism vs non-terrorism movies?
For both non-terrorism- and terrorism-related movies, we have gathered the top 10 most common genres. We then plot the counts of both types of movies against the genres. We obtain the figure below.

![My Image](/assets/img/top_10_genres.png)

What are the most prevalent genres of non-terrorism vs terrorism movies? Do they differ? 
We see that:
- The top 10 most common genres of terrorism movies are: Drama, Action, Thriller, Comedy, Action/Adventure, Horror, Adventure, World cinema, Crime fiction and Science fiction.
- The top 10 most common genres of non-terrorism movies are: Drama, Comedy, Romance Film, Black-and-white, Short film, Thriller, Action, Indie, World cinema and Crime ficiton.
- We notice that for both sets of movies, the most prevalent genre is Drama. This could suggest that dramatic elements are central to storytelling in films regardless of the terrorism theme. 

Now, for a more significant comparison, we will focus on the top 10 most common genres in terrorism movies, and we will look at the proprtion of non-terrorism and terrorism movies for these genres.

![My Image](/assets/img/proportion_genres.png)

1) What genres are more prevalent in terrorism related movies than in non-terrorism related movies?
- Action and Thriller: These genres seem to be more prevalent in terrorism-related movies when compared to non-terrorism-related movies. 
- Adventure and Horror: While not as dominant as Drama, Action, or Thriller, these genres also appear more frequently in terrorism-related movies than in non-terrorism-related ones.
- Drama: This genre has a very high proportion in both terrorism and non-terrorism related movies.

2) How do these genre preferences for terrorism movies reflect cultural attitudes towards terrorism? Do they suggest that certain genres are better suited to explore terrorism-related themes?
- Action and Thriller: These genres are traditionally associated with high energy, suspense, and conflict, which are common elements in terrorism narratives. The prevalence of Action and Thriller genres in terrorism-related movies could reflect the intensity and high stakes often associated with terrorism. 
- Adventure and Horror: These genres could be more prevalent due to the way they can incorporate elements of the unknown and fear, which can reflect unpredictability and fear associated with acts of terrorism.
- Drama: While Drama is prevalent in both types of movies, its slightly reduced prevalence in terrorism-related movies compared to non-terrorism-related ones might indicate that while dramatic storytelling is universal, terrorism movies might need the inclusion of action or thriller elements to better portray the specific themes associated to terrorism.

3) Do these genre trends in terrorism-related movies reflect a global influence, or are they more indicative of Western cinematic trends?
We discuss this in **section 2.2**.

4) Evolution Over Time: How have the representations of terrorism in various genres evolved over time? We discuss this in **section 2.3**.

### 2.2 Does the prevalence of certain genres of terrorism-related movies change between world regions? And between countries?
Let's visualize the heatmap of Movie Genres by Region, by Country, and a bar chart for the counts of movies per genre in the USA.

![My Image](/assets/img/heatmaps_genres.png)

The prevalence of genres like Drama and Thriller in many regions might indicate a universal appeal of intense narratives that deal with complex human emotions and ethical dilemmas, which are often at the core of terrorism-related stories. In contrast, regions where certain genres are more popular may reflect regional storytelling traditions or preferences, such as a penchant for Action/Adventure in the Americas, which could be tied to the Hollywood influence and its history of high-stakes blockbusters.

Economic factors, including the availability of funding and resources, market size, and audience demographics, can significantly influence which genres are produced within a region. For instance, regions where Action/Adventure and Thriller genres are highly prevalent may have more established film industries capable of supporting the high production costs associated with these genres. They may also have larger audiences that provide the box office revenues needed to justify such investments.

The representation of certain genres, such as Action/Adventure and Drama, across multiple regions suggests that these genres have broad international appeal, likely influenced by the widespread distribution of Hollywood films. However, the presence of genres like World Cinema, which is more prevalent in Europe, indicates that unique cultural differences and cinematic expressions still persist despite the forces of globalization.

### 2.3 Were some genres of terrorism movies more popular during specific periods?
Here, we plot the evolution of counts of movies through time, for each genre. 

![My Image](/assets/img/genre_time_series.png)

By comparing these plots to the "Number of Terrorism-Related Movies per Year" in section **Introduction**, the number of terrorism-related movies for each genre follows the same general trend as for all terrorism-related movies together. Indeed, we see a net increase of movies over time for all genres. We notice that some genres are more prevalent than others (Drama, Thriller, Action/Adventure, Horror and World cinema). 
We notice that World cinema has had a peak in the 1990s decade. This could be due to many factors: the global political climate, with the end of the cold war, dissolution of the Soviet Union, the end of apartheid in South Africa, etc, which may have encouraged filmmakers to explore the theme of terrorism through movies; this could also be due to the rise of independent and international cinema in the 1990s (**reference**: https://nofilmschool.com/independent-movies-90s-dominate).  The 1990s saw a surge in independent filmmaking, with more films being produced outside the traditional Hollywood system. 
Thriller, Action and Horror share a similar peak, roughly from 2005 to 2015. Drama knows a very important peak in the late 2010s.

To conclude, the representation of terrorism in various genres have the same overall evolution over time, with an increase in the number of terrorism-movies of all genres. Some genres stand out with specific peaks, notably World cinema in the 1990s.

### Conclusion:
And that's a wrap on our Genre Analysis!

So, what have we learned? When it comes to terrorism movies, Drama is the most prevalent movie genre, in both terrorism- and non-terrorism-relatd movies. It seems that whether our protagonists are diffusing a bomb or a dramatic love triangle, we just can't get enough of those emotional rollercoasters. 

But when the smoke clears, it's Action and Thriller that really stand out. These genres are to terrorism movies what a fuse is to dynamite – absolutely essential for a spectacular show.
Adventure and Horror genres are the next most prevalent genres of terrorism movies. They serve up a blend of chills and thrills, often leaving us with the kind of cliffhangers that make you wish you had a parachute. 

Globally speaking, it looks like genres representing terrorism movies are not very diverse between world regions and conutries. Drama and Thriller seem to be the universal language of 'boom'. However, we do notice some regional preferences for Action/Adventure or World Cinema. 

As for the evolution of terror in films throughout time, all genres have the same trend. They are all characterized by an increase in movie counts, and some genres stand out with important peaks, such as World cinema in the 1990s, Horror, Action and Thriller in the 2000-2010s, and Drama in the 2010s. 
Whatever the genre, it seems like audiences are always ready for narrative detonation.

Now, grab your popcorn and your protective gear; we're moving on to the next explosive analysis before the timer runs out! 🍿💥🎥

-----------------
## 3. Topic Patterns
##### Last but not least, we delve into the thematic jungle of terrorism movies. Are we spotting patterns, or is it as unpredictable as a plot twist in a Hitchcock film?

-----------------
## 4. Emotional Depiction - The Tearjerker ot the Fist-Pumper?
##### Here, we unpack the emotional suitcase of terrorism in films. Do these movies make you grab a tissue, or are they more likely to have you cheering from your seat? And let's not forget the regional flavors – is a terrorism movie in Hollywood spicier than its Bollywood counterpart?