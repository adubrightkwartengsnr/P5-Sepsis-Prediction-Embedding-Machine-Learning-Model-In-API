![Getting Started](Utils/Dashboard.jpeg)
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

**#P5-Sepsis-Prediction: Buiding classification model to predict Sepsis** Sepsis, a life-threatening condition, is a leading cause of mortality in intensive care units. Sepsis is a life-threatening condition caused by the body's response to infection, and early detection is critical for patient survival. By embedding the predictive model in an API, we aim to provide healthcare providers with a powerful tool for real-time sepsis prediction, enhancing decision-making and patient outcomes. While lack of insurance and age differences has been associated with higher in-hospital mortality due to sepsis, the reasons behind this disparity remain unclear. Insurance can facilitate timely access to care, potentially impacting sepsis outcomes and age is a factor that is likely to determine sepsis-related hospitalization.



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
The Telco Churn Classification Project was done following the CRISP-DM process. It also involved a variety of technologies, programming languages, and libraries to process, analyze, and visualize the data. The following tools were utilized:
4. _Python_: Python programming language was the backbone of the project, used for data processing, analysis, and visualization tasks.
5. _Pandas_ and NumPy: Pandas and NumPy libraries were essential for data manipulation and numerical computations.
6. _Matplotlib and Seaborn_: Matplotlib and Seaborn were employed for data visualization, creating insightful charts and graphs to represent the findings.
7. _Visual Studio Code and Jupyter Notebooks_: Jupyter Notebooks within the Visual Studio IDE provided an interactive environment for running code, visualizing data, and documenting the analysis process.
8. _Scikit-learn_: Scikit-learn's library SimpleImputer was utilized for imputing null values in the amount column.
9. _Streamlit_: Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.
10. _FastAPI_: is a web framework first released in 2018 for building HTTP-based service APIs in Python. It is used for building APIs with Python 3.8+ based on standard Python-type hints. FastAPI is based on Pydantic and uses type hints to validate, serialize and deserialize data.
11. _Docker_: Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.
12. _Optuna_: Optuna is an automatic hyperparameter optimization software framework, particularly designed for machine learning.
12. _GitHub_: GitHub served as the version control system for the project, enabling collaboration and tracking changes in the codebase.
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
1. Tailor Pricing Strategies: The analysis reveals a correlation between higher monthly charges and increased customer churn. To bolster retention, Vodafone could explore tailored pricing strategies that balance revenue generation with customer satisfaction and perceived value.
2. Enhance Early Customer Experience: Elevated churn rates during the initial months emphasize the importance of prioritizing early customer experience. By focusing on seamless onboarding processes, service quality, and swift issue resolution, Vodafone can enhance satisfaction and foster loyalty during this critical phase.
3. Promote Long-Term Contracts: Higher churn rates among customers on month-to-month contracts call for attention. Encouraging the adoption of longer-term contracts through incentives and benefits could cultivate commitment and diminish churn.
4. Leverage Additional Services: Services like Online Security and Backup have a notable impact on churn rates. Strengthening these offerings to address customer needs can aid in retention by delivering value-added solutions.
5. Monitor Fiber Optic Offering: Given its high charges and churn rate, meticulous attention to the Fiber Optic service is crucial. Continuously refining and supporting this service will ensure that premium costs align with customer expectations.
6. Personalized Customer Engagement: Utilize insights from churn analysis to craft personalized engagement strategies. Tailored communication, targeted offers, and customized marketing campaigns based on factors such as tenure, contract type, and preferences can enhance loyalty and mitigate churn.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

![image](Utils\Dashboard.jpeg)




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
  git clone https://github.com/adubrightkwartengsnr/LP2-Customer-Churn-Prediction
```

Change into the cloned repository

```sh
  cd Indian_Startup_Ecosystem_Analysis_2018-2021
  
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


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Bright Adu Kwarteng Snr**

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

I would like to express my sincere gratitude to my instructors Racheal Appiah-Kubi and Violette Naa Adoley Allotey for their exceptional guidance, unwavering support, and invaluable mentorship throughout the course of this project. Their expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data analysis.

I would also like to extend a special thank you to Solomon Nyamson for his valuable advice and insights shared during the development of this project. His experiences and expertise in similar projects have been a source of inspiration and guidance, enriching our project with practical knowledge.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p> align="right">(<a href="https://medium.com/@adubrightkwarrteng11/customer-churn-prediction-a-machine-learning-learning-approach-d75d3ef90391">Link to Article</a>)</p>



