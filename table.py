import csv
from prettytable import PrettyTable
csv_file = "cart.csv"
try:
    with open(csv_file, mode="r") as file:
        reader = csv.reader(file)
        table = PrettyTable()
        headers = next(reader, None)  
        if headers:
            table.field_names = headers
            for row in reader:
                table.add_row(row)
            print(table)
        else:
            print("The cart is empty.")
except FileNotFoundError:
    print(f"File {csv_file} does not exist.")
