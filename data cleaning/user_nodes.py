import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Function to read the CSV file into a DataFrame
def read_csv():
    # read the user_nodes.csv file using pandas library and return it
    df = pd.read_csv('user_nodes.csv')
    return df

'''
**Check the null values**
The function check_null_values() reads a DataFrame from read_csv  function which returns data in the user_nodes csv file and 
the it needs to  calculates the sum of null (missing) values for each column in the DataFrame.

It then returns a Series containing the count of null values for each column in the DataFrame. 
This provides insights into the presence and extent of missing data in the dataset after duplicates have been dropped.


'''
# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    return null_values

'''
**Find the Duplicate Values**
Here, We need to check for duplicate values in a dataset  for each column.

Finally, the counts of duplicated values are returned as a integer. This information can be useful in identifying duplicate data and deciding on appropriate strategies to deal with them, 
such as imputation or deletion.
'''

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    return duplicates

'''
**Remove the Duplicate Values**
The function drop_duplicates() reads a DataFrame from a CSV file, removes any duplicate rows in the DataFrame, and returns the cleaned DataFrame without duplicates.

'''


# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace = True)
    return df


'''
The provided function, `data_cleaning()`, aims to enhance the quality and structure of a given DataFrame. It starts by removing duplicate rows to ensure data consistency. 
Subsequently, the function eliminates the columns "has_loan" and "is_act" from the DataFrame, streamlining it for analysis. 
To improve clarity, column names are adjusted: 'id_' becomes 'consumer_id', 'area_id_' is transformed to 'region_id', 'node_id_' is changed to 'node_id', 
'act_date' is renamed to 'start_date', and 'deact_date' is converted to 'end_date'. 
The final step involves exporting the cleaned DataFrame to a CSV file named 'user_nodes_cleaned.csv', without including the index column. 
Upon completion, the function returns the cleaned DataFrame, now prepared for further analysis.
'''

def data_cleaning():

    df = drop_duplicates()

    # Step 3: Drop specified columns from the DataFrame("has_loan", "is_act")
    df.drop(['has_loan', 'is_act'], inplace = True, axis = 1)
    #Rename columns names id_,area_id_,node_id_,act_date',deact_date to  consumer_id,region_id,node_id,start_date,end_date
    df.rename(columns = {'id_' : 'consumer_id',
                         'area_id_' : 'region_id',
                         'node_id_' : 'node_id',
                         'act_date' : 'start_date',
                         'deact_date' : 'end_date'
    }, inplace = True)

    #df.to_csv('user_nodes_cleaned.csv', index=False)
    df.to_csv('user_nodes_cleaned.csv', index = False)
    return df
