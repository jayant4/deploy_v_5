import statistics
import streamlit as st
import numpy as np

st.title("Standard Deviation")

# creating a simple data - set
sample = (st.text_input("Enter Sample values separated by ' , ' or '  ' (space) example : '1,2,3' or '1 2 3 4' : "))
	#[9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4,12, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]


def std_deviation(s):
	return(statistics.stdev(s))


if (st.button("calculate")):
    new_l =list(map(float, sample.split(","))) if sample[1] == "," else list(map(float, (sample.strip().split(" "))))

    print(sample[1])
    std_dev_op=std_deviation(new_l)

    st.write(f"Sum ,∑x = {sum(new_l)} ")
    st.write(f"Mean , x̅ = {np.mean(new_l)}")
    st.write(f"Standard Deviation for sample {new_l} is = {(std_dev_op)} ")

    # f"""
    # #### Thus, if we’re conducting some type of Chi-Square test then we can compare the Chi-Square test statistic to {critical_value}. If the test statistic is greater than {critical_value}, then the results of the test are statistically significant.
    # """
