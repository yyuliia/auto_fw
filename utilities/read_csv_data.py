import csv


def get_csv_data(file_name):
    # empty list
    rows = []
    # open csv file
    csv_file = open(file_name, "r")
    # csv reader
    reader = csv.reader(csv_file)
    # skip the headers
    next(reader)
    # add rows to list
    for row in reader:
        rows.append(row)
    return rows