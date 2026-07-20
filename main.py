from src.extract import extract_data
from src.transform import (convert_order_dates, inspect_dataframe,
                           delivery_dates,validate_delivery_time
                           ,clean_orders,validate_orders,clean_products,
                           clean_order_items,validate_order_items)
from src.relationship import(validate_product_relationship,
                             validate_customer_relationship,validate_order_relationship)
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #extract
    customers=extract_data('customers.csv')
    orders=extract_data('orders.csv')
    products=extract_data("products.csv")
    order_items=extract_data("order_item.csv")
    #transform
    orders=convert_order_dates(orders)#convert data type to string
    orders=delivery_dates(orders)#calculate delivery time

    print(customers.head())
    print(orders.head())
#inspect
    inspect_dataframe(customers,"customers")
    inspect_dataframe(orders,"orders")
    inspect_dataframe(products,"products")
    inspect_dataframe(order_items,"order_item")

#validate
    orders=clean_orders(orders)
    validate_orders(orders)

    products=clean_products(products)

    order_items=clean_order_items(order_items)
    validate_order_items(order_items)

#validate product relationship
    
    validate_product_relationship(order_items, products)

#validate order relationship
    validate_order_relationship(order_items,orders)

#validate customer relationship
    validate_customer_relationship(orders, customers)




  



    

    








if __name__ =="__main__":
    main()


