import streamlit as st

st.title("Degree of freedom of Two sample T Test ")

s1=st.number_input("Enter standard deviation s1 Value ")#50
s2=st.number_input("Enter standard deviation s2 Value ")#60
n1=st.number_input("Enter sample size n1 value ")#24
n2=st.number_input("Enter sample size n2 value") #25

def calculate():
    def degree_of_freedom(s1,s2,n1,n2):
        op_numerator=(((s1*s1)/n1)+((s2*s2)/n2))**2
         # print(op_numerator)

        op_denom=((1/(n1-1))*((s1*s1)/n1)**2)+((1/(n2-1))*((s2*s2)/n2)**2)
        return(op_numerator/op_denom)

    st.markdown(r'''
    $$df = \frac{\frac{s_{1}^{2}}{n_1}+\frac{s_{_2}^{2}}{n_2}}{\frac{\frac{s_{1}^{2}}{n_1}}{n_1-1}+ \frac{\frac{s_{2}^{2}}{n_2}}{n_2-1}}$$
    ''')

    st.write("Degree of Freedom df  is = ",round(degree_of_freedom(s1,s2,n1,n2),7))

if (st.button("calculate")):
        try:
            calculate()
        except :
            st.write("enter some values")

