'''Initial Data Munging + Creating Usable Data Sets: Helper Functions'''

import pandas as pd 

#read in data files
def create_dataframe_csv(file):
    '''Input: file - filepath'''
    return pd.read_csv(file)

#drop columns not needed
def drop_columns(df, cols):
    '''Inputs: df - new dataframe just read in
               cols - list of columns to drop (list of strings)'''
    df.drop(cols, axis=1, inplace=True)
    return df

#get rid of NaN values for numeric data
def fill_nan(df):
    '''Input: df - dataframe with dropped columns'''
    df.fillna(value=0, axis=1, inplace=True)
    return df

#change date column data to datetime type
def change_to_datetime(df, date_col):
    '''Inputs: df - dataframe with dropped columns and NaNs replaced
               date_col - string name of date column in df'''
    df[date_col] = pd.to_datetime(df[date_col])
    return df

#rename columns
def rename_columns(df, new_cols):
    '''Inputs: df - newly imported dataframe
              new_cols - dictionary of new column names'''
    df.rename(columns = new_cols, inplace=True)
    return df

#drop header rows if imported as data rows
def drop_header_rows(df, row_lst):
    '''Inputs: df - newly imported dataframe
              row_lst - list of row indicies to drop that are header info and not data'''
    df.drop(row_lst, axis=0, inplace=True)
    return df

#reset index of dataframe rows
def reset_index_df(df):
    '''Input: df - dataframe with recently removed rows/columns that needs to be re-indexed'''
    df.reset_index(drop=True, inplace=True)
    return df

#groupby to create new dataframe
def groupby_df_sum(df, groupby_col):
    '''Inputs: df - current dataframe
               groupby_col - the column to groupby
               agg - aggregator to use'''
    new_df = df.groupby(groupby_col).sum().reset_index()
    return new_df

#create new dataframe based on column value
def new_df_column_value(df, col, col_val):
    '''Inputs: df - current dataframe
               col - column name to groupby
               col_val - column value to find true'''
    new_df = df[df[col] == col_val]
    return new_df

#create new csv data file from cleaned up dataframes
def df_to_csv(df, file):
    '''Inputs: df - cleaned up dataframe
               file - file path for new data file'''
    df.to_csv(file, index=True)

#sort dataframe by date column
def sort_df_by_date(df, date_col):
    '''Inputs: df - current dataframe
               date_col - date column to sort by'''
    return df.sort_values(by=[date_col])

#change data type to float for columns that should be numeric
def datatype_float(df, col_lst):
    '''Inputs: df - current dataframe
               col_lst - list of columns that need to be change'''
    for col in col_lst:
        df[col] = df[col].astype(float)
    return df
