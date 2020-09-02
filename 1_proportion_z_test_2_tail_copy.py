import math
import streamlit as st
import scipy.stats
import numpy as np
import scipy.special as scsp

P0=st.number_input("Enter P0",min_value=0.01)#0.625
n=st.number_input("Enter  N :",min_value=0.01)#70
x=st.number_input("Enter  X :",min_value=0.01)#30


significance_level=st.number_input("Enter  Significance value :")#0.01
#---------------------Hypothesis test start---------------
ho = st.selectbox(
            "Ho:(p)  P0 : ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ho:(p)  P0 : ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")



# print(hypo_test(ho,ha))



#---------------------Hypothesis test end---------------
#


# --------------------------Rejection Region Start---------------------------------
def rejection_region():
    p_cap = x / n

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

    st.write("Ho:(p) : " + ho + f" : {P0}")
    st.write("Ho:(p) : " + ha + f" : {P0}")

    # --------------------Test Statistic Start--------------------
    z = round((p_cap - P0) / math.sqrt(P0 * (1 - P0) / n),4)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/one%20proportion%2F1_Proportion_Z_Test_test_statistic.png?alt=media&token=e29e2157-9329-4633-8a72-3254174029ec")
    st.write("z statistic is", z)

    # --------------------Test Statistic End--------------------

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))), 6)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(z) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from Z End-------------

    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        z_critical = ((round(scipy.stats.norm.ppf(1 - significance_level / 2), 6)))
        st.write(f"Zc < {z_critical}" if z < 0 else f"Zc  >{abs(z_critical)}")

        # st.write("z test statistic  is :", (z))
        st.write("Decision through p value : ")
        st.write("p value =  ", abs(round(p_two_tailed,5)))
        # st.write(f"since p value is < {significance_level}")
        st.write("""
                             Reject Ho if | Zcalculated | > Zcritical
                             And
                             p value < significance level , α

                             """)
        st.write("Decision through z statistic : ")
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

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
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

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
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z > z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")


# --------------------------Rejection Region End---------------------------------



if (st.button("calculate")):
    rejection_region()

