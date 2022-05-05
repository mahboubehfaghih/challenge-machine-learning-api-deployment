# API deployment

- Repository: `challenge-machine-learning-api-deployment`
- Type of Challenge: `Learning`
- Duration: `6 days`
- Deadline: `05/05/2022 04:30 PM` **(code)**
- Presentation: `06/05/2022 1:30 PM`
- Team challenge : Solo project

## Mission objectives

- Be able to deploy a machine learning model.
- Be able to create a Flask API that can handle a machine learning model.
- Deploy an API to Heroku.

## The Mission

The real estate company "ImmoEliza" is really happy about your data collection using web scrapping. Whenever a new property comes on the market, the question of how it should be priced naturally arises.

Now, the company asks you to create a machine learning model to predict prices on Belgium's real estate sales. "ImmoEliza" has hired you to build a tool that enables the company to predict property prices using linear regression.  

Take the dataset that was previously **scraped** and preprocess the data to be used with machine learning. 

In addition, they would like you to create an API to let their web-developers create a website around it.

Ideally, your API would ask a user to provide with information about a property (features) and return the estimated price using your model.

## Preparation
I am going to explain how to deploy trained linear regression machine learning model as a web application on Heroku.

Since most of the advanced libraries in machine learning available in python, I am going to use python for developing web application as well to avoid any inter language dependencies.This project has three steps.

#### Step 1: Train/Finalize/Save Your Machine Learning Model
I want to build some House’s price prediction webapp which predicts your house price based on your house’s features like "Number of bedrooms", "Living area", "Number of facades", "Surface area land" and etc. For this app, I am selecting "data Folder" dataset to train my ML model.

After model training, I saved the model in file name “house_price_prediction.pkl”. This is a trained model file ready to deploy on web application.

I have created one folder called “mlmodel” . In this folder I have placed trained linear regression model called “house_price_prediction.pkl”. 

#### Step 2: Create Application Web
I create web application that uses the trained model to predict new house selling price. I am using Flask frame work. Flask is a lightweight web framework for developing web applications. 

You can use trained model by just loading from .pkl file.

#### Step 3: Deploy Linear Regression Application
Third and final part is about deployment. I am using Heroku for deploying our house’ price prediction app.

Heroku needs only two basic files for deployment. 

The first thing I need to do is define which libraries my application uses. To achieve this, I need to create a requirements.txt file.

For Heroku to be able to run my application like it should, I need to define a set of processes/commands that it should run beforehand. These commands are located in the Procfile.

Once the application is created on Heroku, we're ready to deploy it online.
