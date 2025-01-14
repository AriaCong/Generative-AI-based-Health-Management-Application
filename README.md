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
      <th scope="col">male</th>
      <th scope="col">age</th>
      <th scope="col">education</th>
      <th scope="col">currentSmoker</th>
      <th scope="col">cigsPerDay</th>
      <th scope="col">BPMeds</th>
      <th scope="col">prevalentStroke</th>
      <th scope="col">prevalentHyp</th>
      <th scope="col">diabetes</th>
      <th scope="col">totChol</th>
      <th scope="col">sysBP</th>
      <th scope="col">diaBP</th>
      <th scope="col">BMI</th>
      <th scope="col">heartRate</th>
      <th scope="col">glucose</th>
      <th scope="col">TenYearCHD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>male or female</td>
      <td>Age of the patient</td>
      <td>0: Less than High School and High School degrees, 1: College Degree and Higher</td>
      <td>whether or not the patient is a current smoker</td>
      <td>the number of cigarettes that the person smoked on average in one day</td>
      <td>whether or not the patient was on blood pressure medication </td>
      <td>whether or not the patient had previously had a stroke</td>
      <td>whether or not the patient was hypertensive</td>
      <td>whether or not the patient had diabetes</td>
      <td>total cholesterol level</td>
      <td>systolic blood pressure</td>
      <td>diastolic blood pressure</td>
      <td>Body Mass Index</td>
      <td>In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values</td>
      <td>glucose level</td>
      <td>“1”-Yes, “0”-No</td>
    </tr>
    <tr>
        <td>Binary</td>
        <td>Continous</td>
        <td>Binary</td>
        <td>Binary</td>
        <td>Continous</td>
        <td>Binary</td>
        <td>Binary</td>
        <td>Binary</td>
        <td>Binary</td>
        <td>Continous</td>
        <td>Continous</td>
        <td>Continous</td>
        <td>Continous</td>
        <td>Continous</td>
        <td>Continous</td>
        <td>Binary</td>
    </tr>

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
