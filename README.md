# Deployment of an AI Course Recommender System Using Streamlit

This project implements and deploys several AI course Recommender Systems using [Streamlit](https://streamlit.io/). The final deployment can be seen here:

[https://ai-course-recommender-demo.herokuapp.com/](https://ai-course-recommender-demo.herokuapp.com/)

The application is the final/capstone project of the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning) offered by IBM & Coursera; check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project/06_Capstone_Recommender_System.md) for more information.

All in all, the following models are created:

- Course Similarity
- User Profile
- Clustering
- Clustering with PCA
- KNN
- NMF
- Neural Network
- Regression with Embedding Features
- Classification with Embedding Features

:warning: I used the template provided by IBM as the basis for the web app, but I think it was a poor decision: many equivalent yet different models are created and packed into only two files; thus, it goes against many software design principles, making code understanding and maintainability difficult. I highlight the concrete problems in the section [Next Steps, Improvements](#next-steps-improvements). If I get time, I'll come back and fix them...

Table of contents:
- [Deployment of an AI Course Recommender System Using Streamlit](#deployment-of-an-ai-course-recommender-system-using-streamlit)
  - [Dataset](#dataset)
  - [How to Use This Project](#how-to-use-this-project)
    - [Installing Dependencies for Custom Environments](#installing-dependencies-for-custom-environments)
  - [Background: Content-Based vs. Collaborative-Filtering Recommender Systems](#background-content-based-vs-collaborative-filtering-recommender-systems)
  - [Notes on the Implemented Analysis and Modeling](#notes-on-the-implemented-analysis-and-modeling)
  - [Deployment to Heroku](#deployment-to-heroku)
  - [Results and Conclusions](#results-and-conclusions)
  - [Next Steps, Improvements](#next-steps-improvements)
  - [References and Links](#references-and-links)
  - [Authorship](#authorship)


## Dataset

The dataset is composed of the following files, located in [`data/`](data), and which can be downloaded from the following links:

- [`course_genre.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/course_genre.csv)
- [`ratings.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/ratings.csv)
- [`course_processed.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/course_processed.csv)
- [`user_profile.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/user_profile.csv)
- [`rs_content_test.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/rs_content_test.csv)

The **course catalogue** is contained in [`course_genre.csv`](data/course_genre.csv), which consists of 307 course entries, each with 16 features:

- `COURSE_ID`
- `TITLE`
- 14 (binary) topic or genre fields: `'Database', 'Python', 'CloudComputing', 'DataAnalysis', 'Containers', 'MachineLearning', 'ComputerVision', 'DataScience', 'BigData', 'Chatbot', 'R', 'BackendDev', 'FrontendDev', 'Blockchain'`.

The table [`course_processed.csv`](data/course_processed.csv) complements [`course_genre.csv`](data/course_genre.csv) by adding one new field/column associated with each course: `DESCRIPTION`.

<p style="text-align:center">
  <img src="./assets/word_cloud.png" alt="A wordcloud generated from the course titles." width=1000px>
  <small style="color:grey">A wordcloud generated from the course titles.</small>
</p>

The **ratings table** is contained in [`ratings.csv`](data/ratings.csv), which consists of 233,306 rating entries, each with 3 features:

- `user`: student id
- `item`: course id, equivalent to `COURSE_ID` in `course_genre.csv`
- `rating`: two possible values:
  - `2`: the user just audited the course without completing it.
  - `3`: the user completed the course and earned a certificate.
  - Other possible values, not present in the dataset: `0` or `NA` (no exposure), `1` (student browser course).

The **user profiles** are contained [`user_profile.csv`](data/user_profile.csv), which consists of 33,901 user entries, each with 14 feature weights each. The weights span from 0 to 63, so I understand they are summed/aggregated values for each student, i.e., the accumulated ratings (2 or 3) of the students for each course feature. In other words, these weights seem not to be normalized.

Some **test user rating data** is provided in [`rs_content_test.csv`](data/rs_content_test.csv). In total, the table has 9,402 entries with values 3 values each: `user` (student id), `item` (`COURSE_ID`), `rating`. Altogether 1000 unique users are contained, so some users have rated some courses.

## How to Use This Project

The directory of the project consists of the following files:

:construction: To be done...

```
.
├── .slugignore
├── Procfile
├── README.md                               # This file
├── assets/
├── backend.py
├── conda.yaml                              # Conda environment file
├── data/
├── notebooks                               # Research notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_FE.ipynb
│   ├── 03_Content_RecSys.ipynb
│   ├── 04_Collaborative_RecSys.ipynb
│   ├── 05_Collaborative_RecSys_ANN.ipynb
│   └── README.md                           # Explanations of the notebooks
├── recommender_app.py                      # Streamlit app
├── requirements.txt                        # Dependencies for deployment
└── setup.sh
```

### Installing Dependencies for Custom Environments

If you'd like to work with this repository locally, you need to create a custom environment and install the required dependencies. A quick recipe which sets everything up with [conda](https://docs.conda.io/en/latest/) is the following:

```bash
# Create environment with YAML, incl. packages
conda env create -f conda.yaml
conda activate course-recommender
```

The `requirements.txt` file is for the deployment; if we want to try the app locally on a minimum environment, we could do it as follows:

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run recommender_app.py
```

:construction: To be done...

List of most important dependencies:

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Wordcloud
- Scikit-Learn
- Streamlit

Also, note that **the notebooks can be opened in Google Colab** by clicking on the icon provided in each of them.

## Background: Content-Based vs. Collaborative-Filtering Recommender Systems

[Matrix_Factorization.pdf](./assets/Matrix_Factorization.pdf)

:construction: To be done...

## Notes on the Implemented Analysis and Modeling

:construction: To be done...

## Deployment to Heroku

```bash
heroku logs --tail --app ai-course-recommender-demo
```

## Results and Conclusions

:construction: To be done...

## Next Steps, Improvements

:construction: To be done...

As I mention in the introduction, I used the starter code/template to implement the app, but I think it has many architectural/design issues that need to be tackled. Here, I list some solutions I'd implement if I had time:

- [ ] Create a library/package and move the code from `backend.py` there; thus, `backend.py` would be the interface which calls the machine learning functionalities and `recommender_app.py` the GUI/app definition.
- [ ] Transform code into OOP-style; each model/approach could be a class derived from a base interface and we could pack them in different files which are used in a main library/package file.
- [ ] Fix the fact that datasets are being loaded every time we click on *Train*. This is Ok for a small demo of different machine learning approaches, but not for a final version, closer to a production setting.
- [ ] Unify the pipeline for all models: the approaches based on neural networks have a different data flow, because they need the selected courses in the training set in order to create the embeddings correctly. Additionally, the neural network model cannot be hashed into a dictionary. The data flow and the in/out interfaces should be the same for all models.
- [ ] The ANN training should consider not only the 2 & 3 ratings.
- [ ] Find out a way to deploy the models which use the ANN to Heroku or a similar cloud service. Currently, the ANN model is too large for the Heroku slug memory.

## References and Links

:construction: To be done...

## Authorship

Mikel Sagardia, 2022.  
No guarantees.

If you find this repository useful, you're free to use it, but please link back to the original source.

This is the final capstone project of the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning); check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project) for more information. I used the starter code from IBM.
