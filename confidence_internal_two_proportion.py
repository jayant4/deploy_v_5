import scipy.stats
import streamlit as st

import math


st.title("2 population Proportion Confidence Interval")

n1=st.number_input("Enter sample size 1, n1 value") #230
n2=st.number_input("Enter sample size 2, n2 value") #540
x1=st.number_input("Enter favourable case 1, x1 value") #100
x2=st.number_input("Enter favourable case 2, x2 value") #200
confidence_level = st.number_input("Enter Significance level, α value")  # 95


def enter_decimal_places():
    decimal_places = st.selectbox("Enter number of decimal places :", (1, 2, 3, 4))
    return decimal_places

def calculate():
    # Sample proportion
    p1_hat = round(x1 / n1,6)
    st.write("p1 hat : ", p1_hat)

    p2_hat = round(x2 / n2,6)
    st.write("p2 hat : ", p2_hat)



    decimal_places = enter_decimal_places()
    significance_level = 1 - (confidence_level) / 100

    z_critical_value = scipy.stats.norm.ppf(1 - significance_level / 2)
    z_critical_value = round(z_critical_value, decimal_places)
    lhs=p1_hat-p2_hat
    rhs=z_critical_value*math.sqrt((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2))

    confidence_interval_lhs,confidence_interval_rhs=(lhs-rhs,lhs+rhs)
    confidence_interval_lhs, confidence_interval_rhs=round(confidence_interval_lhs ,6),round(confidence_interval_rhs ,6)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20proportion%2F2%20population%20Proportion%20Confidence%20Interval_confidence_interval.png?alt=media&token=cf94acea-9677-4a3e-984f-60e9d8b0d0fb")
    st.write((confidence_interval_lhs,confidence_interval_rhs))
    st.write(f"Lower bound : {confidence_interval_lhs}")
    st.write(f"Upper bound : {confidence_interval_rhs}")
if (st.button("calculate")):
        calculate()