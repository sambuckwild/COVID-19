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
from analysis import *

'''Plotting functions'''

def daily_case_bar(df, dates, daily_cases, clr, title, lbl, ax, x_label, y_label):
    '''Inputs: df - dataframe to plot
               dates - x value for bar plot, df[date_column]
               dail_cases - y value for bar plot, df[daily_counts]
               clr - color for plot (string)
               title - string of title for graph
               lbl - string for label for data on plot
               ax_ - default to one ax
               x_label = string for x label
               y_label = string for y label
        Function to create bar plot of daily covid cases
        Output: bar plot'''
    ax.bar(dates, daily_cases, color = clr, label=lbl)
    ax.set_title(title, fontsize=18)
    ax.set_ylabel(y_label, fontsize=14)
    ax.set_xlabel(x_label, fontsize=14)
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    ax.xaxis.set_minor_formatter(DateFormatter('\n%b %Y'))
    ax.tick_params(axis='x', which='major', length=17, width=1, labelsize=1)
    ax.tick_params(axis='x', which='minor', length=3, width=1, labelsize='medium')
    ax.legend()

def daily_case_bar_proportional(df, dates, daily_cases, clr, title, lbl, ax, x_label, y_label):
    '''Inputs: df - dataframe to plot
               dates - x value for bar plot, df[date_column]
               dail_cases - y value for bar plot, df[daily_counts]
               clr - color for plot (string)
               title - string of title for graph
               lbl - string for label for data on plot
               ax - default to one ax
               x_label = string for x label
               y_label = string for y label
        Function to create bar plot of daily covid cases with data proportional to location population
        Output: bar plot'''
    ax.bar(dates, daily_cases, color = clr, label=lbl)
    ax.set_title(title, fontsize=18)
    ax.set_ylabel(y_label, fontsize=14)
    ax.set_xlabel(x_label, fontsize=14)
    ax.xaxis.set_major_locator(MonthLocator())
    ax.xaxis.set_major_formatter(NullFormatter())
    ax.xaxis.set_minor_locator(MonthLocator(bymonthday=15))
    ax.xaxis.set_minor_formatter(DateFormatter('\n%b %Y'))
    ax.tick_params(axis='x', which='major', length=17, width=1, labelsize=1)
    ax.tick_params(axis='x', which='minor', length=3, width=1, labelsize='medium')
    ax.legend()

def freq_plot(c1_dist, c1_clr, c1_label, c2_dist, c2_clr, c2_label, c3_dist, c3_clr, c3_label, 
c4_dist, c4_clr, c4_label, ax, title, x_label, y_label, x):
    '''Inputs: c1_dist, c2_dist, c3_dist, c4_dist - countries' normal approximated distribution
               c1_clr, c2_clr, c3_clr, c4_clr - countries' color for line on plot (string)
               cl_label, c2_label, c3_label, c4_label - string label for country on plot
               ax - axes to put figure on
               title - string of title for plot
               x_label - string of label for x axis
               y_label - string of label for y axis
               x - numpy array to plot distributions over
        Plots a graph with all four countries' frequency distributions for comparison
        Output: plot'''
    ax.plot(x, c1_dist.pdf(x), color=c1_clr, label = c1_label, linewidth=1.5)
    ax.plot(x, c2_dist.pdf(x), color=c2_clr, label=c2_label, linewidth=1.5)
    ax.plot(x, c3_dist.pdf(x), color=c3_clr, label=c3_label, linewidth=1.5)
    ax.plot(x, c4_dist.pdf(x), color=c4_clr, label=c4_label, linewidth=1.5)
    ax.set_xlabel(x_label, fontsize=14)
    ax.set_ylabel(y_label, fontsize=14)
    ax.set_title(title, fontsize=16)
    ax.legend()


def image_of_plot(file):
    '''Input: file - file path for image (string)
        Creates a png file of a plot and saves it to images folder
        Output: png file'''
    return plt.savefig(file, transparent=False, bbox_inches='tight', format='svg', dpi=1200)

    
