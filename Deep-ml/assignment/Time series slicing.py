#https://www.scaler.com/academy/mentee-dashboard/class/417085/assignment/problems/27544?navref=cl_tt_nv

import pandas as pd
import temperatures

#temperatures is the given dataframe consisting of columns {date: (datetime format, 'yyyy-mm-dd'), temp: (float)}

# Set date as the index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

print("The average temperature within the given days in years 2010 and 2011 is:", end = " ")

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011 and retrieve only the mean of temperatures from that subset
avg_10_11 = temperatures_ind.loc["2010":"2011", "temp"].mean()
print(round(avg_10_11, 2))

print("The average temperature within the given days between 2010-08 and 2011-02 is:", end = " ")

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011 and retrieve only the mean of temperatures from that subset
avg_aug_feb = temperatures_ind.loc["2010-08":"2011-02", "temp"].mean()
print(round(avg_aug_feb, 2))