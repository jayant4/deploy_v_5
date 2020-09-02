from scipy import stats
import scipy
import streamlit as st

st.title('Calculate Binomial Distribution')


n = ((st.text_input(" Enter Number of trials(n) : ")) ) # 10
p = ((st.text_input("   Enter Probability of success on a single trial p (0.0 to 1.0) : ")) ) # 0.5
x = (st.text_input("   Enter Number of successes (x)	 : "))  # 3


if (st.button("calculate")):
 try:
    n=float(n)
    p=float(p)
    x=float(x)
    st.write(f"""
        Binomial probability   P(X = x) : {round(scipy.stats.binom.pmf(x,n,p),7)}\n
        Cumulative probability P(X < x) : {round(scipy.stats.binom.cdf(x,n,p)-scipy.stats.binom.pmf(x,n,p),7)}\n
        Cumulative probability P(X ≤ x) : {round(scipy.stats.binom.cdf(x,n,p),7)}\n
        Cumulative probability P(X > x) : {round(scipy.stats.binom.sf(x,n,p),7)}\n
        Cumulative probability P(X ≥ x) : {round(scipy.stats.binom.sf(x,n,p)+scipy.stats.binom.pmf(x,n,p),7)}\n
   """)
 except:
  st.write("enter some values")
