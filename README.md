# Capstone_1
# Project Question/Goal

# Background + Motivation
go with purpose: if the us had public health like Canada, Aus, NZ, would we have done better with managing the pandemic?

# Description Raw Data
show list of columns & datatype --> so that way can show what I paired it down to
(might take away more columns again)
link to sources for data, how many data points (rows) etc

# Exploratory Data Analysis

After creating cleaned dataframes for each country's COVID-19 data, I started exploring the data by looking at  daily case incidence. I created a bar plot function to plot the daily case counts over the past ten months of the pandemic. I plotted each country separately at first:  
  
|                              |                                  |
| ---------------------------- | -------------------------------- |
|![](images/us_daily_cases.png)|![](images/canada_daily_cases.png)|
|                              |                                  |
|![](images/aus_daily_cases.png)|![](images/nz_daily_cases.png)   |

Upon initial analysis of the y-axis (number of COVID-19 cases) it was clear the United States has an overwhelmingly larger amount of COVID-19 cases compared to Canada, Australia and New Zealand. I then wanted to see how the countries compared to each other. I plotted all four together, but due to the United States' highest daily count around 80,000 cases it was hard to see the other three countries data. 

![](images/four_merge_daily_cases.png)  

**Fig 2: Comparing COVID-19 Daily Case Incidence: Comparing United States, Canada, Australia + New Zealand daily incidence of COVID-19 cases; major ticks are beginning and end of each month, minor ticks are the 15th of each month.**

To be able to better compare the four countries, I created a new column in my merged dataframe with the value of daily cases per 100,000 people in each country. This column is the total number of daily cases divided by the country's population over 100,000. As you can see below, with the new proportional data we can see more of each county's results; however, the United States is still far worse off on handling the pandemic compared to Canada, Australia and New Zealand. 

![](images/four_merge_daily_proportional.png)  

**Fig 3: Proportionally Comparing COVID-19 Daily Case Incidence: Comparing United States, Canada, Australia + New Zealand daily incidence of COVID-19 cases per 100,000 people; major ticks are beginning and end of each month, minor ticks are the 15th of each month.**





use this to go through question thought process to see how you got to final question/goal or hypothesis

# Analysis
discuss cleaning pipeline and scripts (try to put this into OOP, need if name main block)
discuss creating new database files of the cleaned data
**doing any stats?

# Future Steps

# References