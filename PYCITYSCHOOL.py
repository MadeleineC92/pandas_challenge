#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd
from pathlib import Path
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = Path(r"C:\Users\Maddy\Desktop\UNI\Homework\Weekly Homework\Assignment-week4\pandas_challenge\pycityschools\Resources/schools_complete.csv")
student_data_to_load = Path(r"C:\Users\Maddy\Desktop\UNI\Homework\Weekly Homework\Assignment-week4\pandas_challenge\pycityschools\Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
data = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])

#Define Data Frame 
df = pd.DataFrame(data)

#Total numbers of schools
school_count= len(df['school_name'].unique())


#total number of students -
student_count= len(data["School ID"])


#Total Budget - SUM BUDGET 
budget= df['budget'].unique().sum()


#Avearge Maths score SUM MATHS SCORE / COUNT STUDENT NAME 
maths_average = df['maths_score'].mean()


#Average Reading score READING SCORE / COUNT STUDENT NAME 
reading_average = df['reading_score'].mean()
reading_average

#Percentage of students with passing maths above 50 
#this is showing the rows that are over 50 
passing_maths_score=data.loc[(data["maths_score"]>= 50)]
total_maths=passing_maths_score["maths_score"].sum()


#find how many students passed maths 
student_maths=data.loc[(data["maths_score"]>= 50)].count()["year"]

#PERCENTAGE = PASSING_MATHS_SCORE / PASSING_MATHS_COUNT
percentage_maths = total_maths/student_count


#Percentage of students with passing reading above 50
#this is showing the rows that are over 50 
passing_reading_score=data.loc[(data["reading_score"]>= 50)]
total_reading=passing_reading_score["reading_score"].sum()


#find how many students passed maths 
student_reading=data.loc[(data["reading_score"]>= 50)].count()["year"]

#PERCENTAGE = PASSING_MATHS_SCORE / PASSING_MATHS_COUNT
percentage_reading = total_reading/student_count


#find how many students passed reading and reading 
student_total=data.loc[(data["reading_score"]>=50) & (data["maths_score"]>= 50)].count()["year"]


#PERCENTAGE = PASSING_READING_SCORE / PASSING_READING_COUNT 
passing_total=passing_maths_score["maths_score"].sum() & passing_reading_score["reading_score"].sum()


#Percentage of students with passing maths and reading (overal passing) - pass = to 50 of more
overall_percentage = passing_total/student_count




# In[ ]:


##Local Government Area Summary
    *Caculate Total Number of Schools - Total Schools
    *Caculate Total Number of Students - Total Students
    *Caculate Total Budget - Budget
    *Caculate Average Maths Score - Maths Average 
    *Caculate Average Reading Score - Reading Average 
    *Caculate Percentage Maths Score -Overall pass (50+)- Percentage Maths
    *Caculate Percentage Reading Score -Overall pass (50+)- Percentage Reading
    *Caculate Percentage Maths & Reading Score -Overall pass (50+)- Overall Percentage 


# In[2]:


area_summary=pd.DataFrame({"Total Schools":[school_count,],
                   "Total Students":[student_count],
                   "Total Budget":[budget],
                   "Average Maths Score":[round(maths_average,2)],
                   "Average Reading Score":[round(reading_average,2)],
                   "Passing Math %":[round( percentage_maths,2)],
                   "Passing Reading %":[round(percentage_reading,2)],
                   "Passing Reading & Math %":[round(overall_percentage,2)]})

area_summary["Total Budget"]=area_summary["Total Budget"].map("${:,.0f}".format)


area_summary


# In[ ]:


## School Summary

* Create an overview table that summarises key metrics about each school, including:
  * School Name -name
  * School Type -school_type
  * Total Students-size
  * Total School Budget - school_budget
  * Per Student Budget -budget_per_student
  * Average Maths Score -aver_maths
  * Average Reading Score -aver_read
  * % Passing Maths -percentage_school_maths
  * % Passing Reading -percentage_school_reading
  * % Overall Passing (The percentage of students that passed maths **and** reading.)-percentage_overall
  
* Create a dataframe to hold the above results


# In[3]:


#School Name,type,size and budget - All data
name=school_data.set_index(["School ID"])

#school Name 
school_group = data.groupby(["school_name"])

#type - Group by so it doesn't come in different lines
school_type =school_group["type"].first()


#Total Students -SIZE
size=school_data.set_index(["school_name"])["size"]


#school budget 
school_budget=school_data.set_index(["school_name"])["budget"]


#average of school budget
averaschool = data.groupby(["school_name"])["budget"].mean()/size


#Average Math score 
#groupby name and then fine average for each school 
aver_maths=data[data["maths_score"] >= 50].groupby(["school_name"])["maths_score"].mean() 


