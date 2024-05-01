
# Placement Prediction Model

This project focuses on building a machine learning model to predict whether a student will get placed based on their CGPA (Cumulative Grade Point Average) and IQ score. The model utilizes Logistic Regression to classify students into two categories: placed or not placed.

## Overview

The project involves several steps, including data preprocessing, exploratory data analysis (EDA), feature selection, model training, evaluation, and deployment.

### Steps Involved:

1. **Preprocessing and EDA**:
   - Load the dataset and remove unnecessary columns.
   - Check for missing values, null values, and duplicates.
   - Visualize the data using scatter plots to understand the relationship between CGPA, IQ, and placement status.

2. **Feature Selection**:
   - Identify input (independent) and output (dependent) variables.
   - Input variables: CGPA and IQ.
   - Output variable: Placement status.

3. **Splitting the Dataset**:
   - Split the dataset into training and testing sets using train_test_split from sklearn.model_selection.

4. **Scaling the Values**:
   - Scale the input variables to a range between 0 and 1 using StandardScaler from sklearn.preprocessing.

5. **Model Training**:
   - Utilize Logistic Regression from sklearn.linear_model to train the model on the training dataset.

6. **Model Evaluation**:
   - Predict placement status on the test dataset and calculate accuracy using accuracy_score from sklearn.metrics.

7. **Deployment**:
   - Deploy the trained model using Flask.

## Usage

### Installation

```bash
pip install pandas numpy scikit-learn mlxtend matplotlib flask
```

### Running the Flask App

```bash
python server.py
```

### Endpoints

- `/`: Home page.
- `/predict`: Endpoint to make predictions. Send CGPA and IQ as input in JSON format.

## Output Images

Include images of scatter plots and decision boundaries here.

![download](https://github.com/shivanagendrak/placement_Review/assets/40945928/898c031b-7daa-4c90-a775-c8b624ddc336)

![download (1)](https://github.com/shivanagendrak/placement_Review/assets/40945928/2c0bd706-3889-43e2-9ef9-a260b934807e)

##Video

https://github.com/shivanagendrak/placement_Review/assets/40945928/f6e72d4f-c022-46af-85b5-62472b9b562d




## Files

- `placement.csv`: Dataset containing student information.
- `server.py`: Flask application for model deployment.
- `model.pkl`: Pickled trained Logistic Regression model.

## Contributors

- [Shiva Nagendra](https://github.com/shivanagendrak)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
