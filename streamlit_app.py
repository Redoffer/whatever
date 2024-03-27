import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown(" 'this is the header") 
st.subheader("this is the subheader") 
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')