# Sydney rental price estimator
This app uses a linear regression model to estimate Sydney rental prices based on location and selected property features.

The model used was trained on data scraped from a popular real estate site. The data was split 70:30 into training and test sets and the resulting model achieved an adjusted Rsquared of 0.67 on the test set. This suggests that around two thirds of the variation in rental property prices can be explained by the predictor variables.

The purpose of this project was to go through the complete process of scraping data from the web, cleaning and pre-processing the data, creating a predictive model with the data and deploying this model in a web application.

The app can be accessed at https://sydney-rental-price-estimator.streamlit.app/
