import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
import datetime as dt
import folium
import matplotlib.dates as dates
from matplotlib.ticker import NullFormatter
from matplotlib.dates import MonthLocator, DateFormatter

from data_munging import *

'''Plotting functions'''

def daily_case_bar(df, dates, daily_cases, clr, title, lbl, ax):
    '''Inputs: df - dataframe to plot
               dates - x value for bar plot, df[date_column]
               dail_cases - y value for bar plot, df[daily_counts]
               clr - color for plot (string)
               title - string of title for graph
               lbl - string for label for data on plot
               ax_ - default to one ax
        Function to create bar plot of daily covid cases
        Output: bar plot'''
    ax.bar(dates, daily_cases, color = clr, label=lbl)
    ax.set_title(title, fontsize=20)
    ax.set_ylabel('Number of SARS-CoV-2 Cases', fontsize=16)
    ax.set_xlabel('\nDate', fontsize=16)
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    ax.xaxis.set_minor_formatter(DateFormatter('\n%b %Y'))
    ax.tick_params(axis='x', which='major', length=17, width=1, labelsize=1)
    ax.tick_params(axis='x', which='minor', length=3, width=1, labelsize='medium')
    ax.legend()
    
 

def image_of_plot(file):
    '''Input: file - file path for image (string)
        Creates a png file of a plot and saves it to images folder
        Output: png file'''
    return plt.savefig(file, transparent=False)

    
if __name__ == '__main__':
    #us daily cases plot
    us_plot = '../images/us_daily_cases.png'
    a = us_covid_total[us_case_date_col]
    b = us_covid_total['new_case']
    fig, ax = plt.subplots(figsize=(6,4))
    daily_case_bar(us_covid_total, a, b, '#FBC00C', 'United States COVID-19 Daily Cases', 'United States', ax)
    image_of_plot(us_plot)
    #canada daily cases plot
    canada_plot = '../images/canada_daily_cases.png'
    c = canada_covid_total[can_date_col]
    d = canada_covid_total['numtoday']
    fig, ax = plt.subplots(figsize=(6,4))
    daily_case_bar(canada_covid_total, c, d, '#A62205', 'Canada COVID-19 Daily Cases', 'Canada', ax)
    image_of_plot(canada_plot)
    #australia daily cases plot
    aus_plot = '../images/aus_daily_cases.png'
    e = aus_covid[aus_date_col]
    f = aus_covid['confirmed']
    fig, ax = plt.subplots(figsize=(6,4))
    daily_case_bar(aus_covid, e, f, '#1A89F4', 'Australia COVID-19 Daily Cases', 'Australia', ax)
    image_of_plot(aus_plot)
    #new zealand daily cases plot
    nz_plot = '../images/nz_daily_cases.png'
    x = nz_covid_total[nz_date_col]
    y = nz_covid_total['Daily_conf']
    fig, ax = plt.subplots(figsize=(6,4))
    daily_case_bar(nz_covid_total, x, y, 'black', 'New Zealand COVID-19 Daily Cases', 'New Zealand', ax)
    image_of_plot(nz_plot)
    #colorado daily cases plot
    colorado_plot = '../images/colorado_daily_cases.png'
    g = co_covid[us_case_date_col]
    h = co_covid['new_case']
    fig, ax = plt.subplots(figsize=(6,4))
    daily_case_bar(co_covid, g, h, 'm', 'Colorado COVID-19 Daily Cases', 'Colorado', ax)
    image_of_plot(colorado_plot)

    #plot with four countries
    merge_plot_1 = '../images/four_merge_daily_cases.png'
    fig, ax = plt.subplots(figsize=(12,8))
    daily_case_bar(us_covid_total, a, b, '#FBC00C', 'Comparison of COVID-19 Daily Cases: Four Countries', 'United States', ax)
    daily_case_bar(canada_covid_total, c, d, '#A62205', 'Comparison of COVID-19 Daily Cases: Four Countries', 'Canada', ax)
    daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Four Countries', 'Australia', ax)
    daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Four Countries', 'New Zealand', ax)
    image_of_plot(merge_plot_1)

    #plot with canada, aus, nz
    merge_plot_2 = '../images/three_merge_daily_cases.png'
    fig, ax = plt.subplots(figsize=(12,8))
    daily_case_bar(canada_covid_total, c, d, '#A62205', 'Comparison of COVID-19 Daily Cases: Three Countries', 'Canada', ax)
    daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Three Countries', 'Australia', ax)
    daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Three Countries', 'New Zealand', ax)
    image_of_plot(merge_plot_2)

    #plot with aus and nz
    merge_plot_3 = '../images/two_merge_daily_cases.png'
    fig, ax = plt.subplots(figsize=(12,8))
    daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Two Countries', 'Australia', ax)
    daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Two Countries', 'New Zealand', ax)
    image_of_plot(merge_plot_3)

    #plot with new zealand and colorado
    merge_plot_4 = '../images/co_nz_merge_daily_cases.png'
    fig, ax = plt.subplots(figsize=(12,8))
    daily_case_bar(co_covid, g, h, 'm', 'Comparison of COVID-19 Daily Cases: New Zealand + Colorado', 'Colorado', ax)
    daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: New Zealand + Colorado', 'New Zealand', ax)
    image_of_plot(merge_plot_4)