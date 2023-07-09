import argparse
import csv
import os
import sys
from rich.console import Console
from rich.traceback import install
from rich import print
from current_date import *
import sys
import matplotlib as plt

# All the needed variables in the program
install()
console = Console()
current_date = CurrentDate(date.today())

BOUGHT_FILE = "bought.csv"
SOLD_FILE = "sold.csv"


# parser arguments command line interface to show the commands use python3 main.py -h
parser = argparse.ArgumentParser(description="Supermarket information tool")

subparsers = parser.add_subparsers(dest="command", help="Information on adjusting the date")
subparser_date = subparsers.add_parser("today", help="This shows today's date")
subparser_forward = subparsers.add_parser("forward", help="Jumping forward")
subparser_rewind = subparsers.add_parser("rewind", help="Hopping back")

# subparsers = parser.add_subparsers(title='Figuring it out', 
#                                    description="This is a test",
#                                    help="what does this do")

parser.add_argument("--prod_name", type=str, metavar="", help="shows product name")
parser.add_argument("--price", type=float, metavar="", help="shows product price")
parser.add_argument("--exp_date", type=str, metavar="", help="shows product expiration date")
parser.add_argument("--quant", type=int, metavar="", help="shows product quantity")

args = parser.parse_args()

if args.command == "today":
    output = current_date.time()
    print(f"This is the current date {output}")

if args.command == "forward":
    forward_output = current_date.go_to_the_future(10)
    print(f"Now we are jumping 'forward' {forward_output}")

if args.command == "rewind":
    rewind_output = current_date.go_to_the_past(30)
    print(f"With this we are going to 'rewind' time {rewind_output}")


# opening csv files 
# def test_function():
#     console.log(log_locals=True)
#     with open("bought.csv", 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)
#         print("\n")
#     with open("sold.csv", 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)
    
# test_function()


# functions needed

# reading the csv file in DictReader
# writing the csv File
# get the current date
# advance time in days
# buy product with dictionary key, value items
# sell the product with dictionary key, value items
# generate an inventory report
# generate revenue report
# generate profit report
# generate export report
# visualize statistics  using matplotlib

class Product:

    def __init__(self, bought, sold):
        self.bought = bought
        self.sold = sold

    def apple(self, price, expire):
        self.price = price
        self.expire = expire
        return self.bought, self.sold
    

class Iventory:
    def __init__(self, Product, Int):
        self.Product = Product
        self.int = int

        def get_product_quant(product: Product): Int 