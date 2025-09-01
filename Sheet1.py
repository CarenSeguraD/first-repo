import csv

with open("Bestseller - Sheet1.csv", "r", encoding='utf8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        current_sales = float(row[4])
    if current_sales > max_sales:
        max_sales = current_sales
        best_selling_book = row


with open("Bestseller - Sheet1.csv", "w", encoding='utf8') as file:
    bestseller_inf = csv.writer(file)
    bestseller_inf.writerow(["Book Signature"])
-------------------------------------------------------------------

# open the file in read mode
with open("Bestseller - Sheet1.csv", "r", encoding="utf8") as file:
    csv_reader = csv.reader(file)

    highest_sales = 0
    bestseller = None

    for row in csv_reader:
        if row and row[2] != "Sales in Millions":   # ignore empty rows and header
            sales = float(row[2])                   # sales column
            if sales > highest_sales:
                highest_sales = sales
                bestseller = row

# create a new file and write one row
with open("bestseller_info.csv", "w", encoding="utf8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(bestseller)
