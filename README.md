# Heart Disease Detection Using Framingham Cardiovascular Disease Dataset

## Table of Contents

1. [Introduction](#introduction)
2. [About the data source](#about-the-data-source)
3. [Data matrics](#data-matrics)
   - [Dataset](#dataset)
   - [Computational Resources and Tools Used](#computational-resources-and-tools-used)
   - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Data Transformation for Modeling](#data-transformation-for-modeling)
4. [Classification Modeling](#classification-modeling)

## Introduction

About heart disease...
https://www.who.int/en/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)

## About the data source

The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.

## Data matrics

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

## Prerequisites

- Jupyter Notebook with Python-3 kernel
- Required libraries (e.g. 'numpy', 'pandas', 'scikit-learn', 'seaborn', 'matplotlib', 'xgboost')

## Data Preprocssing

Code Example:

<body>
    <p>Python Code</p>
    <pre>
    <code>
    import pandas as pd
    import numpy as np
    file_path = '/Users/z5601757/Documents/AriaResearch/Project/Dataset/DatasetToProcess/Framingham_CHD_preprocessed_data.csv'
    try:
        raw_framingham_data = pd.read_csv(file_path)
        column_headers = raw_framingham_data.columns.to_list()
        print(column_headers)
    except Exception as e:
        print(f"An error occurred: {e}")
    df = raw_framingham_data.copy()

    </code>
    </pre>

</body>

['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']
class: 'pandas.core.frame.DataFrame'
RangeIndex: 4133 entries, 0 to 4132
Data columns (total 16 columns):

# Column Non-Null Count Dtype

---

0 male 4133 non-null int64  
 1 age 4133 non-null int64  
 2 education 4133 non-null int64  
 3 currentSmoker 4133 non-null int64  
 4 cigsPerDay 4133 non-null float64
5 BPMeds 4133 non-null float64
6 prevalentStroke 4133 non-null int64  
 7 prevalentHyp 4133 non-null int64  
 8 diabetes 4133 non-null int64  
 9 totChol 4133 non-null float64
10 sysBP 4133 non-null float64
11 diaBP 4133 non-null float64
12 BMI 4133 non-null float64
13 heartRate 4133 non-null float64
14 glucose 4133 non-null float64
15 TenYearCHD 4133 non-null int64  
dtypes: float64(8), int64(8)
memory usage: 516.8 KB

![alt text](<images/Framingham preview.png>)

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

Clean up missing values or out of range values
Ref: https://www.kaggle.com/code/captainozlem/framingham-chd-preprossing-data/notebook

### Data conversion

<body>
    <p>Python Code</p>
    <pre>
    <code>
        import pandas as pd

        # File paths
        input_file = '/Users/z5601757/Documents/AriaResearch/Project/Dataset/heartDisease/reprocessed.hungarian.data'  # Replace with the path to your .data file
        output_file = '/Users/z5601757/Documents/AriaResearch/Project/Dataset/new.csv'  # Replace with your desired .csv file path

        # Step 1: Load the .data file
        # Assuming the .data file is comma-separated
        df = pd.read_csv(input_file, header=None)   # Use `header=None` if there's no header row

        # Step 2: Add column names (optional)
        # Replace ['col1', 'col2', ...] with appropriate column names
        # df.columns = ['col1', 'col2', 'col3', 'col4']

        # Step 3: Save as .csv
        df.to_csv(output_file, index=False)
        print(f"File converted and saved to {output_file}")
        print(df.head(10))
    </code>
    </pre>

</body>
