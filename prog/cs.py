import csv
import sys

def sum_csv_columns_except_first(csv_data):
    """
    Sums up all columns except the first one from CSV data.

    Args:
    csv_data (iterator): An iterator over the rows of the CSV data.

    Returns:
    dict: A dictionary with column headers as keys and their sums as values.
    """
    sums = {}
    for row in csv_data:
        for column in row:
            if column == next(iter(row)):  # Skip the first column
                continue
            try:
                sums[column] = sums.get(column, 0) + float(row[column])
            except ValueError:
                pass  # Ignore non-numeric values
    return sums

def main():
    if len(sys.argv) > 2:
        print("Usage: python cs.py [file_path]")
        sys.exit(1)

    # Check if file path is provided
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            csv_data = csv.DictReader(file)
            sums = sum_csv_columns_except_first(csv_data)
    else:
        csv_data = csv.DictReader(sys.stdin)
        sums = sum_csv_columns_except_first(csv_data)

    for column, sum_value in sums.items():
        print(f"Sum of '{column}': {sum_value}")

if __name__ == "__main__":
    main()
