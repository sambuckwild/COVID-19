# Comparing the COVID-19 Pandemic Between Countries With and Without Universal Public Healthcare 

![](images/coronavirus_image_thin.jpg)  
[source](https://www.nga.org/coronavirus/)

## Project Questions
-  Did Canada, Australia and New Zealand manage the pandemic better than the United States? 
-  If the United States had universal public healthcare and a better pandemic plan/public health system like Canada, Australia, and New Zealand, would the United States have done better with managing the pandemic?   
 

## Background + Motivation   

SARS-CoV-2 (COVID-19) is a viral infectious disease that has caused a global pandemic all of 2020. It is thought to have originated in China, and then spread to almost every country in the world. This pandemic has shown a light on the need for better public health infrastructure and planning. I chose to compare the United States to Canada, Australia, and New Zealand because of the main differences in these country's approaches to handling the pandemic and in their healthcare systems.<br>  

Canada, Australia and New Zealand all have universal healthcare coverage and they all were prepared with updated pandemic plans and guidelines inplace if a public health emergency were to occur. A major part of their plans that helped with the response was identifying the large need for primary care providers in a public health crisis. Comparatively, the United States does not have universal healthcare--meaning not every one could go to the doctor for suspicion of having the infection until the government passed an order making it free for everyone--and they did have a National Council set up with an updated plan in 2017 for a pandemic response but the council was disbanded in 2018 leaving the United States at risk if a pandemic were to occur. [References 1 & 2](#references) <br>  

I wanted to explore the daily case numbers and deaths between the four countries to determine if the United States was truly at a higher risk from the COVID-19 pandemic. 

## Raw Data + Data Cleaning  


#### Initial Data   

The initial data for all four countries was obtained from multiple sources, then cleaned into new datasets and two merged datasets. The initial datasets contained daily case numbers, daily deaths, and information about the state/province, testing numbers (for some countries), and number of people recovered from infection. Initial data cleaning was dropping uneeded columns, renaming columns, filling NaN values, and setting the dates to datetime objects.  

| **United States Data** | **Canada Data** | **Australia Data** | **New Zealand Data** |
| :------------------: | :-----------: |:--------------: | :----------------: |
| 15 Columns             |  31 Columns     | 17 Columns         | 10 Columns           |
| 16681 Rows             | 3418 Rows       | 277 Rows           |  4886 Rows           |
| Split up by States by Date | Split up by Province By Date  | Split up by Date| Split up by Region by Date|
| Retained 10 coulmns in cleaned dataframe|Retained 11 columns|Retained all 17 columns|Retained all 10 columns|
| [United States data source](https://data.cdc.gov/Case-Surveillance/United-States-COVID-19-Cases-and-Deaths-by-State-o/9mfq-cb36)| [Canada data source](https://open.canada.ca/data/en/dataset/261c32ab-4cfd-4f81-9dea-7b64065690dc)   |  [Australia data source](https://github.com/M3IT/COVID-19_Data/blob/master/Data/COVID_AU_national.csv)  | [New Zealand data source](https://nzcoviddashboard.esr.cri.nz/#!/)|  

<font size ="-1">*Table 1: Features + sources for original datasets*</font><br><br>  


#### Cleaned + Merged Dataframe: Daily COVID-19 Cases    

The date and daily cases column from each country's cleaned dataframe was selected and renamed as I merged each dataframe together. An outer join was used so as not to miss any data from countries that started tracking cases earlier than others, thus had more dates listed compared to others. The weighted (proportional) columns were calculated with the daily cases column divided by the country's population divided by 100,000 so it is now a value of daily cases per 100,000 people in that country.

|    | Date    | Aus_Daily_Cases | NZ_Daily_Cases | Canada_Daily_Cases | US_Daily_Totals | Aus_Daily_prop | NZ_Daily_prop | Canada_Daily_prop | US_Daily_prop |
|----|---------|-----------------|----------------|--------------------|-----------------|----------------|---------------|-------------------|---------------|
| 50 | 3/12/20 | 30              | 1              | 38                 | 414             | 0.117647594    | 0.020737281   | 0.100683178       | 0.125074527   |
| 51 | 3/13/20 | 41              | 1              | 38                 | 267             | 0.160785045    | 0.020737281   | 0.100683178       | 0.080664007   |
| 52 | 3/14/20 | 51              | 1              | 20                 | 338             | 0.20000091     | 0.020737281   | 0.052991146       | 0.102113986   |
| 53 | 3/15/20 | 48              | 1              | 54                 | 1237            | 0.18823615     | 0.020737281   | 0.143076095       | 0.373713019   |
| 54 | 3/16/20 | 79              | 7              | 88                 | 755             | 0.309805331    | 0.145160966   | 0.233161043       | 0.22809485    |
| 55 | 3/17/20 | 78              | 11             | 99                 | 2797            | 0.305883744    | 0.228110089   | 0.262306174       | 0.845008338   |   

<font size ="-1">*Table 2: Five rows from cleaned + merged dataframe with country daily cases and weighted daily COVID-19 cases*</font><br><br>  


#### Cleaned + Merged Dataframe: Daily Deaths due to COVID-19    

Similar to the daily cases dataframe, this was a merge of the cleaned countries' dataframes on their daily death count columns along with a weighted daily death column using the country's population divided by 100,000.

|    | Date    | Aus_Daily_Deaths | NZ_Daily_Deaths | Canada_Daily_Deaths | US_Daily_Deaths | Aus_Daily_prop | NZ_Daily_prop | Canada_Daily_prop | US_Daily_prop |
|----|---------|------------------|-----------------|---------------------|-----------------|----------------|---------------|-------------------|---------------|
| 50 | 3/12/20 | 0                | 0               | 0                   | 5               | 0              | 0             | 0                 | 0.001510562   |
| 51 | 3/13/20 | 1                | 0               | 0                   | 6               | 0.003921586    | 0             | 0                 | 0.001812674   |
| 52 | 3/14/20 | 0                | 0               | 0                   | 4               | 0              | 0             | 0                 | 0.00120845    |
| 53 | 3/15/20 | 2                | 0               | 0                   | 16              | 0.007843173    | 0             | 0                 | 0.004833798   |
| 54 | 3/16/20 | 0                | 0               | 3                   | 8               | 0              | 0             | 0.007948672       | 0.002416899   |
| 55 | 3/17/20 | 0                | 0               | 3                   | 22              | 0              | 0             | 0.007948672       | 0.006646472   |   

<font size ="-1">*Table 3: Five rows from cleaned + merged dataframe with country daily deaths and weighted daily deaths due to COVID-19*</font><br><br>  


## Exploratory Data Analysis

After creating cleaned dataframes, I started exploring the data by looking at  daily case incidence of COVID-19 over the past ten months of the pandemic for each country. 
  
|                              |                                  |
| ---------------------------- | -------------------------------- |
|![](images/us_daily_cases.svg)|![](images/canada_daily_cases.svg)|
|                              |                                  |
|![](images/aus_daily_cases.svg)|![](images/nz_daily_cases.svg)   |  

<font size ="-1">*Figure 1: Daily case incidence of COVID-19 for United States, Canada, Australia, and New Zealand* </font><br><br>

Upon initial analysis of the y-axis (# of COVID-19 cases), it was clear the United States has had an overwhelmingly larger amount of COVID-19 cases compared to Canada, Australia and New Zealand.<br>   

#### Comparison of Daily COVID-19 Cases  

To better visualize the direct comparisons, I plotted the four countries together. Due to the United States' highest daily count around 80,000 cases, however, it was hard to see the other three countries' data on the plot. 

![](images/four_merge_daily_cases.svg)   
<font size ="-1">*Figure 2: Comparing United States, Canada, Australia + New Zealand daily incidence of COVID-19 cases; major ticks are beginning and end of each month, minor ticks are the 15th of each month.*</font><br>

To be able to better compare the four countries, I created a new column in my merged dataframe with the value of daily cases per 100,000 people in each country (a weighted daily cases value). Shown below, with the new proportional data we can see more of each county's results; however, the United States is still far worse off on handling the pandemic compared to Canada, Australia and New Zealand. 

![](images/four_merge_daily_proportional.svg)   
<font size ="-1">*Figure 3: Comparing United States, Canada, Australia + New Zealand daily incidence of COVID-19 cases per 100,000 people; major ticks are beginning and end of each month, minor ticks are the 15th of each month.* </font><br><br>

#### Comparison of Daily Deaths due to COVID-19  

Next, I wanted to compare the deaths due to COVID-19 in the four countries. Again, I created a merged dataframe with proportional columns of daily deaths per 100,000 people for each country.  

![](images/four_merge_daily_death_proportional.svg)   
<font size ="-1">*Figure 4: Comparing United States, Canada, Australia + New Zealand daily death count due to COVID-19 per 100,000 people; major ticks are beginning and end of each month, minor ticks are the 15th of each month.* </font><br><br>

Based on the plots, the daily number of deaths was more comparable at the first wave of the pandemic between at least the US and Canada; however, the US appears to have had more deaths proportionally compared to the other three countries. This is shown in the following two tables that illustrate the total number of COVID-19 cases and deaths for each country, along with the weighted total for each country.  

<div align="center">  

| **Country**        | **Total # COVID-19 Cases** | **Total # COVID-19 Cases per 100,000 people**|
| :----------------: | :------------------------: | :------------------------------------------: |
|   United States    |          8,617,022         |                     2603.3                   |
|       Canada       |            203,688         |                      539.7                   |
|     Australia      |             27,527         |                      107.9                   |
|    New Zealand     |              1,154         |                       23.9                   |
<br>  
<div align="left">  

<div align="center">  

| **Country**        | **Total # COVID-19 Deaths** | **Total # COVID-19 Deaths per 100,000 people**|
| :----------------: | :------------------------: | :------------------------------------------: |
|   United States    |          224601        |                     67.85                  |
|       Canada       |            9793       |                      25.95                  |
|     Australia      |             905         |                      3.55                  |
|    New Zealand     |              22        |                       0.46                  |
<br>  
<div align="left">  

## Analysis
 
I performed a hypothesis test to determine whether someone is more likely to die from a COVID-19 infection in the United States compared to "x" country.   

>  H<sub>0</sub> : Probability of dying due to COVID-19 in US &le; Probability of dying due to COVID-19 in "x" country  
> H<sub>a</sub> : Probability of dying due to COVID-19 in US > Probability of dying due to COVID-19 in "x" country<br>  

Due to the p-values from each test with &alpha; = 0.10, I was not able to reject the null hypothesis; thus, I could not conclude that there is a significant difference in the probability of dying due to COVID-19 between the United States and Canada, Australia, or New Zealand.   
> p-value for H<sub>0</sub> US Probability &le; Canada Probability: 0.997   
> p-value for H<sub>0</sub> US Probability &le; Australia Probability: 0.603   
> p-value for H<sub>0</sub> US Probability &le; New Zealand Probability: 0.388    

Even though the plot made it look like the death rate was much worse in the United States, this conclusion makes sense when you look at the proportional frequency of death for each country as they are very close to each other.

| **Country**        | **Frequency of Death due to COVID-19 per 100,000 people** | **Total # Deaths due to COVID-19 per 100,000 people [through 10/26/20]**| **Total # COVID-19 Cases per 100,000 [through 10/12/2020]** |
| :----------------: | :------------------------: | :------------------------------------------: | :--------: |
|   United States    |          0.029        |                     67.85                   |    2352.7     |
|       Canada       |           0.054     |                      25.95                |        484.4  |
|     Australia      |             0.033        |                     3.55                    |   107.0  |
|    New Zealand     |              0.019       |                     0.46                    |     23.9    |
<br>   

> Note: For this analysis I created a third merged dataframe for daily COVID-19 cases with the last two weeks of data removed, before the total # cases was summed. This is due to research suggesting a common time frame from diagnosis (case reported) to death is about 6-12 days. So to be more accurate, the last 14 days of positive cases was removed as those would not have related to any deaths reported.<br>   

[References #3](#reference-list) 



## Future Steps   

Future analysis could be:   
-  Hypothesis test comparing the probability of getting infected with COVID-19 in the United States compared to the other countries   
- Compare demographics from each country to see which age group/sex/ethnicity etc. are more likely to contract COVID-19 or die from a COVID-19 infection   
- Determine which country had the most expenditures relating to the pandemic   
-  Re-analyze the daily case rate spikes/distributions compared to government orders such as stay-at-home, social distancing measures, travel bans, etc. 

## Reference List   

1. [COVID-19 and primary care in six countries](https://bjgpopen.org/content/bjgpoa/early/2020/09/08/bjgpopen20X101128.full.pdf)  

2. [Public Health's Critical Role in Health Reform in the United States](https://www.apha.org/policies-and-advocacy/public-health-policy-statements/policy-database/2014/07/23/11/50/public-healths-critical-role-in-health-reform-in-the-united-states)   

3. [Time between Symptom Onset, Hospitalisation and Recovery or Death: a Statistical Analysis of Different Time-Delay Distributions in Belgian COVID-19 Patients](https://www.medrxiv.org/content/10.1101/2020.07.18.20156307v1)