import seaborn as sns
import matplotlib.pyplot as plt
def inspect_dataframe(df,name):
    print("=="*60)
    print(f"dataset:{name}")
    print("=="*60)
    print("\nShape")
    print(df.shape)
    print("\nColumns")
    print(df.columns.tolist())
    print("\ndata types")
    print(df.dtypes)
    print("\nMissing values")
    print(df.isnull().sum())
    print("\nDuplicate values")
    print(df.duplicated().sum())

import pandas as pd

def convert_order_dates(df):

    date_columns=["order_purchase_timestamp","order_approved_at",
        "order_delivered_carrier_date","order_delivered_customer_date","order_estimated_delivery_date"]
    
    for column in date_columns:
        df[column] = pd.to_datetime(df[column])

    return df


def delivery_dates(df):
    df["delivery_time"]=(df["order_delivered_customer_date"]-df["order_purchase_timestamp"]).dt.days
    return df


def validate_delivery_time(df):
      #validating data for delivery time column of orders
    print("\nDelivery time statistics")
    print(df["delivery_time"].describe())
    print("\n Missing values")
    print(df["delivery_time"].isna().sum())
    print("\nNegative delivery time")
    print((df["delivery_time"]<0).sum())
    print("\n Longest delivery")
    print(df["delivery_time"].max())

    sns.boxplot(y="delivery_time",data=df)
    plt.show()

def clean_orders(df):
    df=convert_order_dates(df)
    df=delivery_dates(df)
    return df



def validate_orders(df):

    print("\nDelivery Time Statistics")
    print(df["delivery_time"].describe())

    print("\nMissing Delivery Time")
    print(df["delivery_time"].isna().sum())

    print("\nNegative Delivery Time")
    print((df["delivery_time"] < 0).sum())

    print("\nLongest Delivery")
    print(df["delivery_time"].max())

    inconsistent = df[
        (df["order_status"] == "delivered") &
        (df["order_delivered_customer_date"].isna())
    ]

    print(f"\nInconsistent delivered orders: {len(inconsistent)}")




def clean_products(df):
    #replacing missinng name with readable value,else the dataset is alredy clean
    df["product_category_name"]=(df["product_category_name"].fillna("Unknown"))

    return df


def clean_order_items(df): #only this coz the data set is clean almost
    df["shipping_limit_date"]=pd.to_datetime(df["shipping_limit_date"])
    return df

def validate_order_items(df):

    print("\nOrder Items Summary")
    print("--------------------")
    print(f"Rows: {len(df)}")
    print(f"Duplicates: {df.duplicated().sum()}")
    print(f"Missing Values:\n{df.isnull().sum()}")
    