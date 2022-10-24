import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities')

df = pd.read_csv('worldcities.csv')

#add a slider

pop_slider = st.sidebar.slider('Choose Population', 0.0, 40.0, 3.60)

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # 总options
     df.capital.unique())  # defaults一开始显示的选项(默认选项)

#filter by population
df = df[df.population >= pop_slider]

#capital_filter is a list of userchoice
#filter by capital
df = df[df.capital.isin(capital_filter)]

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

#filter by country name
if country_filter!='ALL':
    df = df[df.country == country_filter]


#show on map
st.map(df)

#show df
st.write(df)
#show the pop plot
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)