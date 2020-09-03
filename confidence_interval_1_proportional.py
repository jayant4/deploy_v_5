import math
import scipy.stats
import streamlit as st

st.title("Confidence Interval 1 Proportional")

n=st.number_input("Enter n Value")#70
x=st.number_input("Enter x Value")#30
significance_level=st.number_input("Enter Significance level, α value")#0.05

def enter_decimal_places():
    decimal_places=st.selectbox("Enter number of decimal places :",(1,2,3,4))
    return decimal_places

decimal_places=enter_decimal_places()

def calculate():
    p_cap = x / n

    z = scipy.stats.norm.ppf(1 - significance_level / 2)
    z=round(z,decimal_places)

    confidance_interval_left,confidance_interval_right=p_cap-z*math.sqrt(p_cap*(1-p_cap)/n),p_cap+z*math.sqrt(p_cap*(1-p_cap)/n)
    confidance_interval_left, confidance_interval_right=round(confidance_interval_left,6 ),round(confidance_interval_right,6 )
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/confidence%2F1_Proportion_Confidence_Interval_confidence_interval.png?alt=media&token=42f465d5-9c9a-44e9-881e-e1c5590bdaf8")
    st.write((confidance_interval_left, confidance_interval_right))
    st.write("Z value is : ", z )

    st.write("left  : ",confidance_interval_left)
    st.write("right : ",confidance_interval_right)

if (st.button("calculate")):
    try:
        assert n > x
        calculate()
    except :"n should be greater than x"
