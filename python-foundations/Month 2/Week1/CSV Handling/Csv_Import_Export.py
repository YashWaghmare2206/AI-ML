import pandas as pd

# ======================================================
# 1️⃣ IMPORT CSV — USING MOST IMPORTANT PARAMETERS
# ======================================================

df = pd.read_csv(
    "sales_data.csv",

    # ---- File structure ----
    sep=",",                    # column separator
    header=0,                   # first row is header
    names=None,                 # use header names from file

    # ---- Column selection ----
    usecols=["Date", "User ID", "Product Name", "Price", "Qty"],

    # ---- Index handling ----
    index_col=None,             # index will be auto-generated (0,1,2...)

    # ---- Data type handling ----
    dtype={
        "User ID": "int64",
        "Price": "float64",
        "Qty": "int64"
    },

    # ---- Missing values handling ----
    na_values=["NA", "null", "", "None"],

    # ---- Date parsing ----
    parse_dates=["Date"],       # convert Date to datetime

    # ---- Text encoding ----
    encoding="utf-8",

    # ---- Performance / large files ----
    nrows=None,                 # read all rows
    skiprows=None,              # don’t skip rows
    low_memory=False            # avoid mixed dtype warnings
)

# ======================================================
# 2️⃣ INSPECTION & SANITY CHECK
# ======================================================

print("\n--- DATA PREVIEW ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

# ======================================================
# 3️⃣ BASIC TRANSFORMATIONS
# ======================================================

# Rename columns (clean naming)
df.rename(columns={
    "User ID": "user_id",
    "Product Name": "product",
    "Qty": "quantity"
}, inplace=True)

# Create a new derived column
df["total_amount"] = df["Price"] * df["quantity"]

# Set meaningful index (Date is real data)
df.set_index("Date", inplace=True)

# ======================================================
# 4️⃣ EXPORT CSV — USING MOST IMPORTANT PARAMETERS
# ======================================================

df.to_csv(
    "processed_sales_data.csv",

    # ---- Index handling ----
    index=True,                 # index contains real data (Date)
    index_label="date",         # name of index column in CSV

    # ---- File formatting ----
    sep=",",
    header=True,                # write column names

    # ---- Missing values ----
    na_rep="NULL",              # how missing values appear

    # ---- Text encoding ----
    encoding="utf-8",

    # ---- Float formatting ----
    float_format="%.2f",        # price formatting

    # ---- Line handling ----
    line_terminator="\n",

    # ---- Safety ----
    mode="w"                    # write mode (overwrite)
)

print("\nCSV exported successfully!")
