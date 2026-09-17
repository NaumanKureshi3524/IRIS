import numpy as np
import pandas as pd
import streamlit as st

# title
st.title("welcome to Avengers !")

#subt
st.write('I am Ironman')

df=pd.DataFrame({
    "Name":['Aadil','Dhruv','Harshad','Nauman','Nikul'],
    "Age":[20,20,20,21,20]
})

st.write(df)


print("    ")

st.write(" Random ")

print("   ")

r=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
st.write(r)

st.line_chart(r)