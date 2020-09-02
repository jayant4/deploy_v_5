#p-value
from scipy.stats import chi2
import streamlit as st

st.title('P value from Chi Square Test')

ddof=(st.text_input(" Enter Degrees of freedom : "))
alpha=(st.text_input(" Enter Chi-square score "))

def main(alpha,ddof):
    return  (1-chi2.cdf(alpha,ddof))


if (st.button("calculate")):
  p_value= main(float(alpha),float(ddof))
  st.write("P value is ",round(p_value,4))



# print('p-value:',p_value)
# print('Significance level: ',alpha)
# print('Degree of Freedom: ',ddof)
# print('p-value:',p_value)

# print((main(0.2,5)))