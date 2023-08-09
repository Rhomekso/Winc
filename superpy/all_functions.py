import argparse
import csv
import os
import sys
import shutil
import matplotlib as plt
from tempfile import NamedTemporaryFile
from rich.console import Console
from rich.traceback import install
from rich import print
from datetime import datetime
from current_date import *
from csv_reader import *

# All the needed variables in the program
install()
console = Console()

class Inventory:

    def __init__(self, allinfo):
        self.allinfo = allinfo

# this shows inventory information 
    def inventory_info(self):
        # console.log(log_locals=True)
        with open(self.allinfo, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key, value in row.items():
                    print(f"{key}: {value}")

# this shows sales information
    def sales_info(self):
        # console.log(log_locals=True)
        with open(self.allinfo, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                for key, value in row.items():
                    print(f"{key}: {value}")
            return row

# this shows all products and quantity
    def all_products(self):
        # console.log(log_locals=True)
        with open(self.allinfo, "r") as file:
            read = csv.DictReader(file)
            for row in read:
                print(f"Product: {row['product name']}\nQuantity: {row['quantity']}")

# this show the product buy date and expiration date
    def product_bought(self):
        # console.log(log_locals=True)
        with open(self.allinfo, "r") as file:
            read = csv.DictReader(file)
            for row in read:
                print(f"This is the buy date {row['buy date']}, Expiration date {row['expiration date']}")

# this shows products sold and if it was expired
    def product_sold(self): 
        # console.log(log_locals=True)
        csv_reader = CsvReader("info_today.csv")
        info_today = str(csv_reader.create_date_today())
        # print(info_today)
        with open(self.allinfo, "r") as sold:
            check_sold = csv.DictReader(sold)
            for row in check_sold: 
                exp_date = row['expiration date']
                sell_price = row['sell price']
                product = row["product name"]
                if info_today <= exp_date:
                    print(f"{product} was sold for: {sell_price} with expiration date of: {exp_date}")
                else:
                    print(f"ERROR: {product} has been expired {exp_date}")

# this is buying a product 
    def buy_product(self, product_name, price, expiration_date, quantity, today):
        fieldnames = ['id', 'product name','buy date','sell price','expiration date','quantity']
        with open(self.allinfo, "r+", newline="") as buying_prod:
            writer = csv.DictWriter(buying_prod, fieldnames=fieldnames, delimiter=",") 
            if os.path.exists("inventory.csv") == False:
                writer.writeheader()
                id = 1
                writer.writerow({'id': id, 
                                'product name': product_name,
                                'buy date': today, 
                                'sell price': price, 
                                'expiration date': expiration_date, 
                                'quantity': quantity})
            else:
                final_line = buying_prod.readlines()[-1]
                last_line = final_line.split(",")
                id = int(last_line[0]) + 1
                writer.writerow({'id': id, 
                                'product name': product_name,
                                'buy date': today, 
                                'sell price': price, 
                                'expiration date': expiration_date, 
                                'quantity': quantity})


# this is selling a product
    def sell_product(self, product_name, quantity):
        filename = "inventory.csv"
        tempfile = NamedTemporaryFile(mode="w", delete=False)
        fieldnames = ['id', 'product name', 'buy date', 'sell price', 'expiration date', 'quantity']
        with open(self.allinfo, "r+", newline="") as sell_prod, tempfile:
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames, delimiter=",")
            reader = csv.DictReader(sell_prod, fieldnames=fieldnames, delimiter=",")
            if os.path.exists("inventory.csv"):
                prod_found = False
                # writer.writeheader()
                for lines in reader:
                    if product_name == lines["product name"]:
                        prod_found = True
                        product_quantity = lines["quantity"]
                        new_stock = int(product_quantity) - quantity
                        print(f"Updating stock:\nproduct: {lines['product name']}\nquantity: {new_stock}")
                        row = {
                            "id": lines["id"],
                            "product name": lines["product name"],
                            "buy date": lines["buy date"],
                            "sell price": lines["sell price"],
                            "expiration date": lines["expiration date"],
                            "quantity": new_stock
                        }
                        if  new_stock == 0:
                            print(f"{product_name} out of stock, quantity: {new_stock}")
                            continue
                        writer.writerow(row)
                    else:
                        row = {
                            "id": lines["id"],
                            "product name": lines["product name"],
                            "buy date": lines["buy date"],
                            "sell price": lines["sell price"],
                            "expiration date": lines["expiration date"],
                            "quantity": lines["quantity"]
                        }
                        writer.writerow(lines)
                if prod_found == False:
                    print(f"product: {product_name}, not in stock")
            shutil.move(tempfile.name, filename)

# TODO!!!!!
    def get_revenue(self, product, date):
        fieldnames = ["id,product name,buy date,sell price,expiration date,quantity"]
        if os.path.exists("inventory.csv") == True:
            with open(self.allinfo, "r", newline="") as sell_prod:
                total_revenue = 0
                for sell_prod in reader:
                    reader = csv.DictReader(sell_prod, fieldnames=fieldnames, delimiter=",")
                    products = sell_prod.split(",")
                    if date == products["buy date"]:
                        total_revenue = total_revenue + products["price"]
                        
                        return total_revenue




        # accesing the inventory.csv and putting(buying) a product and putting it in an new csv file 
        # function must remove the product and put in the new file.
        # product should be the instance that is accesed by the argparse maybe an empty string ""

        # sell_product
        # report revenue

# class Statisticks:



# functions needed

# buy product with dictionary key, value items
# sell the product with dictionary key, value items
# generate an inventory report
# generate revenue report
# generate profit report
# generate export report
# visualize statistics  using matplotlib
