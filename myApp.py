import streamlit as st
st.title('Title *Markdown* 인식')
st.header('Title *Markdown* 헤더')
st.text('title *Markdown* 인식 못함.')
st.markdown('*markdown* 출력.')
st.text('this is some text.')
x=10
y=20
st.write('x=', x, 'y=', y)

import pandas as pd
df = pd.DataFrame({'col1':[1,2,3]})
df
st.write('데이터 프레임', df)

import matplotlib.pyplot as plt
import numpy as np
arr = np.random.normal(1,1,size=100)
fig,ax = plt.subplots()
ax.hist(arr, bins=20)
fig
code = '''def hello():
print("Hello, Streamlit!")''' 
st.code(code, language='python')
'This is :blue[blue]'
'This is :red[red]'
'This is :green[green]'

st.caption('This')
'여름엔 딱 좋아 :sunglasses:'
':100:점~'
':smile:ㅎㅎ :thumbsup:최고!!'
':sparkles:재밌다.:question::question:'

option = st.selectbox('Please select in selectbox!',('봄', '여름', '가을', '겨울'))

st.write('You selected:', option)