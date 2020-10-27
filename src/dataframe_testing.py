'''Code to create clean datasets'''
from data_munging import *


'''USA Data'''
us_file_case_death = '../data/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv'
us_file_demo_tests = '../data/COVID-19_Case_Surveillance_Public_Use_Data.csv'
us_case_drop_cols = ['pnew_case', 'pnew_death','created_at','consent_cases', 'consent_deaths']
us_demo_drop_cols = ['onset_dt', 'medcond_yn', 'pos_spec_dt']
us_case_date_col = 'submission_date'
us_demo_date_col = 'cdc_report_dt'
us_demo_new_col = {'Race and ethnicity (combined)': 'race_ethnicity'}
us_groupby_col = 'submission_date'
us_total_file = '../data/us_covid_totals.csv'

#create first us covid dataframe
us_covid = create_dataframe_csv(us_file_case_death)
us_covid = drop_columns(us_covid, us_case_drop_cols)
us_covid = change_to_datetime(us_covid, us_case_date_col)
us_covid = fill_nan(us_covid)

#create us covid demographic dataframe
us_covid_demo = create_dataframe_csv(us_file_demo_tests)
us_covid_demo = drop_columns(us_covid_demo, us_demo_drop_cols)
us_covid_demo = change_to_datetime(us_covid_demo, us_demo_date_col)
us_covid_demo = fill_nan(us_covid_demo)
us_covid_demo = rename_columns(us_covid_demo, us_demo_new_col)

#create revised us covid dataframe with totals from all states for each day & save to new csv file
us_covid_total = groupby_df_sum(us_covid, us_groupby_col)
us_covid_total = sort_df_by_date(us_covid_total, us_case_date_col)
df_to_csv(us_covid_total, us_total_file)

'''Colorado Data'''
state_col = 'state'
state_val = 'CO'
us_case_date_col = 'submission_date'
co_data_file = '../data/colorado_covid.csv'

#create colorado dataframe from us dataframe & save to new csv file
co_covid = new_df_column_value(us_covid, state_col, state_val)
co_covid = sort_df_by_date(co_covid, us_case_date_col)
df_to_csv(co_covid, co_data_file)


'''Canada Data'''
can_file_cases = '../data/canada-covid19.csv'
can_drop_cols = ['prnameFR', 'numtotal_last14', 'ratetotal_last14', 'numdeaths_last14',
                   'ratedeaths_last14', 'avgtotal_last7', 'avgincidence_last7', 
                   'percentdeath', 'percentactive', 'avgdeaths_last7', 'avgratedeaths_last7', 
                   'percentrecover', 'ratetested', 'numtoday', 'percentoday', 'ratetotal',
                   'ratedeaths', 'numdeathstoday', 'numtestedtoday', 'numrecoveredtoday', 
                   'rateactive', 'pruid']
can_date_col = 'date'
pr_col = 'prname'
pr_col_value = 'Canada'
can_groupby_col = 'date'
canada_total_file = '../data/canada_covid_totals.csv'

#create canada dataframe
canada_covid = create_dataframe_csv(can_file_cases)
canada_covid = drop_columns(canada_covid, can_drop_cols)
canada_covid = change_to_datetime(canada_covid, can_date_col)
canada_covid = fill_nan(canada_covid)

#create revised canada covid dataframe with totals from all states for each day & save to new csv file
canada_covid_total = new_df_column_value(canada_covid, pr_col, pr_col_value)
canada_covid_total = groupby_df_sum(canada_covid_total, can_groupby_col)
canada_covid_total = sort_df_by_date(canada_covid_total, can_date_col)
df_to_csv(canada_covid_total, canada_total_file)



'''Australia Data'''
aus_file = '../data/COVID_AU_national.csv'
aus_date_col = 'date'
aus_new_file = '../data/australia_covid.csv'

#create aus dataframe & save to new csv
aus_covid = create_dataframe_csv(aus_file)
aus_covid = change_to_datetime(aus_covid, aus_date_col)
aus_covid = fill_nan(aus_covid)
aus_covid = sort_df_by_date(aus_covid, aus_date_col)
df_to_csv(aus_covid, aus_new_file)



'''New Zealand Data'''
nz_file = '../data/overview_case_curve__202010271126.csv'
nz_new_cols = {'ESR Covid-19 Dashboard': 'Date', 'Unnamed: 1': 'Region', 'Unnamed: 2': 'Daily_conf',
                'Unnamed: 3': 'daily_prob', 'Unnamed: 4': 'daily_death', 'Unnamed: 5': 'daily_total_cases',
                'Unnamed: 6': 'cumulative_conf', 'Unnamed: 7': 'cumulative_prob', 
                'Unnamed: 8': 'cumulative_death', 'Unnamed: 9': 'cumulative_total_cases'}
nz_rows = [0,1,2,3]
nz_float_cols = ['Daily_conf','daily_prob', 'daily_death', 'daily_total_cases',
                'cumulative_conf', 'cumulative_prob', 'cumulative_death', 
                'cumulative_total_cases']
nz_date_col = 'Date'
nz_groupby_col = 'Date'
nz_new_file = '../data/newzealand_total_covid.csv' 

#create nz dataframe
nz_covid = create_dataframe_csv(nz_file)
nz_covid = rename_columns(nz_covid, nz_new_cols)
nz_covid = drop_header_rows(nz_covid, nz_rows)
nz_covid = reset_index_df(nz_covid)
nz_covid = change_to_datetime(nz_covid, nz_date_col)
nz_covid = datatype_float(nz_covid, nz_float_cols)

#create total nz dataframe and save to csv
nz_covid_total = groupby_df_sum(nz_covid, nz_groupby_col)
nz_covid_total = sort_df_by_date(nz_covid_total, nz_date_col)
df_to_csv(nz_covid_total, nz_new_file)

