import pandas as pd

df=pd.read_csv(r'C:\Users\Abraham\Desktop\DOINGS\supermarket_sales - Sheet1.csv')

# Display the first few rows
print("\nFirst few Rows:")
print(df.head())

# missing data

print("\nmissing values:")
print(df.isnull().sum())

#checking for duplicate

print("\nduplicate values")
print(df.duplicated().sum())

#checking for data type

print("\ndata type:")
print(df.dtypes)

#convert date to datetime formart

print('\n date to datetime:')
print( pd.to_datetime(df["Date"]))

#convert time to standard time formart
print("\nproper time formart")
print(pd.to_datetime(df["Time"], format="%H:%M").dt.time)

#average purchase values

print("\naverage purchase value:")
print(df["Total"].mean())

#frequency of purchase

total_purchases = df.shape[0]
print("Total Purchases:", total_purchases)

#avarage quantity purchased

print("\naverge Quantity purchaased:")
print(df["Quantity"].mean())


#revenue per prodduct line

print("\nrevenue per product line")
print(df.groupby("Product line")["Total"].sum())

#COSTOMER DISTRIBUTION

print("\ncustomer_distribution:")
print(df["Customer type"].value_counts())


