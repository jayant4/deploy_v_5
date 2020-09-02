import math
import scipy.stats
import pandas as pd
import re
import numpy as np
import streamlit as st


st.title("T Test for Mean Value of Difference")


x=(st.text_input(" Enter Sample values of x  separated by ' , ' or '  ' (space) example : '1,2,3' or '1 2 3 4' : "))
y=(st.text_input(" Enter Sample values of y separated by ' , ' or '  ' (space) example : '1,2,3' or '1 2 3 4' :  "))
n=(st.number_input(" Enter number of rows : "))
ud=(st.text_input(" Enter μ0 ",value=0))
difference = []
ho = st.selectbox(
            "H0   μd : ",
            ('=', '≥', '≤'))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ha μd : ",
            ('≠', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")
significance_level=st.number_input("Enter Significance level, α value")#significance_level=0.01
#0.1




def rejecion_region(x_col,y_col):

            zip_object = zip(x_col, y_col)

            for list1_i, list2_i in zip_object:
                difference.append(list1_i-list2_i)

            sumation_d=sum(difference)


            d_bar=np.mean(difference)


            d_bar_square = [d*d for d in difference]
            sum_d_bar_square=sum(d_bar_square)

            dict_op={"X":x_col,"Y":y_col,"d_bar : X-Y":difference,"d_bar square ":d_bar_square}

            op_df=pd.DataFrame(dict_op)
            st.write(op_df)
            st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2FT%20Test%20for%20Mean%20Value%20of%20Difference%20d%CC%85_count.png?alt=media&token=7eb38d48-2c6f-4598-8371-5095cb576762")
            st.write("mean of difference is: ", d_bar)
            st.write("summation of difference is : ", sumation_d)

            std_dev=math.sqrt((((sum_d_bar_square)-((abs(sumation_d*sumation_d))/n))/(n-1)))
            #np.std(difference)
            st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2FT%20Test%20for%20Mean%20Value%20of%20Difference%20d%CC%85_standerd_deviation.png?alt=media&token=86618e6f-7b51-43f1-8397-c6aa59d6eaf0")
            st.write("standard deviation is : ",std_dev)


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


            # st.write(hypo_test(ho,ha))

            st.write("Ho(μd)  " + ho + f"  {ud}")
            st.write("Ho(μd)  " + ha + f"  {ud}")

            # ---------------------Hypothesis test end---------------

            # --------------------Test Statistic Start--------------------
            t=(d_bar-float(ud))/(std_dev/math.sqrt(float(n)))
            # st.write(round(t,4))

            # --------------------Test Statistic End--------------------

            # ---------------- P value start-----------
            df=int(n)-1


            p_two_tailed= (1 - (scipy.stats.t.cdf((t),df)))*2
            p_right=1 - scipy.stats.t.cdf((t),df)
            p_left=scipy.stats.t.cdf(t,df)
            # st.write(p_two_tailed)
            # ---------------- P value end-----------
# Rejection Region for 2 tail
            if (hypo_test(ho, ha) == "Two_tail"):
                p_right = round(p_two_tailed, 7)
                t_critical = scipy.stats.t.ppf(1 - significance_level / 2, df)
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2FT%20Test%20for%20Mean%20Value%20of%20Difference%20d%CC%85_test_statistic.png?alt=media&token=7d4bee60-4770-4bdb-bb86-c5e8be5ae7d1")
                st.write("t test statistic  is :", round(t, 6))
                st.write(f"Degree of Freedom is df = n-1 = {df}")
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
                    f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t < t_critical else f"since test statistic z calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

            # Rejection Region for left tail
            if (hypo_test(ho, ha) == "Left_tail"):
                t_critical = scipy.stats.t.ppf(significance_level, df)
                st.image(
                    "https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2FT%20Test%20for%20Mean%20Value%20of%20Difference%20d%CC%85_test_statistic.png?alt=media&token=7d4bee60-4770-4bdb-bb86-c5e8be5ae7d1")
                st.write("t test statistic  is :", round(t, 6))
                st.write(f"Degree of Freedom is df = n-1 = {df}")
                st.write("t test critical  is :", round(t_critical, 6))
                st.write("p_value is : ", p_left)
                st.write("Decision through t statistic :")

                st.write("""
                               Reject Ho if  tcalculated  <  tcritical
                                And
                                p value < significance level , α


                                """)
                st.write(f"p_left < {significance_level}")
                st.write("Decision through p value : ")
                st.write(
                    f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t < t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

            # Rejection Region for right tail
            t_critical = scipy.stats.t.ppf(1 - significance_level, df)
            if (hypo_test(ho, ha) == "Right_tail"):
                st.image("https://firebasestorage.googleapis.com/v0/b/statics-82d7e.appspot.com/o/two%20sample%2FT%20Test%20for%20Mean%20Value%20of%20Difference%20d%CC%85_test_statistic.png?alt=media&token=7d4bee60-4770-4bdb-bb86-c5e8be5ae7d1")
                st.write("t test statistic  is :", round(t, 6))
                st.write(f"Degree of Freedom is df = n-1 = {df}")
                st.write("t test critical  is :", round(t_critical, 6))
                st.write("p_value is : ", round(p_right, 7))
                st.write("Decision through t statistic :")
                st.write("Decision through p value : ")
                st.write("Reject Ho if tcalculated > tcritical")
                st.write(f"p_right > {significance_level}")
                st.write(
                    f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t > t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

                st.write("""
                                                                  Reject Ho if  tcalculated  >  tcritical
                                                                   And
                                                                   p value < significance level , α


                                                                   """)
# x_index=(x.index(" ") if " " in x else x.index(",") )




if " " in x:
    x=x.strip().split()
    x=",".join(x)
if " " in y:
    y=y.strip().split()
    y=",".join(y)



if (st.button("calculate")):
    
  
    try:
        # if   not (len(x.strip()) == len(y.strip())):
        #         raise ValueError
        x_col = list(map(float, x.split(","))) if x[x.index(',')] == "," else list(map(float, x.strip().split(" ")))
        y_col = list(map(float, y.split(","))) if y[y.index(',')] == "," else list(map(float, y.strip().split(" ")))
        rejecion_region(x_col,y_col)

    except IndexError:
        st.write("enter atleast 3 value")
    except ValueError:
        st.write("number of x and y values should be same")






# st.write(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed>significance_level else f"since  p-value > {significance_level} therefore reject ")








# x val :  11.2,25.1,14,1.1,2.5,65.4
# y val 11.2,25.1,14,1.1,2.5,65.4