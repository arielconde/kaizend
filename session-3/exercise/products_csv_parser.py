import csv
import argparse

parser = argparse.ArgumentParser(description='Product CSV Reader and Writer')
parser.add_argument('input_filename', help="""the input file
    must be a valid CSV file that contains a `Categories` column""")
parser.add_argument('output_filename', help='the output file')
args = parser.parse_args()

try:
    f = open(args.input_filename, 'r', newline='')
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    with f:
        reader = csv.reader(f)
        columns = next(reader)

        try:
            categories_idx = columns.index('Categories')
        except ValueError as err:
            print(f"Err: {err}")
            print("Categories column is not found on the provided input file!")
        else:
            output_filename = open(args.output_filename, 'w')
            writer = csv.writer(output_filename)
            writer.writerow(columns)
            for row in reader:
                category = row[categories_idx].strip()
                if category != '':
                    writer.writerow(row)
