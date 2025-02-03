age: Patient's Age in years (Numeric)
sex: Patient's Gender Male as 1 Female as 0 (Nominal) bool
chest pain type: Type of chest pain categorized into 1 typical, 2 typical angina, 3 non-anginal pain, 0 asymptomatic
resting bps: Level of blood pressure at resting mode in mm/HG (Numeric)
cholesterol: Serum cholestrol in mg/dl (Numeric)
fasting blood sugar: Blood sugar levels on fasting > 120 mg/dl represents as 1 in case of true and 0 as false
resting ecg: result of electrocardiogram while at rest are represented in 3 distinct values 0 : Normal 1: Abnormality in ST-T wave 2: Left ventricular hypertrophy
max heart rate: Maximum heart rate achieved (Numeric)
exercise angina: Angina induced by exercise 0 depicting NO 1 depicting Yes (Nominal)
oldpeak: Exercise induced ST-depression in comparison with the state of rest (Numeric)
ST slope: ST segment measured in terms of slope during peak exercise 0: Normal 1: Upsloping 2: Flat 3: Downsloping

Normalisation of the numeric features
Encode categorical features:
- one-hot encoding for small categorical variables
- embeddings for large/high-cardinality variables (e.g., thousands of categories)



A correlation coefficient > 0.9 indicates high correlation.