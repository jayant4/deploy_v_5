import streamlit as st

import numpy as np
import scipy.special as scsp

st.title('P value from Z score')


z_value_input=st.text_input(" Enter z value : ")


def main(z):
    """From z-score return p-value."""
    left=0.5 * (1 + scsp.erf(float(z) / np.sqrt(2)))
    right =1-left

    if float(z)<0:
        two_tailed=2*left
    else:
        two_tailed=2*right

    return (round(left,4),round(right,4),round(two_tailed,4))


if (st.button("calculate")):
  left,rigt,two_tail= main((z_value_input))
  st.write("left is ",rigt)
  st.write("two tail is ",two_tail)



