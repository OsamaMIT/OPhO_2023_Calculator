import streamlit as st
import pandas as pd
import random
import math

st.set_page_config(page_title='OPhO23 Calculator', page_icon='⚛', layout="centered", menu_items=None)
st.title('OPhO 2023 Points Calculator')

# Calculator-Input section 
st.subheader('Calculator')
n = st.number_input('Question Number?', min_value=1, max_value=35)
i = ( st.number_input('Number of attempts?', min_value=1, max_value=3) - 1 )
N = st.number_input('How many teams got the question right?', min_value=1, max_value=968)

# Calculator-Output section
def calculate_w(n, N, i):
    # Calculate the exponential term
    exp_term = math.exp(n / 35)
    
    # Calculate the maximum term
    max_term = max(5.5 - math.floor(math.log(N)), 2)
    
    # Calculate the final result
    result = (0.9 ** i) * (exp_term + max_term)
  
    return result
score = calculate_w(n, N, i) # Guess what it does

# Easter Egg that I'm exposing
if score > 8.218: 
  if random.randint(0, 1) == 0:
    st.balloons()
  else:
    st.snow()

# I wanted to get away from the questions 😔
def color(i):
  if i == 0:
    return 'normal'
  elif i == 1:
    return 'off'
  else:
    return 'inverse'

# Outputs calculation result with context
st.write(f'Solving question {n} in {i + 1} tries earns', score, 'points')
# Outputs calculation result with context (again) coz it's fun
st.metric(label=(f"Question {n}"), value=score, delta=(f'{i + 1} ATMP'),
    delta_color=(color(i)))

# Explanation of formula/calculation
st.subheader('Miscellaneous')
st.write('The formula used for the scoring of each problem (according to https://opho.physoly.tech/static/files/rules23u.pdf):')
st.latex(r'''w(n, N) = (0.9)^i\left[ \exp\left(\frac{n}{35}\right) + \max\left(5.5 - \lfloor \ln N \rfloor, 2\right) \right]''')
st.write("'where  i ∈ {0, 1, 2}  (represents whether a team got it on the first try, second try, or third try). Additionally,  N  represents the number of teams that got the question right, and  n  represents the question number (in this regard, expect all questions to be ordered by difficulty).'")
st.caption('The above explanation is quoted directly from the document.')