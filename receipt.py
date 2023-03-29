import csv
import datetime

STORE_NAME = "My Grocery Store"
PRODUCTS_CSV = "products.csv"
REQUEST_CSV = "request.csv"
SALES_TAX_RATE = 0.06

def main():
    try:
        products_dict = read_dictionary(PRODUCTS_CSV, 0)
        print(STORE_NAME)
        print()
        total_quantity = 0
        total_price = 0
        now = datetime.datetime.now()
        if now.hour < 11:
            discount = 0.1  # 10% discount
            print("Today's morning special: 10% off all items before 11:00 a.m.!")
            print()
        else:
            discount = 0.0
        with open(REQUEST_CSV, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product = products_dict[product_number]
                product_name = product[1]
                price = float(product[2]) * (1.0 - discount)
                total_quantity += quantity
                total_price += quantity * price
                print(f"{product_name}: {quantity} @ ${price:.2f}")
        print()
        print(f"Total items: {total_quantity}")
        print(f"Subtotal: ${total_price:.2f}")
        sales_tax = total_price * SALES_TAX_RATE
        print(f"Sales tax: ${sales_tax:.2f}")
        total_due = total_price + sales_tax
        print(f"Total due: ${total_due:.2f}")
        print()
        print("Thank you for shopping at My Grocery Store!")
        formatted_date_time = now.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_date_time)
    except FileNotFoundError as e:
        print(f"Error: missing file {e.filename}")
    except PermissionError:
        print(f"Error: Permission denied while accessing {PRODUCTS_CSV} or {REQUEST_CSV}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file: {e}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        key_column_header = header[key_column_index]
        dictionary = {}
        for row in reader:
            key = row[key_column_index]
            value = row
            dictionary[key] = value
        return dictionary

if __name__ == "__main__":
    main()