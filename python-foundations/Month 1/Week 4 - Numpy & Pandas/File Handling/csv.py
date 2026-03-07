from email.headerregistry import DateHeader
from tokenize import String

#To bring data in, you need to tell Pandas three things:
# Where it is,
# How it's separated, and
# What to use as headers.

# Key Parameters:
# filepath: The name or path to the file.
# sep: The character separating values (Default is ,). For Tabs, use \t.
# header: Which row contains the names? Use None if the file has no names.
# names: A list of names to use if the file doesn't have a header row.

import pandas as pd

## Basics

# pd.read_csv(filename , name= , sep etc)

# Column Handling

# sep        # column separator (default = ',')
# delimiter  # same as sep
# header     # row number to use as column names
# names      # custom column names
# usecols    # select specific columns

# Data Type Control

# dtype      # specify data types
# converters # custom conversion functions

# Row Selection
# nrows      # number of rows to read
# skiprows   # rows to skip


## How to Load file from URLs

# url = "https://website.com/data.csv"
# pd.read_csv(url)



# Medium 1: The Semicolon File
# You have a file named users.csv. The data looks like this: ID;Username;Level 101;DevGuy;5 102;DataQueen;8
# Task: Write the code to load this file correctly into a DataFrame named df_users.
df = pd.read_csv("users.csv", sep=";")

# Medium 2: The Headerless File
# You have a file named prices.txt. It has no header row: Apple, 0.50 Banana, 0.20
# Task: Load this file, tell Pandas there is no header, and name the columns Product and Price.
df2 = pd.read_csv("price.txt", sep=',', header=None, names=['Product' , 'Price'])
print(df2)

# Hard 1: The Remote Tab-Separated File
# URL: https://example.com/data.tsv Goal: Load this web file. (Hint: .tsv usually stands
# for Tab Separated Values, so think about what sep value you need).

# df3 = pd.read_csv("https://website.com/data.csv" , sep= "\t")


## Data Selection & Memory Control

# Using " usecols " , " nrows " , " dtype "

df4 = pd.read_csv(
    "huge_data.csv",
    sep=",",
    converters={
        "price": lambda x: float(x) if x != "" else None,
        "quantity": lambda x: int(x) if x != "" else None,
        "total_amount": lambda x: float(x) if x != "" else None,
    },
    usecols= ["price" , "quantity" , "total_amount"],
    nrows= 9,
    skiprows = [x for x in range(9) if x % 2 != 0 and x != 0]
)

# print(df4)

#
# Medium 1: Selective Loading
# You have a file employee_data.csv with 20 columns, including First Name, Last Name, Salary, and Department. Task: Write the code to load only the First Name and Department columns into a DataFrame.

df5 = pd.read_csv("employee_data.csv",
                  sep= ",",
                  usecols=["First_Name" , "Department"]
                  )

print(df5)

# Medium 2: The Quick Peek
# You are given a massive file "employee_data.csv" that is 5GB in size. You don't want to crash your computer. Task: Write the code to load only the first 100 rows of this file to see what the data looks like.

df6 = pd.read_csv("huge_data.csv",
                  sep = ",",
                  nrows=5
                  )
print(df6)

# Hard 1: The Type-Sensitive ID
# You are loading sales.csv. It has a column named Transaction_ID. These IDs look like 000123, 000124. Problem: If you load normally, Pandas turns them into integers (123, 124), and you lose the leading zeros. Task: Load the file so that the Transaction_ID column is forced to be a string (object). (Hint: Use the dtype={"ColumnName": "type"} dictionary syntax).

df7 = pd.read_csv("huge_data.csv",
                  sep = ",",
                  dtype = {"transaction_id" : "string" , "user_id" : "string"}
                  )
print(df7)


                                                ## Handling Messy Data

## Syntax For" na_value " and " encoding "

# na_values list contain the value that will be converted to NaN
# df = pd.read_csv(
#     "data.csv",
#     encoding="utf-8",     # Always to be written in String
#     na_values=["NA", "N/A", "", "null"]  # Cna also be     na_values={
                                                    #         "Age": ["", "NA"],
                                                    #         "Salary": ["-", "null"]
                                                    #     }
# )


# Medium 1: Cleaning the Header
# Task: Load warehouse_logs.csv so that the first two lines of text are ignored and Log_ID becomes the header.
# Medium 2: Handling Unknowns
# Task: In this file, some Quantity values are written as ???. Load the file so that these are converted to proper NaN (missing) values.
# Hard 1: The Encoding Struggle
# Task: Imagine this warehouse_logs.csv was saved on an old Windows machine and gives you a UnicodeDecodeError. Write the code to load it using the latin1 encoding while still applying the fixes from the previous two questions.

df8 = pd.read_csv("warehouse_logs.csv",
                  sep = ",",
                  skiprows= 2,
                  na_values = ["???"],
                  encoding= "latin1"
                  )

print(df8)


                                                        ## Indexing & Dates

# Syntax for index_col and parse_dates
# index_col:Specifies which column to use as the DataFrame index.
# parse_dates:Converts specified columns from strings into datetime objects while reading the file.

# pd.read_csv(
#     "file.csv",
#     index_col="ID",     # Here column name or index
#     parse_dates=["Joining_Date"]
# )

df9 = pd.read_csv("shipment_tracker.csv",
                  sep= ",",
                  index_col="Serial_Number",
                  parse_dates=["Shipment_Date"],
                  usecols=["Shipment_Date" , "Serial_Number" ,"Weight_KG"]

                  )
print(df9)


                                        ## Exporting Data (to_csv)

# Key Parameters:
# path_or_buf: The name of the file you want to create (e.g., "output.csv").
# index: (Boolean) By default, Pandas saves the index as a column. Usually, you want index=False to avoid adding an extra column of row numbers.
# columns: A list of specific columns you want to export (if you don't want to save the whole thing).
# encoding: Essential if your data contains special characters (use utf-8).

# Medium 1: Basic Save
# Task: Save df_final to a file named results.csv. Make sure it does not include the index (the User_ID) as a separate column in the file.
# Medium 2: Selective Export
# Task: You only want to share the scores. Save only the User_ID (since it's the index) and the Score columns to a file named scores_only.csv. (Hint: If you want to keep the index, set index=True).
# Hard 1: The Secure Export
# Task: Save the file final_report.csv with these rules:
#   Use a Tab (\t) as a separator instead of a comma.
# Save only the User_ID, Status, and Join_Date columns.
# Ensure it is saved with utf-8 encoding to prevent character errors.

df10 = pd.read_csv("results.csv",
                   sep = ",",
                   )

print(df10)

df10 = df10[df10["Score"] >= 80]
df10.to_csv(path_or_buf="results_output.csv", index=False, encoding="utf-8", columns=["Join_Date" , "Score" , "Status"])