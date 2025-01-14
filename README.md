# Heart Disease Detection Using Framingham Cardiovascular Disease Dataset

## Table of Contents

1. [Introduction](#introduction)
2. [Previous Work](#previous-work)
3. [Methodology](#methodology)
   - [Dataset](#dataset)
   - [Computational Resources and Tools Used](#computational-resources-and-tools-used)
   - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Data Transformation for Modeling](#data-transformation-for-modeling)
4. [Classification Modeling](#classification-modeling)

## Abstract

About heart disease...

## About the data source

The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.

## Data matrics as pandas frame and meaning :

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

1. Sex: male or female(Nominal)
2. Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous)
   Behavioral
3. Education: 0: Less than High School and High School degrees, 1: College Degree and Higher
4. Current Smoker: whether or not the patient is a current smoker (Nominal)
5. Cigs Per Day: the number of cigarettes that the person smoked on average in one day. (can be considered continuous as one can have any number of cigarettes, even half a cigarette.)
   Medical( history)
6. BP Meds: whether or not the patient was on blood pressure medication (Nominal)
7. Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)
8. Prevalent Hyp: whether or not the patient was hypertensive (Nominal)
9. Diabetes: whether or not the patient had diabetes (Nominal)
   Medical(current)
10. Tot Chol: total cholesterol level (Continuous)
11. Sys BP: systolic blood pressure (Continuous)
12. Dia BP: diastolic blood pressure (Continuous)
13. BMI: Body Mass Index (Continuous)
14. Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)
15. Glucose: glucose level (Continuous)
    Predict variable (desired target)
16. 10 year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”)

## Prerequisites

Make sure you have the following installed:

- Jupyter Notebook with Python-3 kernel
- Required libraries (e.g. 'numpy', 'pandas', 'scikit-learn', 'seaborn', 'matplotlib', 'xgboost')

# HD-Prediction-App

# HD-Prediction-App

# HD-Prediction-App

# HD-Prediction-App
