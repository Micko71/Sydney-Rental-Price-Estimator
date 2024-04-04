import streamlit as st

st.title('Methodology and Results', anchor=False)
st.write('Data was scraped from a leading real estate site and used to build a multiple linear regression model for the prediction of rental property prices.')
st.divider()
#describe data collection and cleaning 
st.subheader('Data Collection and Cleaning',anchor=False)
st.write("""Rental property data representing property prices and features were scraped from the website and organised into a data frame. 
         The data was cleaned to extract numbers for numeric variables, to create defined and consistently labelled categories for categoric variables, and to ensure price data represented a weekly rent amount. 
        Observations which did not match the required schema were identified and removed, these included listings for parking spaces and rooms in share houses.""")
st.write("""Price outliers as defined by greater than 1.5 times the IQR above the third quartile were remove. 
         The justification for this was that these observations were heavily influenced by factors which were not represented in the available predictor variables.""")
#describe model training and assessment
st.subheader('Model Training and Results',anchor=False)
st.write("""The data was split 70:30 into training and test sets and a multiple linear regression model was fitted using ordinary least squares. 
         Predictor variables used were the number of bedrooms, bathrooms and parking spaces as well as the property type and postcode categorical variables which were one-hot-encoded for modelling. 
         Selected property type and postcode categories were combined based on an analysis of variance test.
         The final model resulted in an adjusted R2 of 0.69 and an F-statistic of 362.6((5,1252), p<.000). 
         This suggests that the combination of predictor variables used in the model explain around 70% of the variation in the target variable (Price). 
         All predictor variable coefficients have p-value < 0.05 suggesting that they are all statistically significant predictors of price (table 1).""")
#display table of predictor variable coefficients and p-values
st.image('predictor_results.jpg','Table 1. Model coefficients and p-values')
st.write('The plot of residuals shows no obvious pattern suggesting that a linear model is an appropriate model (Figure 1).')
st.image('residual_plot.jpg','Figure1, plot of training set residuals')
st.write('The model was applied to the test set and resulted in an R2 of 0.67 with a mean squared error of MSE= 64209.')
#conclusion
st.subheader('Conclusion',anchor=False)
st.write("""The predictor variables used in the model are all statistically significant at a p-value of <=0.05 and together capture around 70% of the variance in rental property price. 
         The remaining price variance can be attributed to other features (for example proximity to public transport) which are not included in the model.""")
