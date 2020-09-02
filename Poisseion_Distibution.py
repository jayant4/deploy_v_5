from  scipy import stats
import scipy
import streamlit as st

st.title('Calculate Poisson Distribution')
# p=λ
p = float((st.number_input("   Enter Average rate of success  λ   ")) ) # 0.5
x = float(st.number_input("   Enter Poisson random variable (x)	: "))  # 10

if (st.button("calculate")):
  try:
    st.write(f"""
    Poisson Probability: P(X = x)	 : {round(scipy.stats.distributions.poisson.pmf(x, p),7)}\n
    Cumulative Probability: P(X < x) : {round(scipy.stats.distributions.poisson.cdf(x, p)-scipy.stats.distributions.poisson.pmf(x, p),7)}\n
    Cumulative Probability: P(X ≤ x): {round(scipy.stats.distributions.poisson.cdf(x, p),7)}\n
    Poisson Probability: P(X > x)	 : {round(scipy.stats.distributions.poisson.sf(x, p),7)}\n
    Poisson Probability: P(X ≥ x)	 : {round(scipy.stats.distributions.poisson.sf(x, p)+scipy.stats.distributions.poisson.pmf(x, p),7)}\n
     """)
  except :
      st.write("enter some values")