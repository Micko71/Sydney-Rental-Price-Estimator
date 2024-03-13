import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Rental Stats')

df = pd.read_csv('Sydney_test.csv')
df['Postcode'] = df['Postcode'].astype(str)

st.write('raw data')
st.write(df)

postcode = st.multiselect('choose postcode',['2000','2007','2009','2010','2011','All'])

if 'All' in postcode:
    postcode = ['2000','2007','2009','2010','2011']

st.write(postcode)

filtered_df = df[df['Postcode'].isin(postcode)]
filtered_df.reset_index(inplace=True)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.boxplot(filtered_df["Price"])
ax1.set_title('Boxplot of Price')
ax1.set_ylabel('Price')

ax2 = sns.histplot(filtered_df['Price'], bins=20,kde=True)

# Set labels and title
ax2.set_xlabel('Values')
ax2.set_ylabel('Frequency')
ax2.set_title('Histogram Example')

# Display the plot
st.pyplot(fig)



# Create a boxplot
fig, ax = plt.subplots()
ax.boxplot(df["Price"])
ax.set_title('Boxplot of Price')
ax.set_ylabel('Price')

# Display the plot in Streamlit
st.pyplot(fig)

# Investigate distribution of price with histogram (minus outliers noted above)
fig, ax = plt.subplots()
#ax = sns.histplot(df[df['Price']<5000]['Price'], bins=20,kde=True)
ax = sns.histplot(df['Price'], bins=20,kde=True)

# Set labels and title
ax.set_xlabel('Values')
ax.set_ylabel('Frequency')
ax.set_title('Histogram Example')

# Display the plot
st.pyplot(fig)