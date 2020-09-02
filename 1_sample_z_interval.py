import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample Z interval ")
n = (st.number_input("Enter sample size, n value"))#n=80
# sample mean x_bar

x_bar = st.number_input("Enter sample mean,  x̄ value")  # 30

# Standard deviation sigma
sigma = st.number_input("Enter standard deviation, σ value") #sigma=40
significance_level = st.number_input("Enter Significance level, α value")  # significance_level=0.5

def enter_decimal_places():
    decimal_places=st.selectbox("Enter number of decimal places :",(1,2,3,4))
    return decimal_places

decimal_places=enter_decimal_places()


def calculate():

    z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
    confidence_level = (1 - significance_level) * 100
    st.write("confidence level =", confidence_level)
    # Confidence interval
    z_critical=round(z_critical,decimal_places)
    c_i_minus,c_i_plus=round(x_bar-z_critical*((sigma)/(math.sqrt(n))),6),round(x_bar+z_critical*((sigma)/(math.sqrt(n))),6)
    st.write("Z(α/2) = ",z_critical)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/confidence%2F1_sample_z_inteval_confidential_interval.png?alt=media&token=1c60ba1e-3b1d-40c5-b28f-20555950d7b2")
    st.write(c_i_minus,c_i_plus)
    st.write(f"lower bound {c_i_plus}")
    st.write(f"upper bound {c_i_minus}")

if (st.button("calculate")):
    calculate()