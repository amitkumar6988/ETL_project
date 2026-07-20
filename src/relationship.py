def validate_product_relationship(order_items, products):

    missing_products = order_items[
        ~order_items["product_id"].isin(products["product_id"])
    ]

    print("\nProduct Relationship Validation")
    print("--------------------------------")
    print(f"Missing product references: {len(missing_products)}")

    return missing_products

def validate_order_relationship(order_items, orders):

    missing_orders = order_items[
        ~order_items["order_id"].isin(orders["order_id"])
    ]

    print("\nOrder Relationship Validation")
    print("------------------------------")
    print(f"Missing order references: {len(missing_orders)}")

    return missing_orders


def validate_customer_relationship(orders, customers):

    missing_customers = orders[
        ~orders["customer_id"].isin(customers["customer_id"])
    ]

    print("\nCustomer Relationship Validation")
    print("---------------------------------")
    print(f"Missing customer references: {len(missing_customers)}")

    return missing_customers