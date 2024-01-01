import bz2file as bz2
import pickle5 as pickle 
import streamlit as st 
import pandas as pd
import numpy as np
import test

pop_anime=pd.read_csv('pop_anime.csv')
with bz2.BZ2File('ss.pbz2','r') as f:
    similarity=pickle.load(f)
names=pop_anime['name'].values
dictt=pickle.load(open('dict.sav','rb'))   

st.sidebar.markdown("<h1 style='text-align: left; color: white;'>Anime Recommender</h1>", unsafe_allow_html=True)
#st.sidebar.markdown("<h3 style='text-align: left; color: white;'>This app predicts the **MSRP** of a car based on its specifications</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left; color: white;'>A simple web app to recommend anime</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: Green;'>Made by Prateek Verma</h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>Github:<a href='https://github.com/prateekverma145'>prateekverma145</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>LinkedIn:<a href='https://www.linkedin.com/in/prateek-verma-2a202b287'>prateek-verma</a></h4>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='text-align: left; color: white;'>Dataset:<a href='https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database'>prateekverma14</a></h4>", unsafe_allow_html=True)
def recommend(anime):
    res=[]
    anime_index=pop_anime[pop_anime['name']==anime].index[0]
    distances=sorted(list(enumerate(similarity[anime_index])),reverse=True,key=lambda x:x[1])
    for i in distances[1:6]:
        res.append(pop_anime.iloc[i[0]]['name'])
    return res    
st.header('Select an anime from the dropdown menu')

t=st.selectbox('Select Anime',names)
st.subheader('Recommended animes are: ')
col=st.columns(5)

if st.button('Recommend'):
    for i,j in enumerate(recommend(t)):
        with col[i]:
            st.write(j)
            st.write(f"rating: {pop_anime[pop_anime['name']==j]['rating'].values[0]}")
            st.image(test.fetch_poster(j,dictt[j]))        
    st.balloons()




