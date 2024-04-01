import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def get_median_values(df,feature):
    categories = df[feature].unique()
    median_values = {}
    for category in categories:
        filtered_df = df[df[feature]==category]
        median_value = filtered_df['Price'].median()
        median_values[category] = round(median_value)
        
    median_df = pd.DataFrame(list(median_values.items()), columns=[feature, 'Median Price'])
    median_df_sorted = median_df.sort_values(by='Median Price', ascending=False)
    return median_df_sorted

def grouped_boxplots(df,feature):
    #display grouped boxplots of price
        median_order = df.groupby(feature)['Price'].median().sort_values().index
        # Create grouped boxplot
        fig, ax = plt.subplots()
        ax = sns.boxplot(x=feature, y='Price', data=df, order=median_order)
        # Set labels and title
        ax.set_xlabel(feature)
        ax.set_ylabel('Price')
        ax.set_title(f'Grouped Boxplot by {feature}')
        #ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_xticklabels(ax.get_xticklabels())
        # Show the plot
        st.pyplot(fig)

def stacked_barchart(df,feature):
    # Calculate counts of each category
    category_counts = df[feature].value_counts()
    # Calculate percentages
    category_percentages = (category_counts / category_counts.sum())*100
    
    # Create DataFrame in wide format
    df_wide = pd.DataFrame({'Percentage': category_percentages}).T
    
    colors = plt.cm.tab10.colors  # Get colors from tab10 colormap

    # Plot the 100% stacked bar chart
    plt.figure(figsize=(8, 6))
    ax = df_wide.plot(kind='bar', stacked=True, color=colors, ax=plt.gca())
    # Remove x-tick labels
    ax.set_xticklabels([])
    # Add title and labels
    plt.title(f'100% Stacked Bar Chart {feature}')
    plt.xlabel(feature)
    plt.ylabel('Percentage')
    # Add percentage labels
    for p in ax.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')
    # Show the plot
    plt.legend(title=feature,loc='upper right')
    st.pyplot(plt)

def countplot(df, feature):
    # Convert integer categories to strings
    df[feature] = df[feature].astype(str)
    # Count occurrences of each category
    category_counts = df[feature].value_counts()

    # Create a color map using tab10
    colors = plt.cm.tab10.colors

    # Create count plot
    plt.figure(figsize=(8, 6))
    for i, (category, count) in enumerate(category_counts.items()):
        plt.bar(i, count, color=colors[i], label=category)

    # Set labels and title
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.title(f'Count Plot of {feature}')
    # Set x-tick labels
    plt.xticks(range(len(category_counts)), category_counts.index)
    # Add legend
    plt.legend(title=feature, loc='upper right')
    # Show the plot
    st.pyplot(plt)

df = pd.read_csv('modelling6_df.csv')

st.title('Data Snapshot',anchor=False)
st.write(f'The information presented here is based data from a sample of {len(df)} rental properties scraped from a leading real estate website.')
st.divider()

#get median price
median_price = df["Price"].median()

st.subheader(f'The estimated median value of Sydney rental properties is: :green[${round(median_price)}]',
             anchor=False)

#get selected group by option
group_by_options = ['none','Group by postcode', 'Group by property type',
                    'Group by number of bedrooms',]
col1,col2 = st.columns(2)
group_by = col1.selectbox('Drill down options (Price):',group_by_options)

price_charts = st.empty()

#define columns
col1, col2 = price_charts.columns(2)

if group_by == 'none':
    with col1:
        # Investigate distribution of price with histogram
        fig, ax = plt.subplots() 
        ax = sns.histplot(df['Price'], bins=20,kde=True)
        # Set labels and title
        ax.set_xlabel('Values')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Price')
        # Display the plot
        st.pyplot(fig)
    with col2:
        # Create a boxplot
        fig, ax = plt.subplots()
        sns.violinplot(df["Price"], inner='box',ax=ax)
        ax.set_title('Violin Plot of Price')
        ax.set_ylabel('Price')
        # Display the plot in Streamlit
        st.pyplot(fig)
    
else:
    if group_by == 'Group by property type':
        feature = 'Property_Type'
    elif group_by == 'Group by postcode':
        feature = 'Postcode' 
    else:
        feature = 'Bed'
    with col1:
        #display table of grouped median prices
        median_df = get_median_values(df,feature)
        st.dataframe(median_df, hide_index=True)
    with col2:
        #display grouped boxplots
        grouped_boxplots(df,feature)

predictor_variables = ['Property_Type', 'Bed', 'Bath', 'Parking', 'Postcode']
col1,col2 = st.columns([1,2])
feature = col1.selectbox('Predictor variable distributions:',predictor_variables)

#define feature charts container
feature_charts = st.empty()

#define columns
col1, col2 = feature_charts.columns(2)
#display countplot and stacked barchart
with col1:
    countplot(df,feature)
with col2:
    stacked_barchart(df,feature)
    



