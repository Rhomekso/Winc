# Imports
import argparse
import csv
import os
import sys
from rich import print
from datetime import date
from all_functions import *


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
INVENTORY_FILE = "inventory.csv"
SALES_FILE = "sales.csv"

# Header
parser = argparse.ArgumentParser(description="Supermarket information tool")

# CLI for product information
parser.add_argument("--all_prod", action="store_true", help="shows all products and quantity")
parser.add_argument("--bought", action="store_true", help="shows all bought products and expiration date")
parser.add_argument("--sold", action="store_true", help="shows product price and expiration date or if it is expired.")
# parser.add_argument("-exp_date", type=str, metavar="", help="shows product expiration date")
# parser.add_argument("-quant", type=int, metavar="", help="shows product quantity")
parser.add_argument("--inven", action="store_true", help="shows product inventory stock information")
parser.add_argument("--sales", action="store_true", help="shows product sales information")



# Command input
subparsers = parser.add_subparsers(dest="command", help="Information on adjusting the data")

# CLI for the date of today
subparser_date = subparsers.add_parser("today", help="This shows today's date")

# CLI for the date of forward
subparser_forward = subparsers.add_parser("forward",help="Jumping forward")
subparser_forward.add_argument("--add", help="add days", type=int, required=True)

# CLI for the date of rewind
subparser_rewind = subparsers.add_parser("rewind", help="Hopping back")
subparser_rewind.add_argument("--sub", help="subtract days", type=int, required=True)

# CLI for the buy parser
subparser_buy = subparsers.add_parser("buy", help="Buying a product")
subparser_buy.add_argument("--product", help="wich product", type=str, required=True)
subparser_buy.add_argument("--price", help="product price", type=float, required=True)
subparser_buy.add_argument("--quantity", help="desired quantity", type=int, required=True)
subparser_buy.add_argument("--expiration", help="expiration date", type=str, required=True)

# CLI for the sell parser
subparser_sell = subparsers.add_parser("sell", help="Selling a product")
subparser_sell.add_argument("--product", help="wich product", type=str, required=True)
subparser_sell.add_argument("--price", help="product price", type=float, required=True)

args = parser.parse_args()

# functions needed

# create an usage guide
# using the argparse module to add arguments and sub arguments to make sure the help information is clear and readable

if __name__ == "__main__":
    
    csv_reader = CsvReader("info_today.csv")
    inventory = Inventory(INVENTORY_FILE)
    sales = Inventory(SALES_FILE)

    if args.command == "today": 
        info_today = csv_reader.create_date_today()


    if args.command == "forward":
        days_forward = args.add
        info_forward = csv_reader.change_forward(days_forward)
        print(f"The date has been changed by {days_forward} days")
        print(f"Now we are jumping 'forward': {info_forward}")

    if args.command == "rewind":
        days_rewind = args.sub
        info_today = csv_reader.create_date_today()
        current_date = CurrentDate(info_today)
        rewind_output = current_date.go_to_the_past(days_rewind)
        info_rewind = csv_reader.change_rewind(days_rewind)
        print(f"The date has been changed by {days_rewind} days")
        print(f"With this we are going to 'rewind' time: {rewind_output}")

    if args.command == "buy":
        prod_name = args.product
        price = args.price 
        exp_date = args.expiration
        quant = args.quantity
        today = csv_reader.create_date_today()
        prod_buy = inventory.buy_product(prod_name, price, exp_date, quant, today)

    if args.command == "sell":
        prod_name = args.product
        price = args.price 
        prod_sell = inventory.sell_product(prod_name, price)

    if args.inven:
        inventory_stock = inventory.inventory_info()

    if args.sales:
        sales_stock = sales.sales_info()

    if args.all_prod:
        inventory.all_products()

    if args.bought:
        inventory.product_bought()

    if args.sold:
        inventory.product_sold()

    
