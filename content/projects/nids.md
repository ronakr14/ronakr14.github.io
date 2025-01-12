---
title: "Network Intrusion Detection System V0.1"
date: 2025-01-11T18:10:02+05:30
draft: false
author: Ronak Rathore
tags: ["Network Detection", "Intruder Detection", "Machine Learning", "Docker", "Python", "AWS EC2", "Classification", "Supervised Learning"]
image: /images/projects/nids/0.jpeg
---
A binary classification machine learning model for Intrusion Detection System.

A special thanks to Satish Kamble.

---
## Abstract
This machine learning model for binary classification identifies users on our network system and divides them into benign and malignant categories. Every network, whether it is private or public, is vulnerable to assaults that stop the regular flow of traffic on networks, as we all know. The fundamental goal of developing this architecture was to protect both public and private networks while warning the administrator of potential future harm.

---
## Tools and Platform
- Editors - Jupyter, Nano
- Language - Python
- Libraries - Sklearn, Pandas, Numpy, Matplotlib, Seaborn, Pickle
- Deployment - AWS EC2, Docker, Python-Flask
- Browser - any

---
## Data Collection
An extensive dataset available on kaggle that combines all of the datasets previously described in: https://staff.itee.uq.edu.au/marius/NIDS_datasets/#RA5

The DoS category’s parent name has been given to the assaults formerly known as DoS attacks-Hulk, DoS attacks-SlowHTTPTest, DoS attacks-GoldenEye, and DoS attacks-Slowloris. DDoS has been used to refer to attacks formerly known as DDOS attack-LOIC-UDP, DDOS attack-HOIC, and DDoS attack-LOIC-HTTP. Brute-force attacks include those with the names FTP-BruteForce, SSH-BruteForce, Brute Force -Web, and Brute Force -XSS. Lastly, SQL Injection attacks have been added to the category of injection attacks.

11,994,893 entries make up the NF-UQ-NIDS dataset, of which 2,786,845 (23.23%) are attacks and 9,208,048 (76.77%) are benign flows.

- Kaggle Link - NF-UQ-NIDS-v2

---
## Exploratory Data Analysis
Exploratory data analysis is the crucial process of doing first investigations on data in order to identify patterns, find anomalies, test hypotheses, and double-check assumptions using summary statistics and graphical representations.
<table>
<tr>
<td>
<ol>
<li>Numerical column description.</li>
<li>Count plot on target column.</li>
<li>Skewness and Kurtosis.</li>
<li>Histogram.</li>
</ol>
</td>
<td>
<ol start="5">
<li>Box plot.</li>
<li>Null value.</li>
<li>Duplicate rows.</li>
<li>Correlation.</li>
</ol>
</td>
</tr>
</table>

---
## Data Pre-processing
<table>
<tr>
<td>
<ol>
<li>Data cleaning.</li>
<li>Label encoding.</li>
<li>Outlier management.</li>
</ol>
</td>
<td>
<ol start="4">
<li>Standardize data.</li>
<li>Under sampling data.</li>
<li>Train-Test-Validation split.</li>
</ol>
</td>
</tr>
</table>

---
## Feature Selection
Eventually, the data scientist will need to determine how helpful a variable is on a larger scale. After preprocessing, the NIDS dataset’s more than 40 features were raised to 120. When we explored models without feature selection, we ran into an issue with overfitting. Therefore, we tried feature selection to avoid overfitting and provide more precise findings by removing unimportant features.

We are selecting features on the basis of three methods:

1. Decision Tree
2. Recursive Feature Elimination
3. Principal Component Analysis

---
## Algorithms
<table>
<tr>
<td>
<ol>
<li>Logistic Regression.</li>
<li>K Nearest Neighbor.</li>
<li>Naïve Bayes - Bernoulli &amp; Gaussian.</li>
</ol>
</td>
<td>
<ol start="4">
<li>Desicion Tree.</li>
<li>Random Forest.</li>
<li>Gradient Boost.</li>
</ol>
</td>
</tr>
</table>

---
## Evaluation
We have used following evaluating terms for the models:

<table>
<tr>
<td>
<ol>
<li>Cross Validation Score</li>
<li>Accuracy</li>
<li>Confusion Matrix</li>
</ol>
</td>
<td>
<ol start="4">
<li>Precision, Recall, F1 Score</li>
<li>ROC Curve</li>
<li>Precision Recall Curve</li>
</ol>
</td>
</tr>
</table>

---
## Deployment
After evaluating the results of the previously described methods, we settled on the random forest classifier model with decision tree as the feature selection model.

The pickle file for this model will be used to deploy the Machine Learning model using the flask application.

This Docker container-based Flask application will be installed on an AWS EC2 instance for easier access for other users.

The Flask UI will be used to collect the user’s input features, process them to produce results, and display the results.

---
## Summary
1. In this research, we developed a model for categorising data into dichotomous variables based on traffic flow, port numbers, and DNS.
2. Data was acquired for model construction from Kaggle.com.
3. We removed any null values, outliers, duplicate rows, and columns with a single value from the data.
4. On categorical columns, we carried out label encoding.
5. After testing various feature selection techniques on the cleaned dataset, we discovered that the feature chosen using the Decision  Tree model outperformed the others in the dataset.
6. On the cleansed dataset, a dozen alternative models were built. The best models were discovered to be Gradient Boosting Classifier and Random Forest Classifier.
7. Created a web application using the Flask framework to make it simple to classify various user inputs using the model.
8. Webapp will let the user know what category it belongs to.


---
## References
1. Machine Learning Methods for Network Intrusion Detection, Mouhammd Alkasassbeh, Mohammad Almseidin (2018)
2. Network intrusion detection system: A machine learning approach,Mrutyunjaya Panda, Ajith Abraham, Swagatam Das, Manas Ranjan Patra (2011)

---
## More Details
1. Source code - Network Intrusion Detection System.
2. Documentation - Network Intrusion Detection System - document file.