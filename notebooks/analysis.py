'''Code for analysis of data'''
from data_munging import *
from plotting import *

import scipy.stats as stats
import numpy as np








if __name__ == '__main__':
    '''daily case stats for table display in readme'''
    #total covid cases overall + proportionally
    us_total = covid_merge['US_Daily_Totals'].sum()
    us_total_prop = covid_merge['US_Daily_prop'].sum()
    can_total = covid_merge['Canada_Daily_Cases'].sum()
    can_total_prop = covid_merge['Canada_Daily_prop'].sum()
    aus_total = covid_merge['Aus_Daily_Cases'].sum()
    aus_total_prop = covid_merge['Aus_Daily_prop'].sum()
    nz_total = covid_merge['NZ_Daily_Cases'].sum()
    nz_total_prop = covid_merge['NZ_Daily_prop'].sum()
    #print(us_total, us_total_prop, can_total, can_total_prop,aus_total, aus_total_prop,nz_total, nz_total_prop)

    #total covid deaths overall + proportionally
    us_total_death = deaths_merge['US_Daily_Deaths'].sum()
    us_total_prop_death = deaths_merge['US_Daily_prop'].sum()
    can_total_death = deaths_merge['Canada_Daily_Deaths'].sum()
    can_total_prop_death = deaths_merge['Canada_Daily_prop'].sum()
    aus_total_death = deaths_merge['Aus_Daily_Deaths'].sum()
    aus_total_prop_death = deaths_merge['Aus_Daily_prop'].sum()
    nz_total_death = deaths_merge['NZ_Daily_Deaths'].sum()
    nz_total_prop_death = deaths_merge['NZ_Daily_prop'].sum()
    # print(us_total_death, us_total_prop_death, can_total_death,can_total_prop_death,aus_total_death, 
    # aus_total_prop_death,nz_total_death, nz_total_prop_death)

    '''hypothesis testing: H0 - no difference in mean daily death between four countries
    # Ha - US mean is > other countries' means'''
    #calculate mean daily number of cases per 100,000 people
    us_mean_prop = np.mean(covid_merge['US_Daily_prop'])
    can_mean_prop = np.mean(covid_merge['Canada_Daily_prop'])
    aus_mean_prop = np.mean(covid_merge['Aus_Daily_prop'])
    nz_mean_prop = np.mean(covid_merge['NZ_Daily_prop'])

    #total number in the sample = all countries' populations
    sample_total = int((us_pop + aus_pop + can_pop + nz_pop)*100000)
    us_sample = 144293207 #number of tests
    can_sample = canada_covid_total['numtested'].sum()
    aus_sample = aus_covid['tests'].sum()
    nz_sample = 1075827 
    #calculate sample variances
    us_var = np.var(covid_merge['US_Daily_prop'])
    can_var = np.var(covid_merge['Canada_Daily_prop'])
    aus_var = np.var(covid_merge['Aus_Daily_prop'])
    nz_var = np.var(covid_merge['NZ_Daily_prop'])
    #distribution sample minus population
    us_norm_dist = stats.norm(0, np.sqrt(us_var/us_sample))
    can_norm_dist = stats.norm(0, np.sqrt(can_var/can_sample))
    aus_norm_dist = stats.norm(0, np.sqrt(aus_var/aus_sample))
    nz_norm_dist = stats.norm(0, np.sqrt(nz_var/nz_sample))