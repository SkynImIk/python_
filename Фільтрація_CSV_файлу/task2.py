import csv

def filter_csv(input_file, output_file, criteria_field, criteria_value):
    with open(input_file, 'r') as input_csv:
        csv_reader = csv.DictReader(input_csv)
        data = [row for row in csv_reader]

    filtered_data = [row for row in data if float(row.get(criteria_field)) >= float(criteria_value)]

    with open(output_file, 'w', newline='') as output_csv:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        
        csv_writer.writeheader()
        csv_writer.writerows(filtered_data)

input_file = 'CSV_data/nalgfs-jun2021-tables-csv.csv'
output_file = 'CSV_data/data_filtered.csv'
criteria_field = 'Data_value'
criteria_value = '5000.0'

filter_csv(input_file, output_file, criteria_field, criteria_value)
