"""CSV manager module
"""
import csv
import os


class CsvManager:
   
    def import_data(
            self, directory, filename, delimiter, quotechar
    ):
        data_file = os.path.join(directory, filename)
        with open(data_file, 'r', newline='', encoding='utf8') as file:
            read_file = csv.reader(
                file, delimiter=delimiter, quotechar=quotechar
            )
            data = []
            for row in read_file:
                data.append(row)
            return data
    
    def export_pre_run_data(self, directory, filename, data):
        data_file = os.path.join(directory, filename)
        with open(data_file, 'w', newline='',  encoding='utf8') as file:
            filewriter = csv.writer(
                file, delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            filewriter.writerow([
                "id",
                "address",
                "new_address",
                "match"
                ]
            )
            for item in data:
                filewriter.writerow(
                    [
                        item[0],
                        item[1],
                        item[2],
                        item[3]
                        ]
                )

    def export_run_data(self, directory, filename, data):
        data_file = os.path.join(directory, filename)
        with open(data_file, 'w', newline='',  encoding='utf8') as file:
            filewriter = csv.writer(
                file, delimiter=';',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
            filewriter.writerow([
                "id",
                "numero",
                "nom_rue",
                "nom_complet",
                "bureau"
                ]
            )
            for item in data:
                filewriter.writerow(
                    [
                        item['id'],
                        str(item['number']),
                        item['street_name'],
                        item['full_address'],
                        item['sector']
                    ]
                )
