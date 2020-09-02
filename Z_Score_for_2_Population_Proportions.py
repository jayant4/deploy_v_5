import math
import scipy.special as scsp
import scipy.stats
import numpy as np
import streamlit as st

st.title('Z Score For 2 Population Proportions')

n1=st.number_input("Enter sample size 1, n1 value")#230
n2=st.number_input("Enter sample size 1, n2 value")#540
x1=st.number_input("Enter favourable case 1, x1 value")#58
x2=st.number_input("Enter favourable case 2, x2 value")#58
significance_level=st.number_input("Enter Significance level, α value")#0.01


ho = st.selectbox(
            "H0 : P1 ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ha : P1",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")




def rejection_region():
    # Sample proportion
    p1_hat = x1 / n1
    # print("p1 hat : ",p1_hat)

    p2_hat = x2 / n2
    # print("p2 hat : ",p2_hat)

    # Pooled Population
    p_bar = (x1 + x2) / (n1 + n2)

    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20population%2F2%20population%20Proportion%20Z%20Test_pooled_proportion.png?alt=media&token=da6ce0ce-5701-4e1c-86d2-dc4e27aea541")
    st.write("p bar : ",round(p_bar,4))

    #
    # Hypothesis Test
    # ---------------------Hypothesis test start---------------

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

    st.write("Ho:P1  " + ho + f"  {round(p2_hat,6)}")
    st.write("Ha:P1  " + ha + f"  {round(p2_hat,6)}")

    # print(hypo_test(ho,ha))

    # ---------------------Hypothesis test end---------------
    # Test Statistic
    z = (p1_hat - p2_hat) / (math.sqrt(p_bar * (1 - p_bar) * (1 / n1 + 1 / n2)))
    st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20population%2F2%20population%20Proportion%20Z%20Test_test_statistic.png?alt=media&token=b3d2cddf-147d-4446-8d78-ec9ac9654d9c")
    print("test statistic z : ", z)

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))), 5)
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
        st.write("p value =  ", abs(round(p_two_tailed, 5)))
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