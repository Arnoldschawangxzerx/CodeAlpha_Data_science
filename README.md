# CodeAlpha_tasks
My internship projects at Code Alpha 
TASK 1: Iris Flower Classification using Machine Learning
   
 Introduction:The objective of this task is to build a machine learning classification model that can accurately predict the species of an Iris flower based on its physical measurements. This task helps in understanding the fundamentals of supervised learning, classification algorithms, data splitting, model training, and evaluation. The Iris dataset is a well-known dataset in machine learning and contains measurements of three different Iris species:
      Iris Setosa,
      Iris Versicolor,
      Iris Virginica
      
    1. Dataset Description
      The Iris dataset consists of 150 samples, with 4 input features and 1 output label.
      Input Features:
        Sepal Length (cm)
        Sepal Width (cm)
        Petal Length (cm)
        Petal Width (cm)
      Target Variable:
        Species of the flower (Setosa, Versicolor, Virginica)
      The data set is balanced, with 50 samples per class, making it suitable for classification tasks.
    2. Tools & Libraries Used
      The following Python libraries were used to complete this task:
      Scikit-learn → Dataset loading, model building, training, and evaluation
      Pandas → Data handling and tabular representation
      Matplotlib → Visualization of the decision tree
    3. Methodology
       3.1 Loading the Dataset
        The Iris dataset was loaded using the built-in load_iris() function from Scikit-learn. This avoids manual downloading and ensures clean and standardized data.
       3.2 Data Splitting
        The dataset was split into:
          80% Training Data
          20% Testing Data
        This was done using train_test_split() to ensure unbiased evaluation of the model.
       3.3 Model Selection
         A Decision Tree Classifier was selected because:
          It is easy to understand and interpret
          It performs well on small datasets
          It visually represents decision-making rules
        3.4 Model Training
          The model was trained using the training dataset, where it learned patterns and rules based on the flower measurements.
        3.5 Model Evaluation
          After training, the model was tested on unseen data. The performance was evaluated using:
          Accuracy Score
          Classification Report (Precision, Recall, F1-score)
TASK 2: Car Price Prediction Using Machine Learning

Introduction: Car price prediction is a real-world machine learning application that helps estimate the market value of vehicles based on various features. This project aims to develop a regression model that predicts car prices       using machine learning techniques.

1. Dataset Description
    The dataset contains information about cars and their selling prices.
    Key Features:
      Brand / Car Name
      Year of Manufacture
      Mileage
      Engine Power
      Fuel Type
    Target Variable:
      Selling Price
  2. Tools & Libraries Used
     Python
     Pandas – Data preprocessing and handling
     Scikit-learn – Model building and evaluation
     Matplotlib – Visualization

  3. What I did:
     3.1 Data Cleaning
      Removed missing values
      Converted categorical features into numerical form using one-hot encoding
     3.2 Feature Selection
      Independent variables were selected based on car characteristics, while the selling price was used as the dependent variable.
     3.3 Model Training
      A Linear Regression model was used to learn the relationship between car features and selling price.
     3.4 Model Evaluation
        The model was evaluated using:
        Mean Absolute Error (MAE)
        Mean Squared Error (MSE)
        R² Score
  4. Results
    The model was able to predict car prices with reasonable accuracy.
    The scatter plot of actual vs predicted prices showed a positive correlation.
    Performance metrics confirmed the effectiveness of regression modeling.
  5. Real-World Applications
    Used car price estimation platforms
    Insurance premium calculation
    Automotive market analysis
    Decision-making for buyers and sellers
  6. Conclusion
    This project demonstrates how machine learning regression techniques can be applied to predict car prices. The task provided hands-on experience with data preprocessing, model training, evaluation, and visualization.


TASK 3: Sales Prediction using Python:
Objective:
Predict future sales based on advertising spend, target segment, and platform. Also analyze how advertising affects sales to help marketing decision-making.
📌 Project Overview

This project focuses on predicting future sales using data-driven techniques in Python. The goal is to analyze how different advertising channels, target segments, and platforms influence sales outcomes and to build a predictive model that can assist businesses in making informed marketing decisions.

The project was developed as part of a remote Data Science internship and demonstrates the complete machine learning workflow, including data preprocessing, exploratory analysis, model building, evaluation, and business insight generation.

🎯 Objectives

Predict sales based on advertising spend and marketing-related features
Clean and preprocess real-world data for modeling
Apply regression techniques to forecast sales
Analyze the impact of advertising strategies on revenue
Generate actionable insights to optimize marketing spend

🗂️ Dataset Description

The dataset contains historical sales and advertising data, including:
Advertising spend across multiple channels (e.g., TV, social media, search ads)
Target customer segments
Marketing platforms
Sales figures
Categorical variables such as platform and target segment are encoded, and missing values are handled to ensure data consistency.

🛠️ Tools & Technologies

Python
Google Colab
Pandas & NumPy – Data manipulation and preprocessing
Matplotlib & Seaborn – Data visualization
Scikit-learn – Machine learning modeling and evaluation

🔄 Project Workflow

Data Loading
Dataset uploaded and loaded using Google Colab
Exploratory Data Analysis (EDA)
Understanding data structure, distributions, and missing values
Data Cleaning & Transformation
Handling missing values
Encoding categorical variables using one-hot encoding
Feature Selection
Identifying relevant features affecting sales
Model Building
Implemented a Linear Regression model to predict sales
Model Evaluation
Evaluated using MAE, RMSE, and R² score
Advertising Impact Analysis
Analyzed regression coefficients to understand how advertising spend affects sales
Sales Forecasting
Predicted future sales based on sample advertising strategies

📈 Model Evaluation Metrics
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score
These metrics help assess prediction accuracy and overall model performance.

💡 Key Insights
Advertising spend has a significant positive impact on sales performance
Certain marketing platforms contribute more effectively to revenue growth
Optimized allocation of advertising budget can improve ROI
Predictive modeling enables better campaign planning and sales forecasting

