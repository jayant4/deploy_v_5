import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title('1 Proportion Z Test')

class _1_proportion_z_test_2_tail:

    def __init__(self):
        self.P0 = st.number_input("Enter hypothesize praportion, P0")  # 0.625
        self.n = st.number_input("Enter sample size, n value")  # 70
        self.x = st.number_input("Enter favourable cases, x value")  # 30
        self.significance_level = st.number_input("Enter Significance level,α value")  # 0.01
        self.ho = st.selectbox(
            "H0 : P ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
        self.ha = st.selectbox(
            "Ha : P ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")


    def one_prop(self):
        #---------------------Hypothesis test start---------------



        def hypo_test(ho,ha):

            if not ((ho==">=" and ha=="≠") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):


                if (ha=="<"):

                    return "Left_tail"
                if (ha==">"):

                    return "Right_tail"
                else:

                    return "Two_tail"
            else:
                st.write("not valid")
                return False

        # print(hypo_test(ho,ha))

        st.write("Ho:(p) : " + self.ho + f" : {self.P0}")
        st.write("Ho:(p) : " + self.ha + f" : {self.P0}")

        #---------------------Hypothesis test end---------------



        # --------- -----------------Rejection Region Start---------------------------------
        def rejection_region():
            p_left = round(0.5 * (1 + scsp.erf(round(float(self.z), 2) / np.sqrt(2))), 4)
            p_right = 1 - p_left
            p_two_tailed = 1
            if float(self.z) < 0:
                p_two_tailed = 2 * p_left
            else:
                p_two_tailed = 2 * p_right
                # #----------------P value from Z End-------------

                # Rejection Region for 2 tail
                if (hypo_test(self.ho, self.ha) == "Two_tail"):
                    z_critical = ((-(scipy.stats.norm.ppf(1 - self.significance_level / 2))))
                    st.write(f"Zc < {z_critical}" if self.z < 0 else f"Zc  >{abs(z_critical)}")

                    # st.write("z test statistic  is :", (z))
                    st.write("Decision through p value : ")
                    st.write("p value =  ", abs(p_two_tailed))
                    st.write(f"since p value is < {self.significance_level}")
                    st.write("""
                                         Reject Ho if | Zcalculated | > Zcritical
                                         And
                                         p value < significance level , α

                                         """)
                    st.write("Decision through z statistic : ")
                    st.write(
                        f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if self.z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

                # Rejection Region for left tail
                if (hypo_test(self.ho, self.ha) == "Left_tail"):
                    z_critical = (-(scipy.stats.norm.ppf(1 - self.significance_level / 2)))

                    st.write(f"Zc =  {z_critical}")
                    # st.write("z test statistic  is  :", (z))
                    st.write("Decision through p value : ")
                    st.write("p value =  ", p_left)
                    st.write(f"p_left < {self.significance_level}")
                    st.write("""
                                                      Reject Ho if  Zcalculated  <  Zcritical
                                                       And
                                                       p value < significance level , α


                                                       """)
                    st.write("Decision through z statistic :")
                    st.write(
                        f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if self.z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

                # Rejection Region for right tail

                if (hypo_test(self.ho, self.ha) == "Right_tail"):
                    z_critical = scipy.stats.norm.ppf(1 - self.significance_level)
                    # if z > (scipy.stats.norm.ppf(1 - significance_level / 2)):
                    #     st.write("\nRight Null hypothesis is rejected ")
                    st.write(f"Zc = {z_critical}")
                    # st.write("z test statistic  is : ", (z))
                    st.write("Decision through p value : ")
                    st.write("p value =  ", p_right)
                    st.write(f"p_right > {self.significance_level}")
                    st.write("""
                                                                      Reject Ho if  Zcalculated  >  Zcritical
                                                                       And
                                                                       p value < significance level , α


                                                                       """)
                    st.write("Decision through z statistic :")
                    st.write(
                        f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if self.z > z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")

        rejection_region()

    # --------------------------Rejection Region End---------------------------------
x=_1_proportion_z_test_2_tail()
if (st.button("calculate")):

    x.one_prop()







