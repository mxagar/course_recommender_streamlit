# Course Recommender System: Research Notebooks

This folder contains research notebooks related to the [course_recommender_streamlit](https://github.com/mxagar/course_recommender_streamlit):

- [`01_EDA.ipynb`](01_EDA.ipynb): Fist exposure to the dataset and basic Exploratory Data Analysis (EDA).
  - All titles are joined to created a `wordcloud`.
  - Course counts for topics are analyzed: sorted according to counts (popularity of each topic).
  - Users with most enrollments are ranked.
  - Courses with most enrollments are ranked: 20 most popular.
  - A join (`merge()`) is performed to get course names.
- [`02_FE.ipynb`](02_FE.ipynb): Feature Engineering (FE).
  - Course title and description are merged to form a text field from which features are extracted, i.e., token counts (Bags of Words, BoW).
  - Text field tokenization is performed with NLTK, removing stop words and taking only nouns (after POS tagging).
  - A vocabulary/dictionary is created with gensim.
  - BoWs are created for each course text field, storing them stacked in a dataframe in which each course-token pair has an entry.
  - The created dataframe is pivoted to create sparse BoW entries, one for each course.
  - Similarities between courses are computed: given a course with its BoW sparse array, the most similar ones are found.
