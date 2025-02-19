# LinkedIn Learning Course
# Example file for Python: Working with Excel and Spreadsheet Data by Joe Marini
# Reading CSV file into an array

# import the csv module from the standard library
import csv

def read_csv_to_array(filename):
  # define the array that will hold the data
  data = []
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row)
  return

# Read the data into an array of arrays
inventory_data = read_csv_to_array("Inventory.csv")

# Each row in the array is itself an array of values

