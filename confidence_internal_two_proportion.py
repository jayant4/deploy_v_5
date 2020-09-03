import scipy.stats
import streamlit as st

import math

st.title("2 population Proportion Confidence Interval")

n1 = st.number_input("Enter sample size 1, n1 value")  # 230
n2 = st.number_input("Enter sample size 2, n2 value")  # 540
x1 = st.number_input("Enter favourable case 1, x1 value")  # 100
x2 = st.number_input("Enter favourable case 2, x2 value")  # 200
significance_level = st.number_input("Enter Significance level, α value")  # 95


def enter_decimal_places():
    decimal_places = st.selectbox("Select Critical Value To Correct Decimal Places To Calculate Confidance Interval :",
                                  (1, 2, 3, 4))
    return decimal_places


decimal_places = enter_decimal_places()


def calculate():
    st.write("SAMPLE PRAPOTION")
    p1_hat = round(x1 / n1, 4)
    st.write("p̂1 : ", p1_hat)

    p2_hat = round(x2 / n2, 4)
    st.write("p̂2 : ", p2_hat)

    significance_level_percent= (1 - (significance_level) / 100)
    # st.write("significance level :", significance_level_percent)
    confidence_level = (1 - significance_level) * 100
    st.write(f"confidence level = {int(confidence_level)}%")

    z = scipy.stats.norm.ppf(1 - significance_level / 2)
    z = round(z, decimal_places)
    st.write("CRITICAL VALUE")
    st.write("Zα/2 : ", z)
    lhs = p1_hat - p2_hat
    rhs = z * math.sqrt((p1_hat * (1 - p1_hat) / n1) + (p2_hat * (1 - p2_hat) / n2))

    confidence_interval_lhs, confidence_interval_rhs = (lhs - rhs, lhs + rhs)
    confidence_interval_lhs, confidence_interval_rhs = round(confidence_interval_lhs, 6), round(confidence_interval_rhs,
                                                                                                6)
    st.image(
        "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20proportion%2F2%20proportion%20interval.png?alt=media&token=1e8aff63-e524-41ea-9d90-433f8bf0a353")
    st.write((confidence_interval_lhs, confidence_interval_rhs))
    st.write(f"Lower bound : {confidence_interval_lhs}")
    st.write(f"Upper bound : {confidence_interval_rhs}")


if (st.button("calculate")):
    calculate()
