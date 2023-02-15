# Deployment of an AI Course Recommender System Using Streamlit

This project implements and deploys several AI course Recommender Systems using [Streamlit](https://streamlit.io/). The final deployment can be seen here:

[https://ai-course-recommender-demo.herokuapp.com/](https://ai-course-recommender-demo.herokuapp.com/)

The application is the final/capstone project of the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning) offered by IBM & Coursera; check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project/06_Capstone_Recommender_System.md) for more information.

All in all, the following models are created:

- **Course Similarity Model**
- **User Profile Model**
- **Clustering Model**
- **Clustering with PCA**
- **KNN Model with Course Ratings**
- **NMF Model**
- **Neural Network (NN)**
- **Regression with NN Embedding Features**
- **Classification with NN Embedding Features**

:warning: :construction: *I used the [template provided by IBM](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/module_5/app.zip) as the basis for the web app, but I think it was a poor decision: many equivalent yet different models are created and packed into only two files; thus, it goes against many software design principles, making code understanding and maintainability difficult. I highlight the concrete problems in the section [Next Steps, Improvements](#next-steps-improvements). If I get time, I'll come back and fix them...*

Table of contents:
- [Deployment of an AI Course Recommender System Using Streamlit](#deployment-of-an-ai-course-recommender-system-using-streamlit)
  - [How to Use This Project](#how-to-use-this-project)
    - [Installing Dependencies for Custom Environments and Running the App Locally](#installing-dependencies-for-custom-environments-and-running-the-app-locally)
  - [The Dataset](#the-dataset)
  - [Notes on Recommender Systems](#notes-on-recommender-systems)
    - [Content-Based Systems](#content-based-systems)
      - [Course Similarity Model](#course-similarity-model)
      - [User Profile Model](#user-profile-model)
      - [Clustering Model with/without PCA](#clustering-model-withwithout-pca)
    - [Collaborative Filtering](#collaborative-filtering)
      - [KNN Model with Course Ratings](#knn-model-with-course-ratings)
      - [NMF Model](#nmf-model)
      - [Artificial Neural Network (ANN) and Derived Models](#artificial-neural-network-ann-and-derived-models)
  - [Notes on the App Structure](#notes-on-the-app-structure)
  - [Notes on the Deployment to Heroku](#notes-on-the-deployment-to-heroku)
  - [Preliminary Results](#preliminary-results)
  - [Next Steps, Improvements](#next-steps-improvements)
  - [References and Links](#references-and-links)
  - [Authorship](#authorship)

## How to Use This Project

The directory of the project consists of the following files:

```
.
├── .slugignore                             # Files to ignore in the Heroku deployment
├── Procfile                                # Heroku deployment: container/service command
├── README.md                               # This file
├── assets/                                 # Images and additional material
├── backend.py                              # Model implementations
├── conda.yaml                              # Conda environment file
├── data/                                   # Dataset files
├── notebooks                               # Research notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_FE.ipynb
│   ├── 03_Content_RecSys.ipynb
│   ├── 04_Collaborative_RecSys.ipynb
│   ├── 05_Collaborative_RecSys_ANN.ipynb
│   └── README.md                           # Explanations of the notebooks
├── recommender_app.py                      # Streamlit app, UI
├── requirements.txt                        # Dependencies for deployment
├── runtime.txt                             # Python version for the Heroku deployment
└── setup.sh                                # Setup file for Streamlit, executed in Procfile
└── tests                                   # Tests for the app; TBD
```

The model implementation is two places:

- In the [notebooks](notebooks), where research and manual tests are carried out.
- In the files [`backend.py`](backend.py) and [`recommender_app.pys`](recommender_app.py), where the code from the notebooks has been refactored to fit a Streamlit app. The functionality (i.e., models, etc.) is in the first, whereas the UI is defined in the second.

There are at least 3 ways you can explore the project:

1. Check the [app deployed on Heroku](https://ai-course-recommender-demo.herokuapp.com/). The URL might need a bit of time until the app awakens; additionally, note that the ANN-based models are disabled on the deployed app because the network exceeds the memory capacity of the eco dyno.
2. Run the app locally. To that end, you need to install the `requirements.txt` and run `streamlit`, as explained in the [next subsection](#installing-dependencies-for-custom-environments-and-running-the-app-locally).
3. Check the [notebooks](notebooks); they contain all model definitions and tests and a summary of their contents is provided in [`notebooks/README.md`](notebooks/README.md). The `conda.yaml` file contains all packages necessary to set up an environment, as explained in the [next subsection](#installing-dependencies-for-custom-environments-and-running-the-app-locally). Alternatively, you can open the notebooks on **Google Colab** by clicking on the dedicated icon in the header of each of them.

### Installing Dependencies for Custom Environments and Running the App Locally

If you'd like to work with this repository locally, you need to create a custom environment and install the required dependencies. A quick recipe which sets everything up with [conda](https://docs.conda.io/en/latest/) is the following:

```bash
# Create environment with YAML, incl. packages
conda env create -f conda.yaml
conda activate course-recommender
```

If you have a Mac with an M1/2 chip and you are having issues with the Tensorflow package, please check [this link](https://towardsdatascience.com/installing-tensorflow-on-the-m1-mac-410bb36b776).

The `requirements.txt` file is for the deployment; if we want to try the app locally on a minimum environment, we could do it as follows:

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run recommender_app.py
```

Also, as mentioned, note that **the notebooks can be opened in Google Colab** by clicking on the icon provided in each of them.

## The Dataset

The dataset used in the project is composed of the following files, located in [`data/`](data), and which can be downloaded from the following links:

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

Clearly, the datasets `ratings.csv` and `course_genre.csv` are the most important ones; with them, we can

- build user profiles,
- compute user and course similarities,
- infer latent user and course features,
- build recommender models, both content-based and with collaborative filtering.

## Notes on Recommender Systems

Altogether, eight recommender systems have been created and deployed; these can be classified in two groups:

  - Content-based: systems in which user and course features (i.e., genres/topics) are known and used.
  - Collaborative Filtering: systems in which user and course features (i.e., genres/topics) are not known, or they are inferred.

In the following, a few notes are provided on the implemented models.

### Content-Based Systems

#### Course Similarity Model

Course similarities are built from course text descriptions using Bags-of-Words (BoW). A similarity value is the projection of a course descriptor vector in the form of a BoW on another, i.e., the cosine similarity between both. Given the selected courses, the set of courses with the highest similarity value are found.

#### User Profile Model

Courses have a genre descriptor vector which encodes all the topics covered by them. User profiles can be built by summing the user course descriptors scaled by the ratings given by the user. Then, for a target user profile, the unselected courses that are most aligned with it can be found using the cosine similarity (i.e., dot product) between the profile and the courses. Finally, the courses with the highest scores are provided.

#### Clustering Model with/without PCA

Courses have a genre descriptor vector which encodes all the topics covered by them. User profiles can be built by summing the user course descriptors scaled by the ratings given by the users. Then, those users can be clustered according to their profile. This approach provides with the courses most popular within the user cluster.

Additionally, user profile descriptors can be transformed to their principal components, taking only a subset of them, enough to cover a percentage of the total variance, selected by the user.

### Collaborative Filtering

#### KNN Model with Course Ratings

Given the ratings dataframe, course columns are treated as course descriptors, i.e., each course is defined by all the ratings provided by the users. With that, a course similarity matrix is built using the cosine similarity. Then, for the set of selected courses, the most similar ones are suggested.

#### NMF Model

Non-Negative Matrix Factorization is performed: given the ratings dataset which contains the rating of each user for each course (sparse notation), the matrix is factorized as the multiplication of two lower rank matrices. That lower rank is the size of a latent space which represents discovered inherent features (e.g., genres). With the factorization, the ratings of unselected courses are predicted by multiplying the lower rank matrices, which yields the approximate but complete user-course rating table. For more information, check [my handwritten explanation on the topic](./assets/Matrix_Factorization.pdf).

#### Artificial Neural Network (ANN) and Derived Models

An Artificial Neural Network (ANN) which maps users and courses to ratings is defined and trained. If the user is in the training set, the ratings for unselected courses can be predicted. However, the most interesting part of this approach consists in extracting the user and course embeddings from the ANN for later use. An embedding vector is a continuous N-dimensional representation of a discrete object (e.g., a user).

The user and item embeddings extracted from the ANN are used to build a linear regression model and a random forest classifier which predict the rating given the embedding of a user and a course.

## Notes on the App Structure

As mentioned, the app is fully contained in these two files:

- [`backend.py`](backend.py): model definition, training and prediction functions.
- [`recommender_app.py`](recommender_app.py): Streamlit UI and usage of `backend.py` functionalities.

The [`recommender_app.py`](recommender_app.py) file instantiates all UI widgets in sequence and it converges to two important functions: `train)()` and `predict()`. These call their homologue in [`backend.py`](backend.py), which bifurcate the execution depending on the selected model (a parameter caught by the UI). All main and auxiliary functions to train the models and produce results are contained in [`backend.py`](backend.py).

I took this structure definition from the [IBM template](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/module_5/app.zip), however, it has some shortcomings; in summary, the architecture from `backend.py` is fine for a demo consisting of one/two simple models, but very messy for nine. Some improvements are listed in the section [Next Steps, Improvements](#next-steps-improvements). 

## Notes on the Deployment to Heroku

[Heroku](https://www.heroku.com/home) is a cloud service which enables very easy (continuous) deployments. In this case, we need to create the following files in the repository:

- `Procfile`
- `.slugignore`
- `runtime.txt`
- `requirements.txt`
- `setup.sh`

Additionally, an app needs to be created in Heroku, via the [CLI](https://devcenter.heroku.com/articles/heroku-cli) or the Heroku web interface. In the case of the web interface, the deployment is realized by simply linking the Github repository to the app. More information on that can be found [here](https://github.com/mxagar/mlops_udacity/blob/main/03_Deployment/MLOpsND_Deployment.md#44-continuous-deployment-with-heroku).

After the deployment, if anything goes wrong, we can check the logs with the CLI as follows:

```bash
# Replace app-name, e.g., with ai-course-recommender-demo
heroku logs --tail --app app-name
```

Continuous Integration and Continuous Deployment (CI/CD) are realized as follows:

- There is a Github action defined in [`.github/workflows/python-app.yml`](.github/workflows/python-app.yml) which runs the tests and is triggered every time we perform a push to the remote repository.
- The option *Continuous deployment* is active in the Heroku app (web interface), so that the code is deployed every time Github runs all tests successfully.

:warning: :construction: The current tests are very few and non-significant; the testing structure was created and now it needs to be populated.

## Preliminary Results

- Content-based systems work efficiently and provide similar results, but they require (manual) genre characterization for users and courses/items.
- Collaborative Filtering systems are based on the assumption that there is a relationship between users and items, so that we can discover the latent features that reveal user preferences.
- The collaborative system which seems to best predict the ratings is the random forest classifier that maps user and course embeddings (from the ANN) to rating classes (2 or 3). However:

  - The training time is the longest.
  - The new users for whom we want to predict (and their example ratings) must be trained with the system so that they have an embedding representation.

## Next Steps, Improvements

As I mention in the introduction, I used the starter code/template to implement the app, but I think it has many architectural/design issues that need to be tackled. Here, I list some solutions I'd implement if I had time:

- [ ] Create a library/package and move the code from `backend.py` there; thus, `backend.py` would be the interface which calls the machine learning functionalities and `recommender_app.py` the GUI/app definition.
- [ ] Transform code into OOP-style; each model/approach could be a class derived from a base interface and we could pack them in different files which are used in a main library/package file.
- [ ] Fix the fact that datasets are being loaded every time we click on *Train*. This is Ok for a small demo of different machine learning approaches, but not for a final version, closer to a production setting.
- [ ] Unify the pipeline for all models: the approaches based on neural networks have a different data flow, because they need the selected courses in the training set in order to create the embeddings correctly. Additionally, the neural network model cannot be hashed into a dictionary. The data flow and the in/out interfaces should be the same for all models.
- [ ] The ANN training should consider not only the 2 & 3 ratings.
- [ ] Find out a way to deploy the models which use the ANN to Heroku or a similar cloud service. Currently, the ANN model is too large for the Heroku slug memory.
- [ ] Implement more tests to cover at least the major functionalities and the `train()` and `predict()` functions in the `backend.py`.

## References and Links

- My guide on how to use Streamlit: [streamlit_guide](https://github.com/mxagar/streamlit_guide)
- My notes on deployments in general (e.g., to Heroku, AWS, Render): [mlops_udacity/deployment](https://github.com/mxagar/mlops_udacity/blob/main/03_Deployment/MLOpsND_Deployment.md)
- My notes on the IBM Machine Learning Specialization: [machine_learning_ibm](https://github.com/mxagar/machine_learning_ibm)
- My notes on the lectures by Andrew Ng about Recommender Systems: [machine_learning_coursera](https://github.com/mxagar/machine_learning_coursera/blob/main/07_Anomaly_Recommender/ML_Anomaly_Recommender.md#machine-learning-anomaly-detection-and-recommender-systems)
- My blog post on how to reach production-level code: [From Jupyter Notebooks to Production-Level Code](https://mikelsagardia.io/blog/machine-learning-production-level.html)

## Authorship

Mikel Sagardia, 2022.  
No guarantees.

If you find this repository useful, you're free to use it, but please link back to the original source.

This is the final capstone project of the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning); check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project) for more information. I used the starter code from IBM.
