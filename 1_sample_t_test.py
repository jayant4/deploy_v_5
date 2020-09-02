import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample T Test ")
#population mean
u_0=st.number_input("Enter hypothesize mean, μ0") #u0=100
# sample size n
n=st.number_input("Enter sample size, n value") #n=100
# sample mean x_bar
x_bar=st.number_input("Enter sample mean,  x̄ value") #x_bar= 110
# Standard deviation sigma
sigma=st.number_input("Enter standard deviation, s value") #sigma=40
# significance_level
significance_level=st.number_input("Enter significance_level value  α  ")#significance_level=0.01

# degrees_of_freedom
dof=n-1

#---------------------Hypothesis test start---------------
ho = st.selectbox(
            "H0 : μ: ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ha : μ ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")



# --------------------------Rejection Region Start---------------------------------
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

    st.write("Ho:(u) : " + ho + f" : {u_0}")
    st.write("Ha:(u) : " + ha + f" : {u_0}")
    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------

    t_test = round((x_bar - u_0) / ((sigma) / math.sqrt(n)),6)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/hypothesis%20test%2Fone_sample_t_test_statistic.png?alt=media&token=9e07fd99-d0c0-42d7-a6b6-f746c5d6dd92")
    st.write("Test Statistic t is: ", t_test)
    st.write(f"Degree of freedom = df= n-1 = {dof}")
    # ---------------Test Statistic end ------------------

    # ----------------P value from T Start-------------
    # p_left = round(0.5 * (1 + scsp.erf(float(t) / np.sqrt(2))), 4)
    # p_right = 1 - p_left
    # p_two_tailed = 1
    # if float(t) < 0:
    #     p_two_tailed = 2 * p_left
    # else:
    #     p_two_tailed = 2 * p_right
    pval = round((scipy.stats.t.sf(np.abs(t_test), dof) * 2), 4)
    # #----------------P value from T End-------------





    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        p_right = round((1 - pval) * 2, 7)
        t_critical = scipy.stats.t.ppf(1 - significance_level / 2, dof)
        st.write("t test statistic  is :", round(t_test, 6))
        st.write(f"DOF {dof}")
        st.write("t test critical  is :", round(t_critical, 6))
        st.write("Decision through T statistic : ")
        st.write("p_value is : ", p_right)

        st.write("""
                   Reject Ho if | tcalculated | > tcritical
                   And
                   p value < significance level , α

                   """)
        st.write("Decision through p value : ")
        st.write(
            f"since p value is < {significance_level}" if p_right < significance_level else f"since p value is > {significance_level}")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic z calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

        # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        t_critical = scipy.stats.t.ppf(significance_level, dof)
        st.write("t test statistic  is :", round(t_test, 6))
        st.write(f"DOF {dof}")
        st.write("t test critical  is :", round(t_critical, 6))
        st.write("p_value is : ", pval)
        st.write("Decision through t statistic :")

        st.write("""
                                  Reject Ho if  tcalculated  <  tcritical
                                   And
                                   p value < significance level , α


                                   """)
        st.write(f"p_left < {significance_level}")
        st.write("Decision through p value : ")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

        # Rejection Region for right tail
    t_critical = scipy.stats.t.ppf(1 - significance_level, dof)
    if (hypo_test(ho, ha) == "Right_tail"):
        st.write("t test statistic  is :", round(t_test, 6))
        st.write(f"DOF {dof}")
        st.write("t test critical  is :", round(t_critical, 6))
        st.write("p_value is : ", round(1 - pval, 7))
        st.write("Decision through t statistic :")
        st.write("Decision through p value : ")
        st.write("Reject Ho if tcalculated > tcritical")
        st.write(f"p_right > {significance_level}")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test > t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("""
                                                  Reject Ho if  tcalculated  >  tcritical
                                                   And
                                                   p value < significance level , α


                                                   """)


# --------------------------Rejection Region End---------------------------------


if (st.button("calculate")):
    rejection_region()