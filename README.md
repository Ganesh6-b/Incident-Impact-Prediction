# Incident-Impact-Prediction

This effect could be positive: a return on investment or customer satisfaction such as a new feature or improvement to a product. Conversely, it could be very negative based on the degree of damage or cost that results. Loss of revenue, manhours, or customers following IT service downtime or poor performance are all negative effects.

Usually, impact would not be expressed in absolute terms, but rather a range or degree that is subject to the interpretation of your company’s context.

This range might include:

Number of customers/users affected
Amount of lost revenue or incurred costs
Number of IT systems/services/elements involved
A variety of terms can help identify the impact, or effect, of an incident:

High
Medium
Low

Remember that words matter: all involved parties must share the same understanding of the scales you use. Clear, common understanding of the impact scale is the first step in effective prioritizing.

Steps involved in this project:

### Dataset
### Data Analysis
### Data Preprocessing
### Feature Selection
### Model Building
### Deployment in Local System
### Making live using Heroku Cloud Platform

Explaining the steps which i have performed in this project in a few words.

1) Dataset: The dataset is having incidents raised by customers.Which contains an event log of an incident management process extracted from a service desk platform of an IT company.

2) Data Analysis: Dataset is having a 25 independent variable and one dependent variable which is impact feature. By performing various visualizations and analysis, generating more and more insights from the data.

3)Data Preprocessing: By Performing one hot encoding and label encoding and also mean and probability encoding for the catagorical variable's. Based on the performance of the model, the specific encoding process is taken for the final model. 

4) Feature Selection: feature selection process is takes place for selecting the specified features suitable for building the model to predict the dependent variable. Various feature selection techniques i have used, such as ExtraTreesClassifier, SelectKModel, Correlation, Mutual info classif and also Univariate Selection.

5) Model Building: I built various models with multiple algorithms such as Logistic Regression, Decision Tree Classifier, K Nearest Neighbour, Naive Bayes, Support Vector Machines and with multiple meta algorithms such as XGBoost Classifier, Gradient Boost and with neural network models with ANN.  Based on the Classification report, i choosed the best model Decision tree Classifier for the project. 

6) Deployment in Local System: For Show casing the project, I used Django Framework.

7) Cloud Platform: To make it live, I choosen the heroku platform.

### To see my website Go to >>> Https://incidentimpactprediction.herokuapp.com
