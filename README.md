# AI-Visa-Processing-Time-Estimator
Infosys Springboard Milestone 1
Intern: Nandini ALlavarapu
Mentor: Saadhana, Infosys Springboard

1. Objective
Prepare a clean dataset for visa applications.
Perform data preprocessing to make it ready for analysis and machine learning.

2. Data Collection
Created a synthetic dataset with the following columns:
app_id – Application ID
app_date – Date of application
decision_date – Date of visa decision
country – Applicant country
visa_category – Type of visa (Student, Work, Tourist)
Number of rows: 4
Number of columns: 5 (initially)

3. Data Cleaning
Converted app_date and decision_date from string to datetime format.
Handled missing values (if any) using forward fill (ffill).
Ensured all columns have consistent and correct formats.

4. Data Preprocessing
Feature Engineering:
processing_time_days = Days between decision_date and app_date (target variable)
delay_status = Categorized processing time:
Normal Delay ≤ 35 days
High Delay > 35 days
normalized_time = Standardized processing time for ML.
Final DataFrame Columns (8):
app_id | app_date | decision_date | country | visa_category | processing_time_days | delay_status | normalized_time

5. Statistics / Results

Average processing time: 36.75 days
Maximum processing time: 40 days
Conclusion:
Dataset is cleaned and preprocessed.
Ready for Exploratory Data Analysis (EDA) and Machine Learning model building.
This dataset is synthetically generated for academic and experimental purposes.
It simulates realistic visa processing scenarios.

How to Run the Code:
Requirements
Python 3.x installed
Pandas and Numpy libraries installed
pip install pandas numpy

Steps
Clone the repository or download the folder.
Open the folder in VS Code / Jupyter Notebook / Terminal.

Run the Python file:
python Milestone1_Data_Preprocessing.py
