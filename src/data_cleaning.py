#The overall purpose of this script is to clean the data that is provided. The data cleaning that should take place includes standardizing column names, strip leading and trailling whitespace from product names and categories, handle missing pieces and quantities, and remove rows with clearly invalid values.

#In this step I am importing the libraries that I need. 
#I am doing this to allow for code reusability and efficiency. This is done at the top of the code so I can use it throughout the script. 
import pandas as pd



#This co-pilot function shoud import the data that I have in sales_data_raw.csv file
#In this step I am loading the data that I need into this file. 
#I am doing this so that I can use that code and clean it to serve the purpose of this project. 
def load_data(file_path: str):
    """Load the data in sales_data_clean.csv file into data_cleaning.py file"""
    data = pd.read_csv(file_path)
    return data

#Now I am going to begin applying the cleaing steps that are needed. 

#This co-pilot function should clean the column names accordingly. 
#I am going to clean the column names by making them lowercase and replacing spaces with underscores and stripping whitespace.
#I am doing this because it helps prevent errors when selecting columns.
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df=df.copy()
    df.columns=(
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )
    return df

#Now I am going to clean the text fields using co-pilot function. I am going to strip leading and trailing whitespace from product names and categories.
##Clean text fields by removing quotes and leading/trailing whitespace in prodname and category columns and date_sold columns.
#This prevents errors when filtering or grouping by these columns.
def clean_text_fields(sales_data):
    for column in ['prodname', 'category']:
        sales_data[column] = sales_data[column].str.strip().str.replace('"', '').str.replace("'", "")
        sales_data['date_sold'] = sales_data['date_sold'].str.strip().str.replace('"', '').str.replace("'", "")
    return sales_data

#Now I am going to use co-pilot to convert data types.
#Convert data types for price and qty columns to numeric.
#This is important for performing calculations and aggregations on these columns.
def convert_data_types(sales_data):
    sales_data['price'] = pd.to_numeric(sales_data['price'], errors='coerce')
    sales_data['qty'] = pd.to_numeric(sales_data['qty'], errors='coerce')
    return sales_data

#Now I am going to handle missing values using co-pilot function.
#Handle missing prices, quantities, and data sold by dropping rows with missing values in these columns.
#This is important to ensure data integrity and accuracy in analysis.
def handle_missing_values(sales_data):
    sales_data = sales_data.dropna(subset=['price', 'qty', 'date_sold'])
    return sales_data  

#Now I am going to remove rows with negative price, quantity, or duplicate rows using co-pilot function.
#Remove rows with negative price or quantity and duplicate rows.
#This is important to ensure data integrity and accuracy in analysis.
def remove_invalid_rows(sales_data):
    sales_data = sales_data[(sales_data['price'] >= 0) & (sales_data['qty'] >= 0)]
    sales_data = sales_data.drop_duplicates()
    return sales_data

#calls the function in sequence to clean the sales data 
if __name__ == "__main__":
    raw_path = "/Users/pariparmar/Documents/ ism2411-data-cleaning-copilot/data/raw/sales_data_raw.csv"
    cleaned_path = "/Users/pariparmar/Documents/ ism2411-data-cleaning-copilot/data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean= convert_data_types(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())

