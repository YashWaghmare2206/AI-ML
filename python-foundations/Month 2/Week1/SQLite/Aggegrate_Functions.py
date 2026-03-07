
# # 🔹 Topic 6 — Aggregate Functions
#
# Goal:
#
# > **Summarize data into numbers**
#
# Aggregates convert **many rows → single value**.
#
# ---
#
# ## 1️⃣ COUNT — Count Rows
#
# ### Example
#
# ```sql
# SELECT COUNT(*) FROM sales;
# ```
#
# Counts **total rows** (including NULLs).
#
# ---
#
# ### Count non-null values
#
# ```sql
# SELECT COUNT(price) FROM sales;
# ```
#
# Counts rows where `price` is NOT NULL.
#
# ---
#
# ## 2️⃣ SUM — Total
#
# ```sql
# SELECT SUM(quantity) FROM sales;
# ```
#
# Adds all quantities.
#
# ---
#
# ## 3️⃣ AVG — Average
#
# ```sql
# SELECT AVG(price) FROM sales;
# ```
#
# Returns mean price.
#
# ---
#
# ## 4️⃣ MIN / MAX
#
# ```sql
# SELECT MIN(price), MAX(price) FROM sales;
# ```
#
# Lowest and highest price.
#
# ---
#
# ## 5️⃣ Aggregate with WHERE (Very Common)
#
# ```sql
# SELECT AVG(price)
# FROM sales
# WHERE product = 'Laptop';
# ```
#
# First filters rows, then aggregates.
#
# ---
#
# ## 6️⃣ Alias with Aggregates
#
# ```sql
# SELECT
# SUM(price * quantity) AS total_revenue
# FROM sales;
# ```
#
# Very common in business analytics.
#
# ---
#
# ## 7️⃣ Multiple Aggregates Together
#
# ```sql
# SELECT
# COUNT(*) AS total_orders,
# SUM(quantity) AS total_items,
# AVG(price) AS avg_price
# FROM sales;
# ```
#
# One query → multiple metrics.
#
# ---
#
# ## 8️⃣ Pandas + Aggregate SQL
#
# ```python
# df = pd.read_sql(
#     "SELECT COUNT(*) AS total_rows FROM sales",
#     conn
# )
# print(df)
# ```
#
# ---
#
# ## ⚠️ Important Rules
#
# * Aggregates **ignore NULL values** (except `COUNT(*)`)
# * Aggregates return **single row**
# * No GROUP BY yet (next topic)
#
