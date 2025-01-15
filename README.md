# Heart Disease Detection Using Framingham Cardiovascular Disease Dataset

## Table of Contents

1. [Introduction](#introduction)
2. [Avaliable data source](#about-the-data-source)
   - [heart_disease_combined_data](#)
3. [Data matrics](#)
   - [Dataset](#dataset)
   - [Computational Resources and Tools Used](#computational-resources-and-tools-used)
   - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Data Transformation for Modeling](#data-transformation-for-modeling)
4. [Classification Modeling](#classification-modeling)

## Introduction

About heart disease...
https://www.who.int/en/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)

## Avaliable data source

1. heart_disease_combined_data.csv

- A dataset contains 4 databases: Cleveland, Hungary, Switzerland, and the VA Long Beach
- This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).
- The names and social security numbers of the patients were recently removed from the database, replaced with dummy values. One file has been "processed", that one containing the Cleveland database. All four unprocessed files also exist in this directory.
- Contains missing values
- Source: https://archive.ics.uci.edu/dataset/45/heart+disease

['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
14 features excluding unique id and the last column as result

RangeIndex: 920 entries, 0 to 919
Data columns (total 16 columns):

---

0 id 920 non-null int64  
 1 age 920 non-null int64  
 2 sex 920 non-null object
3 dataset 920 non-null object
4 cp 920 non-null object
5 trestbps 861 non-null float64
6 chol 890 non-null float64
7 fbs 830 non-null object
8 restecg 918 non-null object
9 thalch 865 non-null float64
10 exang 865 non-null object
11 oldpeak 858 non-null float64
12 slope 611 non-null object
13 ca 309 non-null float64
14 thal 434 non-null object
15 num 920 non-null int64  
dtypes: float64(5), int64(3), object(8)
memory usage: 115.1+ KB

2. Framingham Lifestyle Dataset:

- The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has a 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes.
- Contains missing and invalid data -> data preprocessing done
- Source: https://www.kaggle.com/code/captainozlem/framingham-chd-preprossing-data/notebook

3. Healthcare Stroke dataset:

- Source: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

### Heart Disease Combined Data Matrics

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

### Framingham Data Matrics

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

['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose', 'TenYearCHD']
class: 'pandas.core.frame.DataFrame'
Range Index: 4133 entries, 0 to 4132
Data columns (total 16 columns):

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

## Methodology

### Dataset

The Cleveland Heart Disease dataset, available in the UCI Machine Learning Repository, was used for this research. The dataset consists of 76 attributes, but we focused on a subset of 13 features used in previous studies. These features include age, sex, chest pain type (cp), resting blood pressure (trestbps), serum cholesterol (chol), fasting blood sugar (fbs), maximum heart rate achieved (thalach), exercise-induced angina (exang), ST depression (oldpeak), slope of the peak exercise (slope), number of major vessels (ca), and types of defect (thal). The target variable, `disease_present`, was mapped to binary values indicating the absence or presence of heart disease.

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

python version 3.10.16
conda env vscode_env

conda create --name vscode_env python=3.10
conda install jupyter numpy pandas
conda list numpy
