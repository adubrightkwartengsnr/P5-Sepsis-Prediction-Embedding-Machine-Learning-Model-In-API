<a name="readme-top"></a>

<div align="center">
  <h1><b>P5-Sepsis-Prediction-Embedding-Machine-Learning-Model-In-API</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Project Description ](#Sepsi-Insights)
  - [🛠 Built with ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Insights ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [👥 Authors ](#-authors-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Sepsis Prediction <a name="about-project"></a>

**P5-Sepsis-Prediction: Buiding classification model to predict Sepsis** Sepsis, a life-threatening condition, is a leading cause of mortality in intensive care units. Sepsis is a life-threatening condition caused by the body's response to infection, and early detection is critical for patient survival. By embedding the predictive model in an API, we aim to provide healthcare providers with a powerful tool for real-time sepsis prediction, enhancing decision-making and patient outcomes. While lack of insurance and age differences has been associated with higher in-hospital mortality due to sepsis, the reasons behind this disparity remain unclear. Insurance can facilitate timely access to care, potentially impacting sepsis outcomes and age is a factor that is likely to determine sepsis-related hospitalization.



1. **ID**: Unique Identifier of patient
2. **PRG(Plasma Glucose)**: Measurement of plasma glucose levels. 
3. **PL(Blood Work Result 1)**: Blood work result in mu U/ml. 
4. **PR(Blood Pressure)**: Measurement of blood pressure in mm Hg.
5. **SK(Blood Work Result 2)**: Blood work result in mm. 
6. **TS(Blood Work Result 3)**: Blood work result in mu U/ml.
7. **M11(Body Mass Index)**: BMI calculated as weight in kg/(height in m)^2
8. **BD2(Blood Work Result 4)**: Blood work result in mu U/ml
9. **Age**: Age of the patient in years. 
10. **Insurance**: Indicates whether the patient holds a valid insurance card.
11. **Sepsis**: Target variable indicating whether the patient will develop sepsis (Positive) or (Negative)


## 🛠 Built With <a name="Technologies Used"></a>
The P5-Sepsis-Prediction Project was done following the CRISP-DM process. It also involved a variety of technologies, programming languages, and libraries to process, analyze, and visualize the data. The following tools were utilized:
1. _Python_: Python programming language was the backbone of the project, used for data processing, analysis, and visualization tasks.

2. _Pandas_ and NumPy: Pandas and NumPy libraries were essential for data manipulation and numerical computations.

3. _Matplotlib and Seaborn_: Matplotlib and Seaborn were employed for data visualization, creating insightful charts and graphs to represent the findings.

4. _Visual Studio Code and Jupyter Notebooks_: Jupyter Notebooks within the Visual Studio IDE provided an interactive environment for running code, visualizing data, and documenting the analysis process.

5. _Scikit-learn_: Scikit-learn's library SimpleImputer was utilized for imputing null values in the amount column.

6. _Streamlit_: Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.

7. _FastAPI_: is a web framework first released in 2018 for building HTTP-based service APIs in Python. It is used for building APIs with Python 3.8+ based on standard Python-type hints. FastAPI is based on Pydantic and uses type hints to validate, serialize and deserialize data.

8. _Docker_: Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.

9. _Optuna_: Optuna is an automatic hyperparameter optimization software framework, particularly designed for machine learning.

10. _GitHub_: GitHub served as the version control system for the project, enabling collaboration and tracking changes in the codebase.
    These technologies played a crucial role in the successful implementation of the project, providing the necessary tools to analyze and derive insights from the Indian Startup Ecosystem funding datasets.

<details>
  <summary>Data Sources</summary>
  <p>The dataset provided for this project is a modified version of a publicly available data source from Johns Hopkins University from Kaggle. It includes various patient attributes and their corresponding sepsis status. The dataset is subject to strict usage restrictions and can only be used for the purpose of this assignment. The data directory consists of both the training and testing data.</p>
</details>


<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Success Criteria <a name="key-features"></a>
- Accuracy: The model's should obtain an accuracy of 75% or higher.
- Precision and Recall:The final model should maintain both Precision and Recall scores of 0.75 or above.
- F1 Score: The final model should attain an F1 score of 0.75 to 0.85 or higher according to state-of-the-art SOTA models
Area Under the Receiver Operating Characteristic Curve (AUC-ROC): According to the state-of-the-art SOTA models for sepsis prediction should achieve AUC-ROC scores in the range of 0.80 to 0.90 or higher.

## Key Insights <a name="key-Insights"></a>
The distilled recommendations are as follows:
1. The datasets should be increased further to enable the machine learning models to learn from the data
2. _Analysis of Age Distribution and Sepsis Risk_
    - The average age of all patients in the dataset is approximately 33.29 years.
    - For patients diagnosed with sepsis, the median age is around 34 years.
    - In contrast, patients without sepsis have a median age of about 25 years.
  From these observations, we can infer that older patients are more likely to develop sepsis compared to younger patients. The higher median age for those with sepsis suggests that as age increases, so does the risk of contracting sepsis. This insight highlights the importance of considering age as a significant factor in the risk assessment for sepsis.
3. _Analysis of BMI and Sepsis Risk_:From the my analysis, we can observe that the risk of developing sepsis varies across different BMI categories. Patients categorized as Overweight and Obese have a higher likelihood of developing sepsis compared to those who fall into the Underweight and Normal BMI categories. This insight highlights the importance of considering BMI as a risk factor in the risk assessment for sepsis, as well as the fact that patients with high BMI levels are more likely to develop sepsis. Additionally, the distribution of patients across different BMI categories is not uniform, which may affect the overall accuracy of our risk assessment.

4. _Analysis of Blood Pressure and Sepsis Risk_: From the visualization above, it is evident that all patients in the sepsis dataset fall between the normal pressure levels. This suggests that higher blood pressure is not a major factor in determining the risk of developing sepsis.
Recommendations for Detecting Sepsis: Comprehensive Health Monitoring: Since blood pressure alone is not a significant indicator of sepsis risk, it is crucial to monitor a combination of vital signs and biomarkers, including heart rate, temperature, respiratory rate, and blood tests.

5. _Analysis of Plasma Glucose Levels and Sepsis Risk_: From the exploratory data analysis, it is evident that the median plasma glucose levels of patients with sepsis are higher compared to those without sepsis. Specifically:
- The median plasma glucose level for patients with sepsis is approximately 3.5 mmol/L.
- For patients without sepsis, the median plasma glucose level is around 1.5 mmol/L.
This significant difference indicates that elevated plasma glucose levels are associated with a higher risk of developing sepsis. Given the observed correlation, plasma glucose levels should be included as a key feature in the model.

6._Analysis of Insurance Coverage and Sepsis Risk_:In this analysis, '0' signifies patients without health insurance coverage, and '1' represents patients with insurance coverage.Among the patients without insurance (0), 57 have sepsis, while a larger group, consisting of 131 patients, does not have sepsis. Conversely, among the patients with insurance coverage (1), 151 have sepsis, whereas a higher number of 260 patients are sepsis-free.
This breakdown highlights a notable trend: regardless of insurance status, a larger proportion of patients are tagged as sepsis-negative. This indicates that while insurance coverage is an important factor in healthcare, it does not significantly alter the proportion of sepsis diagnoses in this dataset.


 
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/adubrightkwartengsnr/P5-Sepsis-Prediction-Embedding-Machine-Learning-Model-In-API
```

Change into the cloned repository

```sh
  cd P5-Sepsis-Prediction-Embedding-Machine-Learning-Model-In-API
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```

## Running The Docker Images from Dockerhub

To run the Docker images on your local machine, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python installed on your machine

### Steps

1. **Install Docker**

   If you haven't already installed Docker, you can download and install it from the [official Docker website](https://www.docker.com/get-started). Follow the installation instructions specific to your operating system.

2. **Pull the Docker Images**

   Open your terminal or command prompt and pull the required Docker images from Dockerhub using the following commands:

   ``` sh
   docker pull brightadu/sepsis-predict-api:v1.0
   docker pull brightadu/sepsis-predict-client:v1.0
   ```

  ``` sh
   docker run -d --name mycontainer -p 8000:8000 brightadu/sepsis-predict-api:v1.0
   docker run -d --name mycontainer -p 8000:8000 brightadu/sepsis-predict-client:v1.0
   ```


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Bright Kwarteng Senior Adu**

- GitHub: [GitHub Profile](https://github.com/adubrightkwartengsnr)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/bright-adu-kwarteng-snr)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to express my sincere gratitude to my instructors Racheal Appiah-Kubi and Glen Anum for their exceptional guidance, unwavering support, and invaluable mentorship throughout the course of this project. Their expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data analysis.

I would also like to extend a special thank you to Solomon Nyamson for his valuable advice and insights shared during the development of this project. His experiences and expertise in similar projects have been a source of inspiration and guidance, enriching our project with practical knowledge.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p> align="right">(<a href="https://medium.com/@adubrightkwarrteng11/sepsis-prediction-with-fastapi-streamlit-and-docker-a-complete-guide-3ba952d5fd32">Link to Article</a>)</p>



