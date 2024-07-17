import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE

# Load cleaned dataset
df = pd.read_csv('cleaned_dataset.csv')

# Define a threshold for classifying gender bias based on scores or frequencies
communal_mean = df['communal_score'].mean()
agentic_mean = df['agentic_score'].mean()

# Define a function to classify gender bias
def classify_gender_bias(row):
    if row['communal_score'] > communal_mean and row['agentic_score'] > agentic_mean:
        return 1  # Indicates gender bias present
    else:
        return 0  # Indicates no gender bias or less bias

# Apply the function to create the gender_bias_label column
df['gender_bias_label'] = df.apply(classify_gender_bias, axis=1)

# Assuming X and y are defined as per your dataset structure
X = df[['communal_score', 'agentic_score', 'seniority_level', 'sentiment', 'flesch_reading_ease']]
y = df['gender_bias_label']

# Define preprocessing steps including handling categorical variables
column_transformer = ColumnTransformer([
    ('onehot', OneHotEncoder(), ['seniority_level'])  # Encode 'seniority_level'
], remainder='passthrough')

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to resample the training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Define pipeline with preprocessing and classifier
pipeline = Pipeline([
    ('preprocess', column_transformer),
    ('classifier', LogisticRegression())  # Example classifier, replace with your choice
])

# Define parameters for grid search
param_grid = {
    'classifier__C': [0.1, 1, 10],
    'classifier__penalty': ['l1', 'l2']
}

# Perform grid search
grid_search = GridSearchCV(pipeline, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)
grid_search.fit(X_train_resampled, y_train_resampled)

# Evaluate best model on test data
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred))
