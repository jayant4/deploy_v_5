import math
import scipy.stats
import numpy as np
import streamlit as st

st.title("2 Sample T Test Equal Variance")


u1,u2=0,0
diff=st.number_input("Enter difference in mean, u1- u2")
s1=st.number_input("Enter standard deviation 1, s1 value")#50
s2=st.number_input("Enter standard deviation 2, s2 value")#60
x1_bar=st.number_input("Enter sample mean 1, x̄1 value")#25
x2_bar=st.number_input("Enter sample mean 2, x̄2 value")#124
n1=st.number_input("Enter sample size 1, n1 value")#24
n2=st.number_input("EEnter sample size 1, n2 value")#25
significance_level = st.number_input("Enter Significance level, α value")  # 0.01

#---------------------Hypothesis test start---------------
ho = st.selectbox(
            "H0 : u1- u2 ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ha : u1- u2 ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")







# st.image("https://firebasestorage.googleapis.com/v0/b/fcmfirebaseproject-50a79.appspot.com/o/profile_images%2FEnd_img.jpg?alt=media&token=77ed6ff9-eddb-47cf-9ea8-aef3ce6b2da6",width=240)








def rejecion_region():

            def hypo_test(ho,ha):

                if((ho==">=" and ha=="!=") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):
                    return False
                elif (ha=="<"):
                    return "Left_tail"
                elif (ha==">"):
                    return "Right_tail"
                else:
                    return "Two_tail"
            st.write("Ho:(u) :  u1-u2  " + ho + f": {diff}")
            st.write("Ha:(u) :  u1-u2 "  + ha + f" : {diff}")

            #---------------------Hypothesis test end---------------






            # ----------- Pooled Variance Start------------------

            s_p=(((n1-1)*(s1*s1))+((n2-1)*(s2*s2)))/(n1+n2-2)
            s_p=round(s_p,6)


            # ----------- Pooled Variance End------------------

            # ----------------------- Test Statistic Start-----------------------

            t_test=((x1_bar-x2_bar) - diff)/(math.sqrt(s_p*(1/n1 + 1/n2)))


            dof=n1+n2-2

            # ----------------------- Test Statistic End-----------------------

            # ---------------- P value start-----------
            pval = round((scipy.stats.t.sf(np.abs(t_test), dof) * 2), 4)


# ---------------- P value end-----------
# Rejection Region for 2 tail
            if (hypo_test(ho, ha) == "Two_tail"):
                p_right=round((1-pval)*2,7)
                t_critical = scipy.stats.t.ppf(1 - significance_level / 2, dof)
                st.write("Pooled Variance ")
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_pooled_varience.png?alt=media&token=9939372e-7b84-4d19-bb04-9860a641e216")
                st.write(s_p)
                st.write("Test Statistic")
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_test_statistic.png?alt=media&token=9558ff3f-d06a-4b34-a434-f6cfa77a048e")
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
                st.write(f"since p value is < {significance_level}" if p_right < significance_level else f"since p value is > {significance_level}")
                st.write(
                    f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic z calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

            # Rejection Region for left tail
            if (hypo_test(ho, ha) == "Left_tail"):
                t_critical=scipy.stats.t.ppf(significance_level,dof)
                st.write("Pooled Variance ")
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_pooled_varience.png?alt=media&token=9939372e-7b84-4d19-bb04-9860a641e216")
                st.write(s_p)
                st.write("Test Statistic")
                st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_test_statistic.png?alt=media&token=9558ff3f-d06a-4b34-a434-f6cfa77a048e")
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
            t_critical=scipy.stats.t.ppf(1-significance_level,dof)
            if (hypo_test(ho, ha) == "Right_tail"):
                st.write("Pooled Variance ")
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_pooled_varience.png?alt=media&token=9939372e-7b84-4d19-bb04-9860a641e216")
                st.write(s_p)
                st.write("Test Statistic")
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2F2%20sample%20t%20test%20equal%20variance_test_statistic.png?alt=media&token=9558ff3f-d06a-4b34-a434-f6cfa77a048e")
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

if (st.button("calculate")):
    rejecion_region()












