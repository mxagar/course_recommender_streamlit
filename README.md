# Deployment of an AI Course Recommender System Using Streamlit

This project implements and deploys an AI course Recommender System using [Streamlit](https://streamlit.io/).

The deployed application was inspired by the the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning) offered by IBM & Coursera. In the last course/module of the Specialization, Machine Learning Capstone, a similar application is built; check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project/06_Capstone_Recommender_System.md) for more information.

## Dataset

The dataset is composed of two files, located in [`data/`](data), and which can be downloaded from the following links:

- [`course_genre.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/course_genre.csv)
- [`ratings.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-ML321EN-SkillsNetwork/labs/datasets/ratings.csv)

The **course catalogue** is contained in [`course_genre.csv`](data/course_genre.csv), which consists of 307 course entries, each with 16 features:

- `COURSE_ID`
- `TITLE`
- 12 (binary) topic or genre fields: `'Database', 'Python', 'CloudComputing', 'DataAnalysis', 'Containers', 'MachineLearning', 'ComputerVision', 'DataScience', 'BigData', 'Chatbot', 'R', 'BackendDev', 'FrontendDev', 'Blockchain'`.

The **ratings table** is contained in [`ratings.csv`](data/ratings.csv), which consists of 233306 rating entries, each with 3 features:

- `user`: student id
- `item`: course id, equivalent to `COURSE_ID` in `course_genre.csv`
- `rating`: two possible values:
  - `2`: the user just audited the course without completing it.
  - `3`: the user completed the course and earned a certificate.
  - Other possible values, not present in the dataset: `0` or `NA` (no exposure), `1` (student browser course).

<p style="text-align:center">
  <img src="./assets/word_cloud.png" alt="A wordcloud generated from the course titles." width=1000px>
  <small style="color:grey">A wordcloud generated from the course titles.</small>

</p>

## How to Use This Project

The directory of the project consists of the following files:

:construction: To be done...

```
.
├── README.md           # This file
...
```

### Installing Dependencies for Custom Environments

If you'd like to work with this repository locally, you need to create a custom environment and install the required dependencies. A quick recipe which sets everything up with [conda](https://docs.conda.io/en/latest/) is the following:

```bash
# Create environment with YAML, incl. packages
conda env create -f conda.yaml
conda activate course-recommender

# Install pip dependencies
pip install requirements.txt
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

## Notes on Theory

:construction: To be done...

## Notes on the Implemented Analysis and Modeling

:construction: To be done...

### Summary of Contents

:construction: To be done...

- [ ] A
- [ ] B

## Results and Conclusions

:construction: To be done...

## Next Steps, Improvements

:construction: To be done...

## References and Links

:construction: To be done...

## Authorship

Mikel Sagardia, 2022.  
No guarantees.

If you find this repository useful, you're free to use it, but please link back to the original source.

This project was inspired by the the [IBM Machine Learning Professional Certificate](https://www.coursera.org/professional-certificates/ibm-machine-learning) offered by IBM & Coursera. In the last course/module of the Specialization, Machine Learning Capstone, a similar application is built; check my [class notes](https://github.com/mxagar/machine_learning_ibm/tree/main/06_Capstone_Project) for more information.
