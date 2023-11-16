Project ADA

**Why popularity analysis?**
   Analyzing how popular terrorism-related movies are compared to other genres can offer valuable insights into various aspects of the relationship between movies and society. By examining box office trends, we can understand the demand for these films, helping filmmakers and producers make informed decisions about future productions. Additionally, assessing the cultural impact reveals how much interest and engagement the audience has in this genre, providing insights into societal perceptions.
**Methods**

1. **T-Tests**

   1.1 **Box Office:**
   The distribution of box office revenue demonstrates a heavy tail. Therefore, we initially apply a log-transformation to the revenue data. Subsequently, we employ t-tests to assess the potential significant difference between the means of box office revenues (log-means) for terrorism-related movies and non-terrorism-related movies. To calculate statistical power, we conduct 10,000 simulations of the t-tests. Additionally, we employ bootstrap with 10,000 draws to compute the 95% confidence interval.

   1.2 **Average Rating:**
   Similar to the box office analysis, we utilize t-tests for average ratings. However, since the distribution of average ratings does not exhibit a heavy tail, we apply standard rating values without log-transformation.