if __name__ == '__main__':
    '''us daily cases plot'''
    # us_plot = '../images/us_daily_cases.svg'
    # a = us_covid_total[us_case_date_col]
    # b = us_covid_total['new_case']
    # fig, ax = plt.subplots(figsize=(6,4))
    # daily_case_bar(us_covid_total, a, b, '#FBC00C', 'United States COVID-19 Daily Cases', 'United States', 
    # ax,'\nDate','# COVID-19 Cases')
    # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, ha='center')
    # image_of_plot(us_plot)

    '''canada daily cases plot'''
    # canada_plot = '../images/canada_daily_cases.svg'
    # c = canada_covid_total[can_date_col]
    # d = canada_covid_total['numtoday']
    # fig, ax = plt.subplots(figsize=(6,4))
    # daily_case_bar(canada_covid_total, c, d, '#A62205', 'Canada COVID-19 Daily Cases', 'Canada', 
    # ax,'\nDate','# COVID-19 Cases')
    # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, ha='center')
    # image_of_plot(canada_plot)

    '''australia daily cases plot'''
    # aus_plot = '../images/aus_daily_cases.svg'
    # e = aus_covid[aus_date_col]
    # f = aus_covid['confirmed']
    # fig, ax = plt.subplots(figsize=(6,4))
    # daily_case_bar(aus_covid, e, f, '#1A89F4', 'Australia COVID-19 Daily Cases', 'Australia', 
    # ax,'\nDate','# COVID-19 Cases')
    # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, ha='center')
    # image_of_plot(aus_plot)

    '''new zealand daily cases plot'''
    # nz_plot = '../images/nz_daily_cases.svg'
    # x = nz_covid_total[nz_date_col]
    # y = nz_covid_total['Daily_conf']
    # fig, ax = plt.subplots(figsize=(6,4))
    # daily_case_bar(nz_covid_total, x, y, 'black', 'New Zealand COVID-19 Daily Cases', 'New Zealand', 
    # ax,'\nDate','# COVID-19 Cases')
    # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, ha='center')
    # image_of_plot(nz_plot)

    '''colorado daily cases plot'''
    # colorado_plot = '../images/colorado_daily_cases.svg'
    # g = co_covid[us_case_date_col]
    # h = co_covid['new_case']
    # fig, ax = plt.subplots(figsize=(6,4))
    # daily_case_bar(co_covid, g, h, 'm', 'Colorado COVID-19 Daily Cases', 'Colorado', ax,
    # '\nDate','# COVID-19 Cases')
    # plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, ha='center')
    # image_of_plot(colorado_plot)

    '''plot with four countries'''
    # merge_plot_1 = '../images/four_merge_daily_cases.svg'
    # fig, ax = plt.subplots(figsize=(11, 7))
    # daily_case_bar(us_covid_total, a, b, '#FBC00C', 'Comparison of COVID-19 Daily Cases: Four Countries', 
    # 'United States', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(canada_covid_total, c, d, '#A62205', 'Comparison of COVID-19 Daily Cases: Four Countries', 
    # 'Canada', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Four Countries', 
    # 'Australia', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Four Countries', 
    # 'New Zealand', ax,'\nDate','# COVID-19 Cases')
    # image_of_plot(merge_plot_1)

    '''plot with canada, aus, nz'''
    # merge_plot_2 = '../images/three_merge_daily_cases.svg'
    # fig, ax = plt.subplots(figsize=(12,8))
    # daily_case_bar(canada_covid_total, c, d, '#A62205', 'Comparison of COVID-19 Daily Cases: Three Countries', 
    # 'Canada', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Three Countries', 
    # 'Australia', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Three Countries', 
    # 'New Zealand', ax,'\nDate','# COVID-19 Cases')
    # image_of_plot(merge_plot_2)

    '''plot with aus and nz'''
    # merge_plot_3 = '../images/two_merge_daily_cases.svg'
    # fig, ax = plt.subplots(figsize=(12,8))
    # daily_case_bar(aus_covid, e, f, '#1A89F4', 'Comparison of COVID-19 Daily Cases: Two Countries', 
    # 'Australia', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: Two Countries', 
    # 'New Zealand', ax,'\nDate','# COVID-19 Cases')
    # image_of_plot(merge_plot_3)

    '''plot with new zealand and colorado'''
    # merge_plot_4 = '../images/co_nz_merge_daily_cases.svg'
    # fig, ax = plt.subplots(figsize=(12,8))
    # daily_case_bar(co_covid, g, h, 'm', 'Comparison of COVID-19 Daily Cases: New Zealand + Colorado', 
    # 'Colorado', ax,'\nDate','# COVID-19 Cases')
    # daily_case_bar(nz_covid_total, x, y, 'black', 'Comparison of COVID-19 Daily Cases: New Zealand + Colorado',
    #  'New Zealand', ax,'\nDate','# COVID-19 Cases')
    # image_of_plot(merge_plot_4)

    '''plot with four countries + proportional data'''
    # merge_plot_5 = '../images/four_merge_daily_proportional.svg'
    # fig, ax = plt.subplots(figsize=(11, 7))
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['US_Daily_prop'], '#FBC00C', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'United States', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['Canada_Daily_prop'], '#A62205', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'Canada', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['Aus_Daily_prop'], '#1A89F4', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'Australia', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['NZ_Daily_prop'], 'black', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'New Zealand', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # image_of_plot(merge_plot_5)

    '''plot with canada, aus, nz + proportional data'''
    # merge_plot_6 = '../images/three_merge_daily_proportional.svg'
    # fig, ax = plt.subplots(figsize=(10,6))
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['Canada_Daily_prop'], 
    # '#A62205', 'Proportional Comparison of COVID-19 Daily Cases', 'Canada', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['Aus_Daily_prop'], 
    # '#1A89F4', 'Proportional Comparison of COVID-19 Daily Cases', 'Australia', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['NZ_Daily_prop'], 
    # 'black', 'Proportional Comparison of COVID-19 Daily Cases', 'New Zealand', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # image_of_plot(merge_plot_6)

    '''plot with aus and nz + proportional data'''
    # merge_plot_7 = '../images/two_merge_daily_proportional.svg'
    # fig, ax = plt.subplots(figsize=(10,6))
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['Aus_Daily_prop'], 
    # '#1A89F4', 'Proportioanl Comparison of COVID-19 Daily Cases', 'Australia', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['NZ_Daily_prop'], 
    # 'black', 'Proportional Comparison of COVID-19 Daily Cases', 'New Zealand', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # image_of_plot(merge_plot_7)

    '''plot with new zealand and colorado + proportional data'''
    # merge_plot_8 = '../images/co_nz_merge_daily_proportional.svg'
    # fig, ax = plt.subplots(figsize=(10,6))
    # daily_case_bar_proportional(co_covid, co_covid[us_case_date_col], co_covid['CO_Daily_prop'], 'm', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'Colorado', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # daily_case_bar_proportional(covid_merge, covid_merge['Date'], covid_merge['NZ_Daily_prop'], 'black', 
    # 'Proportional Comparison of COVID-19 Daily Cases', 'New Zealand', ax,'\nDate',
    # '# COVID-19 Cases per 100,000 people')
    # image_of_plot(merge_plot_8)

    '''plot with four countries daily death rate'''
    # merge_plot_9 = '../images/four_merge_daily_death_proportional.svg'
    # fig, ax = plt.subplots(figsize=(11, 7))
    # daily_case_bar_proportional(deaths_merge, deaths_merge['Date'], deaths_merge['US_Daily_prop'], 
    # '#FBC00C', 'Proportional Comparison of COVID-19 Daily Deaths', 'United States', ax,'\nDate',
    # '# COVID-19 Deaths per 100,000 people')
    # daily_case_bar_proportional(deaths_merge, deaths_merge['Date'], deaths_merge['Canada_Daily_prop'], 
    # '#A62205', 'Proportional Comparison of COVID-19 Daily Deaths', 'Canada', ax,'\nDate',
    # '# COVID-19 Deaths per 100,000 people')
    # daily_case_bar_proportional(deaths_merge, deaths_merge['Date'], deaths_merge['Aus_Daily_prop'], 
    # '#1A89F4', 'Proportional Comparison of COVID-19 Daily Deaths', 'Australia', ax,'\nDate',
    # '# COVID-19 Deaths per 100,000 people')
    # daily_case_bar_proportional(deaths_merge, deaths_merge['Date'], deaths_merge['NZ_Daily_prop'], 
    # 'black', 'Proportional Comparison of COVID-19 Daily Deaths', 'New Zealand', ax,'\nDate',
    # '# COVID-19 Deaths per 100,000 people')
    # image_of_plot(merge_plot_9)

    '''plot of four countries' frequencies of deaths per cases'''
    # freq_plot_1 = '../images/frequency_plot.svg'
    # x=np.linspace(-5, 90, num=250)
    # fig, ax = plt.subplots(figsize=(10,6))
    # freq_plot(us_norm_dist, '#FBC00C', 'United States', can_norm_dist, '#A62205', 'Canada', aus_norm_dist, 
    # '#1A89F4', 'Australia', nz_norm_dist, 'black', 'New Zealand', ax, 
    # 'Comparing Country Probability of Death due to COVID-19 Infection', 
    # '# Deaths due to COVID-19 per 100,000 people', 'Density', x=x)
    # image_of_plot(freq_plot_1)
