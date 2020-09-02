import math
import streamlit as st
import scipy.stats

# sample size n
st.title("1 Sample T interval ")
n = st.number_input("Enter sample size, n value") #n=80
# sample mean x_bar
x_bar=st.number_input("Enter sample mean,  x̄ value") #50
# x = st.number_input("Enter x value")  # 30

# Standard deviation sigma

sigma = st.number_input("Enter standard deviation, s value") #sigma=60

significance_level = st.number_input("Enter Significance level, α value")  # significance_level=0.05
# degree_of_freedom
degree_of_freedom=n-1

def calculate():
    t_critcal=scipy.stats.t.ppf(1-significance_level/2,degree_of_freedom)
    t_critcal=round(t_critcal,6)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/confidence%2F1_sample_t_inteval_critical_value.png?alt=media&token=3459cd1c-775b-4bcc-bb68-a09c04070354")
    st.write("t_(α/2),df=",round(t_critcal,6))

    confidence_level =(1-significance_level)*100
    st.write("confidence level =",confidence_level)

    confidence_interval_minus,confidence_interval_plus=x_bar-t_critcal*sigma/math.sqrt(n),x_bar+t_critcal*sigma/math.sqrt(n)
    confidence_interval_minus, confidence_interval_plus=round(confidence_interval_minus,6),round(confidence_interval_plus,6)
    st.write("x̅  ±t(α/2),df  × s/√n =",(confidence_interval_minus,confidence_interval_plus))

    st.write(f"lower bound : {confidence_interval_minus}")
    st.write(f"upper bound : {confidence_interval_plus}")

if (st.button("calculate")):

    calculate()