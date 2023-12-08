import csv

class CSVLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = [CSVRow(row) for row in csv_reader]
        return data

class CSVRow:
    def __init__(self, data):
        self.data = data

    def get_value(self, column_name):
        return self.data[column_name]

    def get_value_as_int(self, column_name):
        return int(self.data[column_name])

    def get_value_as_float(self, column_name):
        return float(self.data[column_name])

    def __repr__(self):
        return f"CSVRow({self.data})"

class ObjectListGenerator:
    def __init__(self, obj_list):
        self.obj_list = obj_list

    def generate_objects(self):
        for obj in self.obj_list:
            yield obj

class ColumnPrinter:
    def __init__(self, obj_list):
        self.obj_list = obj_list

    def print_columns(self, *column_names):
        for obj in self.obj_list:
            columns = [obj.get_value(column_name) for column_name in column_names]
            print(', '.join(str(column) for column in columns))

# Завантаження даних
csv_loader = CSVLoader("CSV_data/russia_losses_equipment.csv")
generator = ObjectListGenerator(csv_loader.data)

# Виведення стовпців за введеними користувачем назвами
printer = ColumnPrinter(csv_loader.data)
column_names = input("Введіть назви стовпців (через кому): ").split(',')
printer.print_columns(*column_names)
