import math
from scipy import stats
import streamlit as st

st.title('P value from pearson R')

r=round(st.number_input(" Enter R value : "),4)
N=st.text_input(" Enter N value : ")



def calculate(r,N):
    if   r<1 or N>6:
        if not N==2:
            t =r/math.sqrt((1-r*r)/(N-2))
            p=1 - stats.t.cdf(t,N-2)
            return(p,p*2)
        else:
            return "N value 2 not valid",""
    else:
        return "N should be greater than 6 or r less than 1",""

if (st.button("calculate")):
  p_one_tail,p_two_tail= (calculate(float(r),float(N)))

  if type(p_two_tail and p_one_tail)!=str:
    st.write(" One tail probability is  ",round(p_one_tail,4))


    st.write("Two tail probability is ",round(p_two_tail,4))

  else:
      st.write(p_one_tail)

# print(calculate(0.1,4))