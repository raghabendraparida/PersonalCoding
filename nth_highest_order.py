import pandas as pd

# Sample data
data = {
    'customer_id': [1, 2, 1, 3, 2, 2, 4, 3, 1, 4],
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
}
df = pd.DataFrame(data)

# Step 1: Count orders per customer
order_counts = df.groupby('customer_id').size().reset_index(name='order_count')

# Step 2: Sort by order count descending
sorted_counts = order_counts.sort_values(by='order_count', ascending=False)

# Step 3: Get the nth highest
n = 2  # Change this value to get a different rank
if n <= len(sorted_counts):
    nth_highest = sorted_counts.iloc[n - 1]  # zero-based index
    print(f"{n}th highest order count is by customer {nth_highest['customer_id']} with {nth_highest['order_count']} orders.")
else:
    print(f"There are only {len(sorted_counts)} customers. Cannot retrieve the {n}th highest.")
