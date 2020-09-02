import math
import scipy.stats
import streamlit as st

st.title("2 Sample T Confidence Interval")

sigma1=st.number_input("Enter standard deviation 1, s1 value") #sigma1=50
sigma2=st.number_input("Enter standard deviation 2, s2 value") #sigma2=60
x1_bar=st.number_input("Enter sample mean 1, x̄1 value") #x1bar=123.2
n1=st.number_input("Enter sample size 1, n1 value") #n1=58
n2=st.number_input("Enter sample size 2, n2 value") #n2=48
x2_bar=st.number_input("Enter sample mean 2, x̄2 value") #x2bar=173

significance_level=st.number_input("Enter Significance level, α value") #0.05

def degree_of_freedom(s1,s2,n1,n2):
    op_numerator=(((s1*s1)/n1)+((s2*s2)/n2))**2

    op_denom=((1/(n1-1))*((s1*s1)/n1)**2)+((1/(n2-1))*((s2*s2)/n2)**2)

    return(op_numerator/op_denom)
def calculate():
    lhs=x1_bar-x2_bar
    dof = degree_of_freedom(sigma1, sigma2, n1, n2)
    st.write("Degree of Freedom df  is = ", round(degree_of_freedom(sigma1, sigma2, n1, n2), 7))
    st.markdown(r'''
           $$df = \frac{\frac{s_{1}^{2}}{n_1}+\frac{s_{_2}^{2}}{n_2}}{\frac{\frac{s_{1}^{2}}{n_1}}{n_1-1}+ \frac{\frac{s_{2}^{2}}{n_2}}{n_2-1}}$$
           ''')


    rhs=(scipy.stats.t.ppf(1-significance_level/2,dof))*(math.sqrt((sigma1*sigma1)/n1+(sigma2*sigma2)/n2))
    confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
    confidence_level = (1 - significance_level) * 100
    st.write("confidence level =", confidence_level)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/confidence%2F2_sample_t_confidential_interval_confidence_interval.png?alt=media&token=a329863c-d1e8-4387-83ea-47df8db1f414")
    st.write(confidence_level_minus,confidence_level_plus)
    st.write(f"Lower bound : {confidence_level_minus}")
    st.write(f"Upper bound : {confidence_level_plus}")
if (st.button("calculate")):
        calculate()