#average reading score 
aver_read=data[data["reading_score"] >= 50].groupby(["school_name"])["reading_score"].mean()


#groupby to find how many students pass maths 
passingmathsum = data[data["maths_score"] >= 50].groupby(["school_name"])["maths_score"].sum() 


passingmathcount = data[data["maths_score"] >= 50].groupby(["school_name"])["maths_score"].count()

percentage_school_maths = passingmathsum/size


passingreadingsum = data[data["maths_score"] >= 50].groupby(["school_name"])["reading_score"].sum() 


passingreadingcount = data[data["maths_score"] >= 50].groupby(["school_name"])["reading_score"].count()

percentage_school_reading = passingreadingsum/size


#groupby to find how many students pass maths and reading together and the total amount
passingMathReadingsum = data[data["maths_score"] >= 50].groupby(["school_name"])["maths_score"].sum() & data[data["reading_score"] >= 50].groupby(["school_name"])["reading_score"].sum()


#group by school to find out the count of how many people passed reading and maths 
passingMathReadingcount = data[data["maths_score"] >= 50].groupby(["school_name"])["maths_score"].count() & data[data["reading_score"] >= 50].groupby(["school_name"])["reading_score"].count()


percentage_overall = passingMathReadingsum /size

#show in datafram and format
per_school_summary=pd.DataFrame({"School Type":school_type,
                   "Total Students":size,
                   "Total School Budget $":school_budget,
                   "Per Student Budget $":averaschool,                
                   "Average Maths Score":aver_maths,
                   "Average Reading Score":aver_read,
                   "Passing Math %":percentage_school_maths,
                   "Passing Reading %":percentage_school_reading,
                   "Passing Overall %":percentage_overall})

#formating my dataframe 






per_school_summary


# In[ ]:


## Top Performing Schools (By % Overall Passing)
#* Sort and display the top five performing schools by % overall passing.


# In[4]:


#sort by %overall passing in descending order display .head(5)
top_schools=per_school_summary.sort_values(["Passing Overall %"],ascending=False)
top_schools.head(5)


# In[ ]:


## Bottom Performing Schools (By % Overall Passing)
#* Sort and display the five worst-performing schools by % overall passing.


# In[5]:


#sort by %overall passing in ascending order display .head(5)
bottom_schools = per_school_summary.sort_values(["Passing Overall %"],ascending=True)
bottom_schools.head(5) 


# In[ ]:


## Maths Scores by Year
* Create a table that lists the average maths score for students of each year level (9, 10, 11, 12) at each school.
  * Create a pandas series for each year. Hint: use a conditional statement.
  * Group each series by school
  * Combine the series into a dataframe
  * Optional: give the displayed data cleaner formatting


# In[6]:


#define and filter data by year 
year_nine_maths = data[(data["year"] == 9)]
year_ten_maths= data[(data["year"] == 10)]
year_eleven_maths= data[(data["year"] == 11)]
year_tweleve_maths= data[(data["year"] == 12)]

#create series by score - formating change 
nine_aver_maths=year_nine_maths.groupby(["school_name"])["maths_score"].mean().map("{:,.2f}".format)
ten_aver_maths=year_ten_maths.groupby(["school_name"])["maths_score"].mean().map("{:,.2f}".format)
eleven_aver_maths=year_eleven_maths.groupby(["school_name"])["maths_score"].mean().map("{:,.2f}".format)
tweleve_aver_maths=year_tweleve_maths.groupby(["school_name"])["maths_score"].mean().map("{:,.2f}".format)

#display in datafram, re-name columns
maths_scores_by_year=pd.DataFrame({"Year 9":nine_aver_maths,
                             "Year 10":ten_aver_maths,
                             "Year 11":eleven_aver_maths,
                             "Year 12":tweleve_aver_maths})

maths_scores_by_year



# In[ ]:


## Reading Score by Year
* Create a table that lists the average maths score for students of each year level (9, 10, 11, 12) at each school.
  * Create a pandas series for each year. Hint: use a conditional statement.
  * Group each series by school
  * Combine the series into a dataframe
  * Optional: give the displayed data cleaner formatting


# In[7]:


#table that list the average reading scores for students in 9,10,11 at each school -Reading
#define and filter data by year 
year_nine_reading = data[(data["year"] == 9)]
year_ten_reading= data[(data["year"] == 10)]
year_eleven_reading= data[(data["year"] == 11)]
year_tweleve_reading= data[(data["year"] == 12)]

