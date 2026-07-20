from src.extract import extract_data
from src.transform import convert_order_dates, inspect_dataframe,delivery_dates
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #load
    customers=extract_data('customers.csv')
    orders=extract_data('orders.csv')
    #transform
    orders=convert_order_dates(orders)#convert data type to string
    orders=delivery_dates(orders)#calculate delivery time

    print(customers.head())
    print(orders.head())
#inspect
    inspect_dataframe(customers,"customers")
    inspect_dataframe(orders,"orders")

    print(orders["delivery_time"].describe())

    

    








if __name__ =="__main__":
    main()


