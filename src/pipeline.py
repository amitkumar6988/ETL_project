import pandas as pd 


def build_sales_dataset(customers, orders, order_items, products):

    sales = (
        order_items
        .merge(orders, on="order_id", how="left")
        .merge(products, on="product_id", how="left")
        .merge(customers, on="customer_id", how="left")
    )

    return sales