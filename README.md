# Language Models and Linguistic Typology

## Data

[data/](data)
- [delta_df.csv](data/delta_df.csv): The raw amount of improvement for each language and task  
- [feature_values.csv](data/feature_values.csv): The selected features include feature group, name, and language values  
- [metrics_df.csv](data/metrics_df.csv): The accuracy scores for each intermediate checkpoint on each task  
- [fit_data.csv](data/fit_data.csv): The estimated best-fit curve points for each task and language  
- [p90_df.csv](data/p90_df.csv): The estimated point where the model reaches 90 percent of overall performance improvements.  
- [popt.json](data/popt.json): The parameters for the best-fit curve  

## Structure

In some of the directories, there is a helper notebook for debugging and testing visualizations.

- [index.qmd](index.qmd) Where the abstract will be

1. [Introduction](1-introduction)
2. [Related Work](2-related_work)
3. [Models and Data](3-models_data)
4. [Methods](4-methods)
5. [Results](5-results)
6. [Discussion](6-discussion)
7. [Conclusion](7-conclusion)

- [Appendix](appendix) Not all of this will be submitted in the paper, but this is where I am dumping visualizations and other tables for ease. 
