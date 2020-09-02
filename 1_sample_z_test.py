import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample Z Test ")
#population mean
u_0=st.number_input("Enter hypothesize mean, μ0 ")

# sample size n
n=st.number_input("Enter sample size, n value")

# sample mean x_bar
x_bar=st.number_input("Enter sample mean,  x̄ value")

# Standard deviation sigma
sigma=st.number_input("Enter standard deviation, σ value ")

# significance_level
significance_level=st.number_input("Enter Significance level, α value")

#---------------------Hypothesis test start---------------
ho = st.selectbox("H0 : μ : ", ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ha : μ : ",
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

    st.write("Ho:(u)  " + ho + f"  {u_0}")
    st.write("Ho:(u)  " + ha + f"  {u_0}")
    # st.write("z = (x̄ – μ) / (σ / √n)")
    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------

    z = (x_bar - u_0) / ((sigma) / math.sqrt(n))
    z=round(z,6)
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/hypothesis%20test%2Fone_sample_z_test_statistic.png?alt=media&token=99e80e38-aad9-4d3c-b17c-a1e622769aa0")
    st.write("Test Statistic z is: ", z)
    # ---------------Test Statistic end ------------------

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(round(float(z),2) / np.sqrt(2))), 4)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(z) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from Z End-------------

        # Rejection Region for 2 tail
        if (hypo_test(ho, ha) == "Two_tail"):
                z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
                st.write(f"Zc < {z_critical}" if z < 0 else f"Zc  >{abs(z_critical)}")

                # st.write("z test statistic  is :", (z))
                st.write("Decision through p value : ")
                st.write("p value =  ", abs(p_two_tailed))
                st.write(f"since p value is < {significance_level}")
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
            st.write(f"p_left < {significance_level}")
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
            st.write(f"p_right > {significance_level}")
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