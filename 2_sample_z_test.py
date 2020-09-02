import math
import scipy.stats
import scipy.special as scsp
import numpy as np
import streamlit as st

st.title("2 Sample Z Test")

u1,u2=0,0
diff=st.number_input("Enter difference in mean, u1- u2")#10
sigma1=st.number_input("Enter standard deviation 1, σ1 value")#50
sigma2=st.number_input("Enter standard deviation 2, σ2 value")#60
x1_bar=st.number_input("Enter sample mean 1, x̄1 value")#25
x2_bar=st.number_input("Enter sample mean 2, x̄2 value")#124
n1=st.number_input("Enter sample size 1, n1 value")#24
n2=st.number_input("Enter sample size 1, n2 value")#25
significance_level=st.number_input("Enter Significance level, α value")#0.05




#---------------------Hypothesis test start---------------
# ho="="#input("u:(p)  u_0 : ")
# ha="!="#input("u:(p)  u_0 : ")

ho = st.selectbox(
            "Ho:(p)  P0 : ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ho:(p)  P0 : ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")



def rejection_region():
    def hypo_test(ho, ha):

        if ((ho == ">=" and ha == "!=") or (ho == ">=" and ha == ">") or (ho == "<=" and ha == "!=") or (
                ho == "<=" and ha == "<")):
            return False
        elif (ha == "<"):
            return "Left_tail"
        elif (ha == ">"):
            return "Right_tail"
        else:
            return "Two_tail"

    st.write("Ho:(u) :  u1-u2  " + ho + f": {diff}")
    st.write("Ha:(u) :  u1-u2 " + ha + f" : {diff}")

    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------
    # ---------------Test Statistic start ----------------
    z = (x1_bar - x2_bar - diff) / (math.sqrt((sigma1 * sigma1) / n1 + (sigma2 * sigma2) / n2))
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/hypothesis%20test%2Ftwo_sample_z_test_statistic.png?alt=media&token=b48a5fe0-8c65-466a-9709-b91535a8d9f1")
    st.write("z statistic is",z)
    # ---------------Test Statistic end ------------------

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))), 5)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(z) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from Z End-------------

    if (hypo_test(ho, ha) == "Two_tail"):
        z_critical = ((round(scipy.stats.norm.ppf(1 - significance_level / 2),6)))
        st.write(f"Zc < {z_critical}" if z < 0 else f"Zc  >{abs(z_critical)}")

        # st.write("z test statistic  is :", (z))
        st.write("Decision through p value : ")
        st.write("p value =  ", abs(p_two_tailed))
        # st.write(f"since p value is < {significance_level}")
        st.write("""
                          Reject Ho if | Zcalculated | > Zcritical
                          And
                          p value < significance level , α

                          """)
        st.write("Decision through z statistic : ")
        # st.write(
        #     f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        z_critical = (-(scipy.stats.norm.ppf(1 - significance_level / 2)))

        st.write(f"Zc =  {z_critical}")
        # st.write("z test statistic  is  :", (z))
        st.write("Decision through p value : ")
        st.write("p value =  ", p_left)
        # st.write(f"p_left < {significance_level}")
        st.write("""
                                       Reject Ho if  Zcalculated  <  Zcritical
                                        And
                                        p value < significance level , α


                                        """)
        st.write("Decision through z statistic :")
        # st.write(
        #     f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

    # Rejection Region for right tail

    if (hypo_test(ho, ha) == "Right_tail"):
        z_critical = scipy.stats.norm.ppf(1 - significance_level)
        # if z > (scipy.stats.norm.ppf(1 - significance_level / 2)):
        #     st.write("\nRight Null hypothesis is rejected ")
        st.write(f"Zc = {z_critical}")
        # st.write("z test statistic  is : ", (z))
        st.write("Decision through p value : ")
        st.write("p value =  ", p_right)
        # st.write(f"p_right > {significance_level}")
        st.write("""
                                                       Reject Ho if  Zcalculated  >  Zcritical
                                                        And
                                                        p value < significance level , α


                                                        """)
        st.write("Decision through z statistic :")
        # st.write(
        #     f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z > z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")


if (st.button("calculate")):

    rejection_region()

# --------------------------Rejection Region End---------------------------------