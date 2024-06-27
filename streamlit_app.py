# Required Libraries
import streamlit as st
import pandas as pd
import altair as alt

# Title for the App
st.title("Google Search Console Data Comparison")

#File Upload
file1 = st.file_uploader("Upload File", type=["xls", "xlsx"])
file2 = st.file_uploader("Upload File2", type=["xls", "xlsx"])

# loading the data
if file1 and file2 is not None:
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # Data Wrangling
    # Rename the columns for a unified format if necessary
    # df1.columns = ['column_name1', 'column_name2', '...']
    # df2.columns = ['column_name1', 'column_name2', '...']

    # Perform DiD Analysis
    # This will depend on your specific DiD methodology
    # Assuming 'group' indicates the condition ('before', 'after') and 'year' indicates the grouping factor (this year, last year)
    # diff_in_diff = (df1[df1['group']=='after']['value'].mean() - df1[df1['group']=='before']['value'].mean()) - (df2[df2['group']=='after']['value'].mean() - df2[df2['group']=='before']['value'].mean())

    # Add the visualization to app
    st.write("Difference in Differences (DiD) Result: ", diff_in_diff)

    # visualize the data
    st.write('This Year:', df1)
    st.write('Last Year:', df2)

    # Assuming the dataframes df1 and df2 have a numerical 'value' column and 'date' column
    chart1 = alt.Chart(df1).mark_line().encode(
        x='date:T',
        y='value:Q'
    ).properties(title='This Year')

    chart2 = alt.Chart(df2).mark_line().encode(
        x='date:T',
        y='value:Q'
    ).properties(title='Last Year')

    st.altair_chart(chart1 + chart2)
