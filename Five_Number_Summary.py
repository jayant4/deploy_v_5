# calculate a 5-number summary
from numpy import percentile
import streamlit as st

st.title('Calculate Five Number Summary ')

data = (st.text_input(" Enter Sample values separated by ' , ' or '  ' (space) example : '1,2,3' or '1 2 3 4' : "))
    #[1,3,2,6,8,9,10,5]
# calculate quartiles

def calculate(new_l):
    quartiles = percentile(new_l, [25, 50, 75])
    # calculate min/max
    data_min, data_max = min(new_l),max(new_l)
    # print 5-number summary
    st.write(f"""
    Min:  {data_min} \n
    Q1: {quartiles[0]} \n 
    Median:  {quartiles[1]}\n
    Q3:  {quartiles[2]}\n
    Max:  {data_max}\n
    """)

if (st.button("calculate")):
    if " " in data:
        data = data.strip().split()
        data = ",".join(data)

    try:
        assert len(data) >5
        new_l = list(map(float, data.split(",")))
        st.write(tuple(sorted(new_l)))
        calculate(sorted(new_l))


    except :st.write("please enter atleast 5 values")






