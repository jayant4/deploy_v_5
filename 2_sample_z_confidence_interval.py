import math

import scipy.stats
import streamlit as st


st.title("2 Sample Z confidence Interval")

sigma1=st.number_input("Enter standard deviation 1, σ1 value")#50
sigma2=st.number_input("Enter standard deviation 2, σ2 value")#60
x1_bar=st.number_input("Enter sample mean 1, x̄1 value")#123.2
n1=st.number_input("Enter sample size 1, n1 value")#58
n2=st.number_input("Enter sample size 2, n2 value")#48
x2_bar=st.number_input("Enter sample mean 2, x̄2 value")#173

significance_level=st.number_input("Enter Significance level, α value")#0.05


def enter_decimal_places():
    decimal_places=st.selectbox("Enter number of decimal places :",(1,2,3,4))
    return decimal_places

decimal_places=enter_decimal_places()

def calculate():
    confidence_level = (1 - significance_level) * 100
    st.write("confidence level =", confidence_level)
    z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
    z_critical = round(z_critical, decimal_places)
    st.write("Z(α/2) = ", z_critical)

    lhs=round(x1_bar-x2_bar,6)
    rhs=(scipy.stats.norm.ppf(1-significance_level/2))*(math.sqrt((sigma1*sigma1)/n1+(sigma2*sigma2)/n2))
    rhs=round(rhs,6)
    confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/confidence%2F2_sample_z_confidential_interval_confidence_interval.png?alt=media&token=9d356db5-951d-43ee-8de7-ac9b0146b40c")
    st.write(confidence_level_minus,confidence_level_plus)
    st.write(f"Lower bound : {confidence_level_minus}")
    st.write(f"Upper bound : {confidence_level_plus}")

if (st.button("calculate")):
        calculate()