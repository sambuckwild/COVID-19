'''Initial Data Munging + Creating Usable Data Sets: Helper Functions'''

import pandas as pd 

def create_dataframe_csv(file):
    '''Input: file - filepath string
    Read in a csv file to create dataframe
    Output: dataframe'''
    return pd.read_csv(file)

def drop_columns(df, cols):
    '''Inputs: df - new dataframe just read in
               cols - list of columns to drop (list of strings)
        Drop columns we don't need in dataframe
        Output: dataframe'''
    df.drop(cols, axis=1, inplace=True)
    return df

def fill_nan(df):
    '''Input: df - dataframe with dropped columns
    Get rid of NaN values for numeric data in dataframe
    Output: dataframe'''
    df.fillna(value=0, axis=1, inplace=True)
    return df

def change_to_datetime(df, date_col, day1):
    '''Inputs: df - dataframe with dropped columns and NaNs replaced
               date_col - string name of date column in df
               day1 - argument to tell it if date string coming in has day first (day1=True or False)
        Change datatype of date collumn to datetime
        Output: dataframe'''
    df[date_col] = pd.to_datetime(df[date_col], dayfirst=day1)
    return df

def rename_columns(df, new_cols):
    '''Inputs: df - newly imported dataframe
              new_cols - dictionary of new column names
        Rename columns in dataframe
        Output: dataframe'''
    df.rename(columns = new_cols, inplace=True)
    return df

def drop_header_rows(df, row_lst):
    '''Inputs: df - newly imported dataframe
              row_lst - list of row indicies to drop that are header info and not data
        Drop the header rows in case import causes column names to be in a row instead of headers
        Output: dataframe'''
    df.drop(row_lst, axis=0, inplace=True)
    return df

def reset_index_df(df):
    '''Input: df - dataframe with recently removed rows/columns that needs to be re-indexed
    Reset the index of dataframe
    Output: dataframe'''
    df.reset_index(drop=True, inplace=True)
    return df

def groupby_df_sum(df, groupby_col):
    '''Inputs: df - current dataframe
               groupby_col - the column to groupby (column name as string)
        Groupby a column to create a new dataframe
        Output: dataframe'''
    new_df = df.groupby(groupby_col).sum().reset_index()
    return new_df

def new_df_column_value(df, col, col_val):
    '''Inputs: df - current dataframe
               col - column name to groupby (column name as string)
               col_val - column value to sort rows by into new dataframe
        Creates a new dataframe based on a specific value in a column
        Output: dataframe
        '''
    new_df = df[df[col] == col_val]
    return new_df

def sort_df_by_date(df, date_col):
    '''Inputs: df - current dataframe
               date_col - date column to sort by (string name)
        Sort dataframe by date column
        Output: dataframe'''
    return df.sort_values(by=[date_col])

def datatype_integer(df, col_lst):
    '''Inputs: df - current dataframe
               col_lst - list of columns that need to be change (list of strings)
        Change data type to integer for columns that should be numeric
        Output: dataframe'''
    for col in col_lst:
        df[col] = df[col].astype(int)
    return df

def merge_df_daily_cases(df1, df2, df1_cols, df2_cols, left_col, right_col):
    '''Inputs: df1 - left join dataframe
               df2 - right join dataframe
               df1_cols - list of columns to have in final (list of strings)
               df2_cols - list of columns to have in final (list of strings)
               left_col = column on left df to merge on (string name)
               right_col = column on right df to merge on (string name)
        Merge two dataframes keeping only specific columns in the output
        Output: Newly merged dataframe'''
    new_df = df1[df1_cols].merge(df2[df2_cols], how='outer', left_on=left_col, right_on=right_col)
    return new_df

def df_to_csv(df, file):
    '''Inputs: df - cleaned up dataframe
               file - file path for new data file (string)
        Create new csv data file of cleaned up dataframes
        Output: csv file'''
    df.to_csv(file, index=True)

