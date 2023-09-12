import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# Function to read the CSV file into a DataFrame
def read_csv():
    # read the user_transactions.csv file using pandas library and return it
    df = pd.read_csv('user_transactions.csv')
    return df

'''
Check the null values
The function check_null_values() reads a DataFrame from read_csv  function which returns data in the user_transactions csv file 
and the it needs to  calculates the sum of null (missing) values for each column in the DataFrame.
'''

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    return null_values

'''
Find the Duplicate Values
Here, We need to check for duplicate values in a dataset  for each column.

Finally, the counts of duplicated values are returned as a integer. 
This information can be useful in identifying duplicate data and deciding on appropriate strategies to deal with them, such as imputation or deletion.
'''

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    return duplicates

'''
Remove the Duplicate Values
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
Data Cleaning:
The function data_cleaning() is designed to enhance a DataFrame's quality by removing specific columns and renaming others, preparing the data for analysis. 

Initially, duplicate rows are removed and any rows with null values are dropped. Then, the columns "has_credit_card" and "account_type" are selected for removal to streamline the dataset for analysis.

The DataFrame's columns are updated by renaming 'id_' to 'consumer_id', 't_date' to 'transaction_date', 't_type' to 'transaction_type', and 't_amt' to 'transaction_amount' for improved clarity and interpretation.

Once these steps are completed, the cleaned DataFrame is saved as 'user_transaction_cleaned.csv' without the index column and returned for further analysis.
'''

def data_cleaning():
    """
    Data Cleaning Function:
    Cleans the DataFrame by dropping specified columns and renaming others.

    Returns:
    DataFrame: The cleaned DataFrame after dropping and renaming columns.
    """
    # Step 1: Get the DataFrame with duplicate rows removed and rows with null values dropped
    df = drop_duplicates()

    # Step 2: Columns to remove from the DataFrame
    #columns needs to be removed "has_credit_card" and  "account_type"
    
    # Drop specified columns from the DataFrame
    df.drop(['has_credit_card', 'account_type'], axis = 1, inplace = True)
    
    #Rename columns id_,t_date,t_type,t_amt to consumer_id,transaction_date,transaction_type,transaction_amount
   
    # Step 5: Rename columns using the new column names
    df.rename(columns = {'id_' : 'consumer_id',
                         't_date' : 'transaction_date',
                         't_type' : 'transaction_type',
                         't_amt' : 'transaction_amount'
    }, inplace = True)

    #df.to_csv('user_transaction_cleaned.csv', index=False)
    df.to_csv("user_transaction_cleaned.csv", index = False)
    return df

