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


    