if __name__ == '__main__':
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
    us_covid = change_to_datetime(us_covid, us_case_date_col, day1=False)
    us_covid = fill_nan(us_covid)

    #create us covid demographic dataframe
    us_covid_demo = create_dataframe_csv(us_file_demo_tests)
    us_covid_demo = drop_columns(us_covid_demo, us_demo_drop_cols)
    us_covid_demo = change_to_datetime(us_covid_demo, us_demo_date_col, day1=False)
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
                    'percentrecover', 'ratetested', 'percentoday', 'ratetotal',
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
    canada_covid = change_to_datetime(canada_covid, can_date_col, day1=True)
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
    aus_covid = change_to_datetime(aus_covid, aus_date_col, day1=False)
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
    nz_int_cols = ['Daily_conf','daily_prob', 'daily_death', 'daily_total_cases',
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
    nz_covid = change_to_datetime(nz_covid, nz_date_col, day1=True)
    nz_covid = datatype_integer(nz_covid, nz_int_cols)

    #create total nz dataframe and save to csv
    nz_covid_total = groupby_df_sum(nz_covid, nz_groupby_col)
    nz_covid_total = sort_df_by_date(nz_covid_total, nz_date_col)
    df_to_csv(nz_covid_total, nz_new_file)


    '''Combined Dataframe for Daily Totals & Daily Deaths'''
    nz_cols = ['Date', 'Daily_conf']
    aus_cols = ['date', 'confirmed']
    aus_nz_cols = {'date': 'Aus_Date','Date': 'NZ_Date','confirmed': 'Aus_Daily_Cases','Daily_conf': 'NZ_Daily_Cases'}
    ausnz_date_col = 'Aus_Date'
    can_cols = ['date', 'numtoday']
    ausnz_cols = ['Aus_Date', 'Aus_Daily_Cases', 'NZ_Daily_Cases']
    ausnz_can_cols = {'date': 'Canada_Date', 'numtoday': 'Canada_Daily_Cases'}
    ausnzcan_cols = ['Aus_Date', 'Aus_Daily_Cases', 'NZ_Daily_Cases', 'Canada_Daily_Cases']
    us_cols = ['submission_date', 'new_case']
    full_merge_cols = {'submission_date': 'US_Date', 'new_case': 'US_Daily_Totals'}

    #merge aus and nz first
    aus_nz_covid = merge_df_daily_cases(aus_covid, nz_covid_total, aus_cols, nz_cols, aus_date_col, nz_date_col)
    aus_nz_covid = rename_columns(aus_nz_covid, aus_nz_cols)
    aus_nz_covid = sort_df_by_date(aus_nz_covid, ausnz_date_col)
    aus_nz_covid = fill_nan(aus_nz_covid)
    aus_nz_covid = drop_columns(aus_nz_covid, ['NZ_Date'])
    #merge aus/nz with canada
    ausnz_can_covid = merge_df_daily_cases(aus_nz_covid, canada_covid_total, ausnz_cols, can_cols, ausnz_date_col, can_date_col)
    ausnz_can_covid = rename_columns(ausnz_can_covid, ausnz_can_cols)
    ausnz_can_covid = sort_df_by_date(ausnz_can_covid, ausnz_date_col)
    ausnz_can_covid = fill_nan(ausnz_can_covid)
    ausnz_can_covid = drop_columns(ausnz_can_covid, ['Canada_Date'])
    #merge aus/nz/canada with usa
    covid_merge = merge_df_daily_cases(ausnz_can_covid, us_covid_total, ausnzcan_cols, us_cols, ausnz_date_col, us_case_date_col)
    covid_merge = rename_columns(covid_merge, full_merge_cols)
    covid_merge = sort_df_by_date(covid_merge, 'US_Date').reset_index(drop=True)
    covid_merge = fill_nan(covid_merge)
    covid_merge.iloc[0:3, 0] = covid_merge.iloc[0:3, 4]
    covid_merge = drop_columns(covid_merge, ['US_Date'])
    covid_merge = rename_columns(covid_merge, {'Aus_Date': 'Date'})
    covid_merge = change_to_datetime(covid_merge, 'Date', day1=False)

   