# Gender Bias Detection in Job Descriptions

## Project Overview

This project focused on detecting gender bias in job descriptions using various machine learning algorithms. The primary goal was to develop and evaluate predictive models to classify job descriptions based on the presence of gender bias, specifically looking at communal and agentic word counts. The advanced features of this project included handling class imbalance, implementing a machine learning pipeline, and evaluating multiple models.

## Data Source

The dataset used in this project was sourced from the [Data Science Salary Estimator](https://github.com/PlayingNumbers/ds_salary_proj/blob/master/eda_data.csv) project, created by [PlayingNumbers](https://github.com/PlayingNumbers/ds_salary_proj).

### Web Scraping from Source Dataset

The original project from which the dataset was obtained tweaked the web scraper GitHub repo to scrape 1000 job postings from Glassdoor.com, collecting data on job title, salary estimate, job description, rating, company, location, company headquarters, company size, company founded date, type of ownership, industry, sector, revenue, and competitors.

### Data Cleaning from Source Dataset

The data was cleaned to make it usable for the model:
- Parsed numeric data out of salary.
- Created columns for employer-provided salary and hourly wages.
- Removed rows without salary.
- Parsed rating out of company text.
- Created a new column for company state.
- Added a column indicating if the job was at the company’s headquarters.
- Transformed founded date into the age of the company.
- Created columns for the presence of different skills in the job description (Python, R, Excel, AWS, Spark).
- Added columns for simplified job title and seniority.
- Created a column for description length.

### Data Collection from Source Dataset

- **Method:** Scraped over 1000 job descriptions from Glassdoor using Python and Selenium.
- **Features Collected:**
  - Job title
  - Salary estimate
  - Job description
  - Company rating
  - Company name
  - Location
  - Company headquarters
  - Company size
  - Company founded date
  - Type of ownership
  - Industry
  - Sector
  - Revenue
  - Competitors

## Advanvanced Features
The source dataset was further transformed for the purposes of this project.

### 1. Data Preprocessing

- **Handling Missing Values:** Missing values in the dataset were imputed using appropriate strategies, ensuring no loss of data integrity.
- **Feature Encoding:** Categorical features were encoded using `OneHotEncoder` for nominal variables and label encoding for ordinal variables.
- **Feature Scaling:** Numerical features were scaled using `StandardScaler` to standardize the range of values, which is particularly important for algorithms like K-Nearest Neighbors (KNN).

### 2. Feature Engineering

- **Agentic and Communal Word Counts:** New features were engineered by counting the occurrences of agentic and communal words in job descriptions.
- **Text Length Features:** Features such as the length of the job description were included to provide additional context for the models.

### 3. Model Training and Evaluation

- **Algorithms Used:**
  - **Random Forest:** Selected for its robustness and ability to handle feature importance and interactions.
  - **XGBoost:** Chosen for its efficiency and performance, especially with imbalanced datasets.
  - **Logistic Regression:** Implemented for its simplicity and interpretability.
  - **K-Nearest Neighbors (KNN):** Included for its effectiveness in certain types of problems where class boundaries are not well-defined.

- **Hyperparameter Tuning:** Grid search and random search were used to optimize model parameters, enhancing performance.
- **Cross-Validation:** A 5-fold cross-validation approach was employed to ensure robust model evaluation and prevent overfitting.

### 4. Addressing Class Imbalance

- **SMOTE (Synthetic Minority Over-sampling Technique):** Applied to oversample the minority class (Gender_Bias = 1), creating a balanced dataset for training.
- **Cost-Sensitive Learning:** Implemented to assign higher penalties for misclassifying the minority class, thereby improving recall.

### 5. Model Evaluation Metrics

- **Accuracy:** Overall accuracy of the model predictions.
- **Precision, Recall, and F1-score:** Detailed metrics for both classes, with a focus on improving the recall for the minority class (Gender_Bias = 1).
- **Confusion Matrix:** Used to visualize the performance of the models and understand misclassification patterns.

### 6. Implementation Details

- **Libraries Used:**
  - `scikit-learn`: For model training, evaluation, and preprocessing.
  - `pandas`: For data manipulation and preprocessing.
  - `numpy`: For numerical operations.
  - `imbalanced-learn`: For implementing SMOTE.

- **Pipeline Workflow:**
  - Data was preprocessed to handle missing values and encode categorical features.
  - Numerical features were scaled.
  - Models were trained using the processed data.
  - Hyperparameters were tuned using grid search and cross-validation.
  - Model performance was evaluated on a separate test set.

### 7. Key Insights and Challenges

- **Handling Imbalance:** Effective handling of class imbalance was crucial for improving the detection of the minority class. SMOTE and cost-sensitive learning were key techniques used.
- **Feature Importance:** Random Forest and XGBoost provided insights into feature importance, helping to understand which features contributed most to the predictions.
- **Model Performance:** While Random Forest and XGBoost outperformed other models in overall accuracy, KNN offered simplicity and showed potential with appropriate parameter tuning.
- **Challenges Addressed:** The biggest challenge was the class imbalance, which was addressed through multiple techniques, including SMOTE and cost-sensitive learning.

### Results

- **Random Forest Model:**
  - Accuracy: 91.3%
  - Precision (Gender_Bias = 1): 100%
  - Recall (Gender_Bias = 1): 70%
  - F1-score (Gender_Bias = 1): 82%

- **K-Nearest Neighbors Model:**
  - Accuracy: 72.3%
  - Precision (Gender_Bias = 1): 35%
  - Recall (Gender_Bias = 1): 8%
  - F1-score (Gender_Bias = 1): 13%

### Conclusion

The project successfully implemented a machine learning pipeline to detect gender bias in job descriptions. Advanced preprocessing, feature engineering, and handling of class imbalance led to promising results. Future work will focus on refining the models, incorporating more sophisticated NLP techniques, expanding the dataset, and exploring additional bias mitigation strategies.


