# Detecting Gender Bias in Glassdoor Job Listings

This repository contains code and resources for a data science project that aims to detect gender bias in job listings sourced from Glassdoor. The project utilizes machine learning techniques to analyze job descriptions and associated metadata to identify potential biases based on gender-specific language and job requirements.

## Project Overview

The goal of this project is to:
- Scrape job listings from Glassdoor, focusing on details such as job titles, descriptions, qualifications, and company information.
- Develop machine learning models to predict gender-associated biases in job listings.
- Evaluate the models based on metrics such as precision, recall, and F1-score.
- Provide insights and visualizations to interpret the results and identify potential biases.

## Project Structure

The repository is structured as follows:

- **data/**: Placeholder directory for storing scraped job listings and any processed data.
- **notebooks/**: Jupyter notebooks for data preprocessing, model development, and result analysis.
- **scripts/**: Python scripts for web scraping, data cleaning, feature engineering, and model evaluation.
- **README.md**: This file, providing an overview of the project and instructions for usage.
- **requirements.txt**: List of Python packages required to run the code.

## Getting Started

### Prerequisites

- Python 3.x
- Libraries listed in `requirements.txt` (`pip install -r requirements.txt`)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/gender-bias-linkedin.git
   cd gender-bias-linkedin
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. **Scraping Glassdoor Data**: Use the provided scripts or adapt them to scrape job listings from Glassdoor. Note: This project originally was focused on Linkedin, however web scrapping is not compliant with LinkedIn's terms of service.
   
2. **Data Preprocessing**: Clean and preprocess the scraped data using Jupyter notebooks provided in the `notebooks/` directory.

3. **Model Development**: Develop machine learning models (e.g., logistic regression, SVM, neural networks) to predict gender bias in job listings. Implement feature engineering and model training based on the cleaned data.

4. **Evaluation**: Evaluate model performance using appropriate metrics (precision, recall, F1-score) and visualize results to interpret bias detection.

5. **Documentation and Reporting**: Document findings, insights, and limitations of the model and data sources used. Use visualizations and statistical tests to support conclusions.

