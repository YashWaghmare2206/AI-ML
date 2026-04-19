# To truly master CSV handling, you need to move beyond simple loading and handle the "real-world" messiness. Here are your mastery questions.
#
# ### 🧪 CSV Mastery Challenge
#
# **Medium 1: The Multi-Separator & Metadata Headache**
# You are given a file named `sensor_log.txt`. The first 5 lines contain hardware serial numbers and technician notes. The data starts on line 6. The columns are separated by a **semicolon (**`;`**)**. Additionally, the sensor sometimes glitches and records the text `"ERROR_99"` or `"OFFLINE"` instead of a numerical value in the `temperature` column.
#
# * **The Task:** Write a single `pd.read_csv()` command that:
# 1. Skips the first 5 lines of metadata.
# 2. Uses the correct semicolon separator.
# 3. Treats both `"ERROR_99"` and `"OFFLINE"` as proper `NaN` (missing values) so you can perform math on the temperature column later.
#
# **Medium 2: Selective Loading & Data Integrity**
# You have a massive dataset `global_transactions.csv` with 100 columns. You only need the columns: `Transaction_ID`, `Amount`, and `Currency`.
#
# * **The Task:**
# 1. Write the code to load **only** those 3 columns.
# 2. Force the `Transaction_ID` to be loaded as a **string** (`object`) even if it looks like a number (to prevent Python from stripping leading zeros).
# 3. Export this filtered data to a new file called `filtered_sales.tsv` using a **Tab** as a separator, ensuring that no extra index column is created in the new file.
#
# **Hard 1: The "Chunked" Aggregation (Pipeline Logic)**
# You are working on a server with very low RAM. You have a `huge_data.csv` file (50GB) that contains a column named `Revenue`. You cannot load the whole file into memory.
#
# * **The Task:** 1.  Explain how you would use the `chunksize` parameter to read this file in pieces of 10,000 rows.
# 2.  Write a conceptual Python loop that iterates through these chunks, calculates the **sum** of the `Revenue` column for each chunk, and keeps a "Running Total" variable.
# 3.  By the end of the loop, you should have the total revenue of the entire 50GB file without ever having more than 10,000 rows in your RAM at once.
# ---
# **How would you like to handle these?** You can provide the code/logic for them now to verify your understanding, or if you're feeling 100% confident, we can open the door to **3️⃣ JSON File Handling (Local Files)**.


import pandas as pd

## Q1

df1 = pd.read_csv("sensor_log.txt",
                  sep = ";",
                  skiprows = 5,  # blank line are ignored automatically
                  na_values = ["ERROR_99" , "OFFLINE"],
                  )

print(df1)


## Q2

df2 = pd.read_csv("global_transactions.csv",
                  sep=",",
                  usecols=["Transaction_ID" , "Amount" , "Currency"],
                  dtype={"Transaction_ID" : "string"},

                  )

df2.to_csv("filtered_sales.tsv" ,
           sep = "\t",
           index=False
           )

## Q3

# Now i am using chunksize syntax : chunksize= count_of_rows..and the return objict is not dataframe but and "TextFileReader (iterator)" so iwe have to loop over it and it is an pipe of dataframe after dataframe

chunk_iterator = pd.read_csv("huge_data.csv",
                             sep=",",
                             usecols=["Revenue"],
                             chunksize=47
                             )

revenue_total = 0

for chunk in chunk_iterator:
    revenue_total += chunk["Revenue"].sum()  # sum is use for adding all values in that column of dataframe..as chunksize use retrun and iterator of dataframe
print(f"Total Revenue is : {revenue_total}")