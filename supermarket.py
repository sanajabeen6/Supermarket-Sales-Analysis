#Task 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('supermarket_sales .csv')
df.head()
df.info()


#Task 2
df.describe()


#Task 3
# Group by 'Branch' and sum the 'Total' column
branch_sales = df.groupby('Branch')['Total'].sum()

# Find the branch with the highest total sales
highest_branch = branch_sales.idxmax()
highest_sales = branch_sales.max()

print(f"Branch with highest total sales: {highest_branch} (Total Sales: {highest_sales})")

# Group by 'Product line' and sum the 'Total'
product_line_totals = df.groupby('Product line')['Total'].sum()

# Sort product lines by total in descending order
top_product_lines = product_line_totals.sort_values(ascending=False)

print(top_product_lines)

# Calculate average 'Total' for each 'Customer type'
avg_spend = df.groupby('Customer type')['Total'].mean()

print(avg_spend)

# Calculate average 'Rating' for each 'Branch'
avg_ratings = df.groupby('Branch')['Rating'].mean()

print(avg_ratings)


# Task 4

# Task A:
# Assuming df is your DataFrame
branch_totals = df.groupby('Branch')['Total'].sum().reset_index()

# Create bar chart with seaborn
sns.barplot(data=branch_totals, x='Branch', y='Total', palette='bright')
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Task B:
# Assuming df is your DataFrame
product_line_totals = df.groupby('Product line')['Total'].sum().reset_index()

# Create bar chart with seaborn
sns.barplot(data=product_line_totals, x='Product line', y='Total', palette='pastel')
plt.title('Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Task C:
# Assuming df is your DataFrame
# Group by 'Customer type' and calculate average 'Total'
avg_spending = df.groupby('Customer type')['Total'].mean().reset_index()

# Bar plot comparison
sns.barplot(data=avg_spending, x='Customer type', y='Total', palette='GnBu')
plt.title('Average Spending: Member vs Non-Member')
plt.xlabel('Customer Type')
plt.ylabel('Average Total')
plt.tight_layout()
plt.show()

# Task D:
# Histogram of customer ratings
sns.histplot(df['Rating'], bins=10, kde=True, color='magenta')
plt.title('Distribution of Customer Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# Total Sales Over 3-Month Period
# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate total sales by date
daily_sales = df.groupby('Date')['Total'].sum().reset_index()

# Line chart of total sales over time
sns.lineplot(data=daily_sales, x='Date', y='Total', marker='o')
plt.title('Total Sales Over 3-Month Period')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()


# Calculate average 'Rating' for each 'Branch'
df = pd.read_csv('supermarket_sales .csv')
avg_ratings = df.groupby('Branch')['Rating'].mean()

# Find the branch with the highest average rating
highest_branch = avg_ratings.idxmax()
highest_rating = avg_ratings.max()

print(f"Branch with the highest customer satisfaction rating: {highest_branch} (Average Rating: {highest_rating:.2f})")
