# Cardiovascular Datasets for Disease Prediction

## Table of Contents

1. [Introduction](#introduction)
2. [Available Data Sources](#about-the-data-source)
   - [heart_disease_combined_data](#heart_disease_combined_data)
   - [framingham_lifestyle_dataset](#framingham_lifestyle_dataset)
   - [healthcare_stroke_dataset](#healthcare_stroke_dataset)
3. [Data matrics](#)
   - [Dataset](#dataset)
   - [Computational Resources and Tools Used](#computational-resources-and-tools-used)
   - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Data Transformation for Modeling](#data-transformation-for-modeling)
4. [Classification Modeling](#classification-modeling)

## Introduction

Cardiovascular diseases (CVDs) are the leading cause of death globally, as stated by the World Health Organization (WHO). Early detection and intervention can significantly improve patient outcomes. This project focuses on utilizing machine learning techniques to predict heart disease using publicly available datasets.
https://www.who.int/en/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)
https://www.cdc.gov/heart-disease/data-research/facts-stats/index.html

1. Age alone doesn’t cause coronary artery disease, but the older you get and the longer you’ve been exposed to the effects of risks such as high blood pressure or an unhealthy lifestyle, the greater your overall risk.
2. Blood pressure is the force blood exerts on artery walls. When your reading is consistently above 140/90, you have a condition called hypertension, or high blood pressure. The stress that higher blood pressure places on one’s arteries and heart makes a heart attack or stroke more likely.
3. High blood cholesterol is defined as having too much cholesterol—a waxy, fatty substance—in the blood. Having either high LDL cholesterol (“bad” cholesterol) or low HDL cholesterol (“good” cholesterol)—or both—is one of the best predictors of your risk of heart disease. A blood lipid profile measures both your cholesterol numbers and your triglycerides, another type of fat in the blood that is a risk factor.
4. High blood sugar increases plaque buildup, which causes artery damage that leads to heart disease. Diabetics have double the risk of coronary heart disease. In fact, most people with type 2 diabetes eventually develop heart disease.
5. Smoking, excess weight, and other bad lifestyles

## Available Data Sources

### heart_disease_combined_data

The Cleveland Heart Disease dataset, available in the UCI Machine Learning Repository, was used for this research. The dataset consists of 76 attributes, but we focused on a subset of 13 features used in previous studies. These features include age, sex, chest pain type (cp), resting blood pressure (trestbps), serum cholesterol (chol), fasting blood sugar (fbs), maximum heart rate achieved (thalach), exercise-induced angina (exang), ST depression (oldpeak), slope of the peak exercise (slope), number of major vessels (ca), and types of defect (thal). The target variable, `disease_present`, was mapped to binary values indicating the absence or presence of heart disease.

<li> Description: This dataset combines information from four databases: Cleveland, Hungary, Switzerland, and the VA Long Beach. It contains 76 attributes, but researchers typically use a subset of 14 attributes.</li>
<li> Target Variable: The presence of heart disease, represented as an integer value (0 = no disease, 1-4 = varying degrees of disease severity).</li>
<li> Source: https://archive.ics.uci.edu/dataset/45/heart+disease</li>
<li> Key Notes:
1. Missing values are present.
2. The Cleveland database is the most commonly used subset for machine learning research.
</li>
The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).
The names and social security numbers of the patients were recently removed from the database, replaced with dummy values. One file has been "processed", that one containing the Cleveland database. All four unprocessed files also exist in this directory.

### framingham_lifestyle_dataset

<li> Description: This dataset stems from an ongoing cardiovascular study in Framingham, Massachusetts, aimed at predicting a 10-year risk of coronary heart disease (CHD).</li>
<li> Target Variable: Binary (1 = risk of CHD, 0 = no risk).</li>
<li> Source: Kaggle Dataset
<li> Key Notes:
Contains missing and invalid data.
Features include age, gender, smoking status, blood pressure, cholesterol levels, diabetes, and more.</li>
<li> Source: https://www.kaggle.com/code/captainozlem/framingham-chd-preprossing-data/notebook</li>

The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.

### healthcare_stroke_dataset

<li> Description: This dataset provides information on stroke risk factors and outcomes.</li>
<li> Target Variable: Binary (1 = stroke, 0 = no stroke)..</li>
<i> Source: Kaggle Dataset
<li> Key Notes:
Contains missing and invalid data.
Features include age, gender, smoking status, blood pressure, cholesterol levels, diabetes, and more.</li>
<li> Source: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset</li>

## Dataset Overview

### heart_disease_combined_data

Heart Disease Combined Data Metrics

<table>
  <caption>
    Dataset Columns and Data Types
  </caption>
  <thead>
    <tr>
      <th scope="col">Row</th>
      <th scope="col">Column</th>
      <th scope="col">Description</th>
      <th scope="col">Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>id</td>
      <td>Unique id for each patient</td>
      <td>int64</td>
    </tr>
    <tr>
      <td>1</td>
      <td>age</td>
      <td>Age in years</td>
      <td>int64</td>
    </tr>
    <tr>
      <td>2</td>
      <td>sex</td>
      <td>gender(1 = male; 0 = female)</td>
      <td>binary</td>
    </tr>
    <tr>
      <td>3</td>
      <td>dataset</td>
      <td>Source</td>
      <td>object</td>
    </tr>
    <tr>
      <td>4</td>
      <td>cp</td>
      <td>Chest pain type -> 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic</td>
      <td>object</td>
    </tr>
    <tr>
      <td>5</td>
      <td>trestbps</td>
      <td>Resting blood pressure (in mm Hg on admission to the hospital)</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>6</td>
      <td>chol</td>
      <td>Serum cholesterol in mg/dl</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>7</td>
      <td>fbs</td>
      <td>Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)</td>
      <td>binary</td>
    </tr>
    <tr>
      <td>8</td>
      <td>restecg</td>
      <td>Resting electrocardiographic results -> 0: normal, 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 005 mV), 2: showing probable or definite left ventricular hypertropy by Estes criteria</td>
      <td>object</td>
    </tr>
    <tr>
      <td>9</td>
      <td>thalch</td>
      <td>maximum heart rate achieved in beats per minute (bpm)</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>10</td>
      <td>exang</td>
      <td>Exercise induced angina (1 = yes; 0 = no)</td>
      <td>binary</td>
    </tr>
    <tr>
      <td>11</td>
      <td>oldpeak</td>
      <td>ST depression induced by exercise relative to rest</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>12</td>
      <td>slope</td>
      <td>The slope of the peak exercise ST segment->1: upsloping, 2: flat, 3: down-sloping</td>
      <td>object</td>
    </tr>
    <tr>
      <td>13</td>
      <td>ca</td>
      <td>number of major vessels (0-3) colored by fluoroscopy</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>14</td>
      <td>thal</td>
      <td>3 = normal; 6 = fixed defect; 7 = reversible defect</td>
      <td>object</td>
    </tr>
    <tr>
      <td>15</td>
      <td>num</td>
      <td>Result: The predicted attributeThe predicted attribute</td>
      <td>int64</td>
    </tr>
  </tbody>
</table>
Result Values 1-4: These values represent different degrees of heart disease severity or different types of heart conditions. The exact meaning of each value can vary depending on how the dataset was collected and annotated. However, generally, higher values indicate a higher severity of heart disease or the presence of specific cardiac conditions.
<hr />
<li> RangeIndex: 920 entries, 0 to 919 </li>
<li> Data columns (total 16 columns): 
   14 features excluding unique id and the last column as result </li>
</i> ['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num'] </li>
   dtypes: float64(5), int64(3), object(8)
<li> memory usage: 115.1+ KB </li>

### framingham_lifestyle_dataset

Framingham Dataset Metrics

<table>
  <caption>
    Framingham CHD Data matrics as pandas frame and meaning
  </caption>
  <thead>
    <tr>
      <th scope="col">Category</th>
      <th scope="col">Description</th>
      <th scope="col">Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Male</td>
      <td>Male or female</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Age</td>
      <td>Age of the patient</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Education</td>
      <td>0: Less than High School and High School degrees, 1: College Degree and Higher</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Current Smoker</td>
      <td>Whether or not the patient is a current smoker</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Cigarettes Per Day</td>
      <td>The number of cigarettes that the person smoked on average in one day</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Blood Pressure Medications</td>
      <td>Whether or not the patient was on blood pressure medication</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Prevalent Stroke</td>
      <td>Whether or not the patient had previously had a stroke</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Prevalent Hypertension</td>
      <td>Whether or not the patient was hypertensive</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Diabetes</td>
      <td>Whether or not the patient had diabetes</td>
      <td>Binary</td>
    </tr>
    <tr>
      <td>Total Cholesterol</td>
      <td>Total cholesterol level</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Systolic Blood Pressure</td>
      <td>Systolic blood pressure</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Diastolic Blood Pressure</td>
      <td>Diastolic blood pressure</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Body Mass Index</td>
      <td>Body Mass Index</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Heart Rate</td>
      <td>
        In medical research, variables such as heart rate, though in fact
        discrete, yet are considered continuous because of a large number of
        possible values
      </td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Glucose</td>
      <td>Glucose level</td>
      <td>Continuous</td>
    </tr>
    <tr>
      <td>Ten Year CHD</td>
      <td>"1"-Yes, "0"-No</td>
      <td>Binary</td>
    </tr>
  </tbody>
</table>

<hr />
<li> Range Index: 4133 entries, 0 to 4132 </li>
<li> Data columns (total 16 columns):
['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD'] </li>
<li> 15 features in total, and last column is result </li>
<li> dtypes: float64(8), int64(8)
memory usage: 516.8 KB </li>

![alt text](<images/Framingham preview.png>)

Missing values:
male 0
age 0
education 105
currentSmoker 0
cigsPerDay 29
BPMeds 53
prevalentStroke 0
prevalentHyp 0
diabetes 0
totChol 50
sysBP 0
diaBP 0
BMI 19
heartRate 1
glucose 388
TenYearCHD 0
dtype: int64

### Healthcare Stroke dataset:

## Prerequisites

- Jupyter Notebook with Python-3 kernel, current env -> python version 3.10.16
- Required libraries (e.g. 'numpy', 'pandas', 'scikit-learn', 'seaborn', 'matplotlib', 'xgboost') check package version: conda list numpy
- env name: conda env vscode_env

## Data Preprocssing

## Methodology

### Computational Resources and Tools Used

The project was implemented using Python within a Jupyter Notebook environment, utilizing essential libraries such as Matplotlib, Seaborn, Scikit-learn, NumPy, and Pandas. No extra computational resources were required beyond standard CPU cores.

### Exploratory Data Analysis (EDA)

The project commenced with loading and understanding the dataset. Missing values were handled appropriately, and features were visualized using bar charts, box plots, violin plots, and pair plots to uncover complex patterns and relationships within the data.

### Data Transformation for Modeling

Categorical features were label encoded using Scikit-learn's `LabelEncoder`. Features like 'cp', 'restecg', 'slope', 'thal', 'fbs', and 'exang' were converted into numerical representations, ensuring they were appropriately represented for machine learning models.

## Classification Modeling

For predicting heart disease, three machine learning models were used: Logistic Regression, XGBoost, and Support Vector Machine (SVM). Each model was trained and evaluated on the dataset. The data was split into training and testing sets, with standard scaling applied for uniformity across features.

### XGBoost

XGBoost is a scalable and distributed gradient-boosted decision tree (GBDT) machine learning framework. We used the `XGBClassifier` for binary classification with default parameters and trained it on the heart disease dataset.

### SVM

Support Vector Machine (SVM) is a supervised learning algorithm suitable for classification tasks. The SVM model was trained using an RBF kernel with default parameters.

### Logistic Regression

Logistic Regression is a statistical method used for binary classification problems. The model was trained with default parameters, utilizing predictor variables such as age, cholesterol levels, exercise habits, and chest pain type.

## Results

The models were evaluated using metrics such as accuracy, precision, recall, and F1 score. SVM demonstrated the highest accuracy at 80%, followed by XGBoost at 78%, and Logistic Regression at 77%. SVM's higher recall (83%) suggests its effectiveness in capturing individuals with heart disease. Precision was consistent across models at 84%, resulting in fewer false positives. The F1 score for SVM was 84%, indicating a good balance between capturing disease cases and minimizing false positives.

| Model               | Accuracy | Precision | Recall | F1 Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 77%      | 84%       | 78%    | 81%      |
| XGBoost             | 78%      | 84%       | 78%    | 81%      |
| SVM                 | 80%      | 84%       | 83%    | 84%      |

## Conclusion

Support Vector Machine (SVM) emerged as the most accurate model for detecting heart disease, showcasing superior performance in metrics such as recall and F1 score. While XGBoost and Logistic Regression also demonstrated competitive performance, SVM's precision and recall make it a robust choice for early and accurate heart disease detection. Future work could involve fine-tuning the parameters and exploring other classification techniques to further enhance model performance.

## References

1. Pavlova, A. I. (2023). Application of Machine Learning Algorithms for Heart Disease Prediction. Siberian Journal of Life Sciences and Agriculture, 15(3), 475-496. [DOI](https://doi.org/10.12731/2658-6649-2023-15-3-475-496)
2. Ramakrishnan, S., & Mahesh, B. (2023). Heart Disease Prediction Using Machine Learning. International Journal of Engineering Technology and Management Sciences, 7(6). [DOI](https://doi.org/10.46647/ijetms.2023.v07i06.027)
3. Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J.-J., Sandhu, S., Guppy, K. H., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. The American Journal of Cardiology, 64(5), 304–310. [DOI](<https://doi.org/10.1016/0002-9149(89)90524-9>)
4. Ayatollahi, H., Gholamhosseini, L., & Salehi, M. (2019). Predicting coronary artery disease: A comparison between two data mining algorithms. BMC Public Health, 19(1), 448–448. [DOI](https://doi.org/10.1186/s12889-019-6721-5)
5. Nashif, S., Raihan, M.R., Islam, M.R., & Imam, M.H. (2018). Heart Disease Detection by Using Machine Learning Algorithms and a Real-Time Cardiovascular Health Monitoring System. World Journal of Engineering and Technology, 6, 854-873. [Link](https://www.scirp.org/journal/paperinformation.aspx?paperid=88650)
6. Liu, X., Wang, X., Su, Q., Zhang, M., Zhu, Y., Wang, Q., & Wang, Q. (2017). A Hybrid Classification System for Heart Disease Diagnosis Based on the RFRS Method. Computational and Mathematical Methods in Medicine, 2017, 8272091–11. [DOI](https://doi.org/10.1155/2017/8272091)
