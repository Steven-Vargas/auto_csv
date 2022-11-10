import csv


def main():
    with open("file.csv", mode="w") as csv_file:
        file_writer = csv.writer(csv_file,
                                 delimiter=",",
                                 quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)

        column_headers = [
            "title",
            "agency",
            "required_report_name",
            "subject",
            "description",
            "date_published",
            "report_type",
            "language",
            "fiscal_year",
            "file"
        ]

        file_writer.writerow(column_headers)

        file_ext = ".pdf"
        # Write test row data for desired row count
        for num in range(1, 26):
            row_data = [
                f"This is test bulk import work #{num}",
                "Doris",
                "Not Required",
                "Accesibility",
                "Lorem ipsum dolor sit amet. Qui vero dignissimos et esse adipisci et adipisci optio et officia dolor "
                "et fuga itaque est fugiat dolores ad distinctio sunt. Vel soluta iusto et eveniet ipsam ut officiis "
                "expedita est autem quia aut quisquam perferendis id doloremque tenetur.",
                "2022-11-10",
                "Brochures",
                "English",
                "2022",
                f"file_{num}{file_ext}"
            ]
            file_writer.writerow(row_data)


if __name__ == "__main__":
    main()