#create series by score - formating change 
nine_aver_reading=year_nine_reading.groupby(["school_name"])["reading_score"].mean().map("{:,.2f}".format)
ten_aver_reading=year_ten_reading.groupby(["school_name"])["reading_score"].mean().map("{:,.2f}".format)
eleven_aver_reading=year_eleven_reading.groupby(["school_name"])["reading_score"].mean().map("{:,.2f}".format)
tweleve_aver_reading=year_tweleve_reading.groupby(["school_name"])["reading_score"].mean().map("{:,.2f}".format)

#display in datafram, re-name columns
reading_score_by_year=pd.DataFrame({"Year 9":nine_aver_reading,
                             "Year 10":ten_aver_reading,
                             "Year 11":eleven_aver_reading,
                             "Year 12":tweleve_aver_reading})

reading_score_by_year


# In[ ]:


## Scores by School Spending

* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Maths Score
  * Average Reading Score
  * % Passing Maths
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


# In[8]:


#scores by school spending 

#table that breaks down school performances - average spending ranges (per studen) 
#use bins to group school spending 
#table must have 
##Average Math score, reading score - passing maths and reading results and overall passing rate (average on the passing maths and reading results)
#provided bin 
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"]
per_school_summary['bins'] = pd.cut(averaschool, spending_bins, labels = labels,right=False)
per_school_summary

spending_math_scores = per_school_summary.groupby(["bins"])["Average Maths Score"].mean().map("{:,.2f}".format)
spending_reading_scores = per_school_summary.groupby(["bins"])["Average Reading Score"].mean().map("{:,.2f}".format)
spending_passing_math = per_school_summary.groupby(["bins"])["Passing Math %"].mean().map("{:,.2f}%".format)
spending_passing_reading = per_school_summary.groupby(["bins"])["Passing Reading %"].mean().map("{:,.2f}%".format)
overall_passing_spending = per_school_summary.groupby(["bins"])["Passing Overall %"].mean().map("{:,.2f}%".format)

#create Data Fram - Spending_summary

Spending_summary=pd.DataFrame({"Average Maths Score":spending_math_scores,
                               "Average Reading Score":spending_reading_scores,
                               "Passing Math %":spending_passing_math,
                               "Passing Reading %":spending_passing_reading,
                               "Passing Overall %":overall_passing_spending})
Spending_summary


# In[ ]:


## Scores by School Size
* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Maths Score
  * Average Reading Score
  * % Passing Maths
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


# In[9]:


#scores by school Size
size_bins = [0, 1000, 2000, 5000, ]
labels = ["Small(1000)", "Medium(1000-2000)", "Large(2000-5000)"]
per_school_summary['bins'] = pd.cut(size, size_bins, labels = labels,right=False)
per_school_summary

size_math_scores = per_school_summary.groupby(["bins"])["Average Maths Score"].mean().map("{:,.2f}".format)
size_reading_scores = per_school_summary.groupby(["bins"])["Average Reading Score"].mean().map("{:,.2f}".format)
size_passing_math = per_school_summary.groupby(["bins"])["Passing Math %"].mean().map("{:,.2f}%".format)
size_passing_reading = per_school_summary.groupby(["bins"])["Passing Reading %"].mean().map("{:,.2f}%".format)
size_passing_spending = per_school_summary.groupby(["bins"])["Passing Overall %"].mean().map("{:,.2f}%".format)

size_summary=pd.DataFrame({"Average Maths Score":size_math_scores,
                               "Average Reading Score":size_reading_scores,
                               "Passing Math %":size_passing_math,
                               "Passing Reading %":size_passing_reading,
                               "Passing Overall %":size_passing_spending})
size_summary


# In[ ]:


## Scores by School Type
* Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
  * Average Maths Score
  * Average Reading Score
  * % Passing Maths
  * % Passing Reading
  * Overall Passing Rate (Average of the above two)


# In[10]:


#table that breaks down school performances - average spending ranges (per student) 
#use bins to group school spending 
#table must have 
##Average Math score, reading score - passing maths and reading results and overall passing rate (average on the passing maths and reading results)
type_math_scores = per_school_summary.groupby(["School Type"])["Average Maths Score"].mean().map("{:,.2f}".format)
type_reading_scores = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean().map("{:,.2f}".format)
type_passing_math = per_school_summary.groupby(["School Type"])["Passing Math %"].mean().map("{:,.2f}%".format)
type_passing_reading = per_school_summary.groupby(["School Type"])["Passing Reading %"].mean().map("{:,.2f}%".format)
type_passing_spending = per_school_summary.groupby(["School Type"])["Passing Overall %"].mean().map("{:,.2f}%".format)

type_summary=pd.DataFrame({"Average Maths Score":type_math_scores,
                               "Average Reading Score":type_reading_scores,
                               "Passing Math %":type_passing_math,
                               "Passing Reading %":type_passing_reading,
                               "Passing Overall %":type_passing_spending})
type_summary


# In[ ]:




