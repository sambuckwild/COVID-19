'''Code for analysis of data'''
from data_munging import *
from plotting import *

import scipy.stats as stats
import numpy as np

def death_frequency(total_death, total_cases):
    '''Inputs: total_death - total # covid deaths proportional to population
               total_cases - total # covid cases proportional to population
        Calculate frequency of deaths after covid infection
        Output: float'''
    return total_death / total_cases

def shared_frequency(c1_death, c2_death, c1_cases, c2_cases):
    '''Inputs: c1_death - country 1's total death
               c2_death - country 2's total death
               c1_cases - country 1's total cases
               c2_cases - country 2's total cases
        Calculate shared frequency
        Output: float'''
    return (c1_death + c2_death) / (c1_cases + c2_cases)

def shared_std(shared_freq, c1_cases, c2_cases):
    '''Inputs: shared_freq - calculated shared frequency
            c1_cases - country 1's total cases
            c2_cases - country 2's total cases
    Calculate shared standard deviation
    Output: float'''
    return np.sqrt(((c1_cases+c2_cases)*shared_freq*(1-shared_freq))/(c1_cases*c2_cases))

def diff_frequencies(c1_freq, c2_freq):
    '''Inputs: c1_freq - first country's frequency of deaths per cases
               c2_freq - second country's frequency of deaths per cases, comparison one
        Calculates the difference in frequencies betwen two countries
        Output: float'''
    return c1_freq - c2_freq

def p_value(diff_dist, diff_freq):
    '''Inputs: diff_dist - normal distribution of difference in frequencies
               diff_freq - difference in frequencies
        Calculates the p_value between two sample frequencies
        Output: float'''
    return 1 - diff_dist.cdf(diff_freq)

def binom_approx_norm_dist(n, p):
    '''Inputs: n - country's total number cases (minus last two weeks)
               p - country's frequency of deaths per cases
        Creates a normal distribution approximation from a binomial distribution
        Output: normal distribution'''
    mean = n * p
    var = n*p*(1-p)
    return stats.norm(mean, np.sqrt(var))

if __name__ == '__main__':
    '''daily case stats for table display in readme'''
    #create data frame for hypothesis testing that doesn't have last two weeks of cases
    covid_merge_two_week = covid_merge.iloc[0:265, :]

    #total covid cases overall + proportionally
    us_total = covid_merge_two_week['US_Daily_Totals'].sum()
    us_total_prop = covid_merge_two_week['US_Daily_prop'].sum()
    can_total = covid_merge_two_week['Canada_Daily_Cases'].sum()
    can_total_prop = covid_merge_two_week['Canada_Daily_prop'].sum()
    aus_total = covid_merge_two_week['Aus_Daily_Cases'].sum()
    aus_total_prop = covid_merge_two_week['Aus_Daily_prop'].sum()
    nz_total = covid_merge_two_week['NZ_Daily_Cases'].sum()
    nz_total_prop = covid_merge_two_week['NZ_Daily_prop'].sum()
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

    '''hypothesis testing: H0 - other countries probability of death match US 
    # Ha - US mean is > other countries' probability of death after diagnosis'''
    #calculate frequency or probability of death after covid diagnosis for each country
    us_p = death_frequency(us_total_prop_death, us_total_prop)
    can_p = death_frequency(can_total_prop_death,  can_total_prop)
    aus_p = death_frequency(aus_total_prop_death, aus_total_prop)
    nz_p = death_frequency(nz_total_prop_death, nz_total_prop)
    # print(us_p, can_p, aus_p, nz_p)

    #calculate shared frequency and plot normal distribution with country US - x 
    #since the skeptic would say US <= country x
    mu = 0
    shared_p_can_us = shared_frequency(us_total_prop_death, can_total_prop_death, us_total_prop, can_total_prop)
    std_can_us = shared_std(shared_p_can_us, us_total_prop, can_total_prop)
    diff_norm_can_us = stats.norm(0, std_can_us) #normal distribution of the differences in frequencies
    shared_p_aus_us = shared_frequency(us_total_prop_death, aus_total_prop_death, us_total_prop, aus_total_prop)
    std_aus_us = shared_std(shared_p_aus_us, us_total_prop, aus_total_prop)
    diff_norm_aus_us = stats.norm(0, std_aus_us) 
    shared_p_nz_us = shared_frequency(us_total_prop_death,nz_total_prop_death, us_total_prop, nz_total_prop)
    std_nz_us = shared_std(shared_p_nz_us, us_total_prop, nz_total_prop)
    diff_norm_nz_us = stats.norm(0, std_nz_us) 

    #calculate p_value for difference in frequencies for hypothesis test
    diff_freq_can_us = diff_frequencies(us_p, can_p)
    p_value_can_us = p_value(diff_norm_can_us, diff_freq_can_us)
    diff_freq_aus_us = diff_frequencies(us_p, aus_p)
    p_value_aus_us = p_value(diff_norm_aus_us, diff_freq_aus_us)
    diff_freq_nz_us = diff_frequencies(us_p, nz_p)
    p_value_nz_us = p_value(diff_norm_nz_us, diff_freq_nz_us)
    # print(diff_freq_can_us, p_value_can_us)
    # print(diff_freq_aus_us, p_value_aus_us)
    # print(diff_freq_nz_us, p_value_can_us)

    #approximated normal distributions of frequency of deaths per cases 
    us_norm_dist = binom_approx_norm_dist(us_total_prop, us_p)
    can_norm_dist = binom_approx_norm_dist(can_total_prop, can_p)
    aus_norm_dist = binom_approx_norm_dist(aus_total_prop, aus_p)
    nz_norm_dist = binom_approx_norm_dist(nz_total_prop, nz_p)

    