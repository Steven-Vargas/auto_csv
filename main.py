import csv


def main():
    with open("file.csv", mode="w") as csv_file:
        file_writer = csv.writer(csv_file,
                                 delimiter=",",
                                 quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)

        column_headers = [
            "Column1",
            "Column2",
            "Column3"
        ]

        file_writer.writerow(column_headers)

        # Write test row data for desired row count
        for num in range(1, 101):
            row_data = [
                "Column1 Data",
                "Columns2 Data",
                # Include sequential row count in column
                f"Column3_{num}"
            ]
            file_writer.writerow(row_data)


if __name__ == "__main__":
    main()
