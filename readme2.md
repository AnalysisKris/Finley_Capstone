# Gender Bias Detection in Job Descriptions

## Overview

This repository contains the code and documentation for a project focused on detecting gender bias in job descriptions using machine learning techniques. The primary goal was to develop a model that can identify potential gender bias in job descriptions to promote fairness and inclusivity in hiring practices.

## Data

The dataset used in this project was `gendered_data.csv`, which includes various job description attributes. Key features in the dataset included:
- **Numerical Features**: `word_count`, `age`, `min_salary`, `avg_salary`, `max_salary`, `Rating`, `Founded`
- **Categorical Features**: `job_state_encoded`, `num_comp_encoded`, `job_simp_encoded`, `headquarters_state_encoded`, `Sector_encoded`, `employer_provided`, `num_comp`, `Industry_encoded`, `same_state`, `aws`, `Type of ownership_encoded`, `seniority_encoded`, `hourly`, `spark`, `python_yn`, `R_yn`
- **Target Variable**: `Gender_Bias` (binary, indicating the presence or absence of gender bias based on a threshold of the ratio of `Agentic_Count` to `Communal_Count`)

## Model

### Random Forest Classifier

A Random Forest Classifier was employed to predict gender bias. The model was trained and evaluated using the following metrics:
- **Accuracy**: 87.25%
- **Confusion Matrix**: Provides insight into the number of correct and incorrect predictions for each class.
- **Classification Report**: Detailed precision, recall, and F1-score for each class.

#### Key Hyperparameters

The optimal hyperparameters for the Random Forest model were determined using GridSearchCV. The best hyperparameters identified were:
- `max_depth`: None
- `min_samples_leaf`: 1
- `min_samples_split`: 5
- `n_estimators`: 100

### Evaluation Metrics

- **Confusion Matrix**: 

    ![Confusion Matrix](images/confusion_matrix.png)

    |            | Predicted 0 | Predicted 1 |
    |------------|-------------|-------------|
    | Actual 0   | 63          | 8           |
    | Actual 1   | 11          | 67          |

- **Classification Report**:

    | Class | Precision | Recall | F1-Score | Support |
    |-------|-----------|--------|----------|---------|
    | 0     | 0.85      | 0.89   | 0.87     | 71      |
    | 1     | 0.89      | 0.86   | 0.88     | 78      |
    | Accuracy |       |        | 0.87     | 149     |
    | Macro Avg | 0.87  | 0.87   | 0.87     | 149     |
    | Weighted Avg | 0.87 | 0.87 | 0.87     | 149     |

- **ROC Curve**: 

    ![ROC Curve](images/roc_curve.png)

    The AUC score was 0.92, indicating strong performance in distinguishing between classes.

- **Precision-Recall Curve**:

    ![Precision-Recall Curve](images/pr_curve.png)

    The AUC score was 0.93, reflecting the model's precision and recall.

## Feature Importance

The analysis of feature importance revealed that the most influential features in predicting gender bias were:
- `desc_len`
- `Sentiment`
- `max_salary`
- `avg_salary`
- `min_salary`

Features such as `employer_provided`, `hourly`, and `R_yn` were found to have minimal impact.

### Feature Importances Table

    | Feature          | Importance |
    |------------------|------------|
    | desc_len         | 0.154      |
    | Sentiment        | 0.132      |
    | max_salary       | 0.124      |
    | avg_salary       | 0.115      |
    | min_salary       | 0.105      |
    | Sector_encoded   | 0.098      |
    | Industry_encoded | 0.090      |
    | employer_provided| 0.045      |
    | hourly           | 0.039      |
    | R_yn             | 0.037      |

##Conclusion
The Random Forest Classifier model effectively identified gender bias in job descriptions, achieving an accuracy of 87.25% and demonstrating balanced performance across both classes. The model's strong performance, as evidenced by the ROC and Precision-Recall curves, underscores its potential for practical application in promoting fairness in hiring practices. The feature importance analysis provided valuable insights into the key factors contributing to gender bias, guiding future work towards developing more inclusive job descriptions. Future research could enhance the model's performance further by exploring additional features, classifiers, and datasets to broaden its applicability.

## Limitations
The analysis had several limitations:

The assignment of communal and agentic words was subjective, potentially introducing bias.
The model's accuracy is dependent on the quality and representativeness of the data.
The dataset was limited to job descriptions related to data science, which may affect the model's applicability to other industries or regions.
The model only considered textual and basic numerical features, possibly overlooking other indicators of bias.

## Future Work
Future improvements could include:

Further hyperparameter tuning
Advanced feature engineering
Comparison with other classifiers
Expansion of the dataset to include diverse job descriptions

## Acknowledgments
Special thanks to [Data Source] for providing the dataset and [https://github.com/PlayingNumbers/ds_salary_proj/blob/master/eda_data.csv] for the source data used.