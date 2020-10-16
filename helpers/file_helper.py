#!/usr/bin/env python

import csv

class FileHelper:
    @staticmethod
    def send_to_file(filename:str, data:str, file_type:str, new_line:bool = False) -> bool:
        try:
            with open(filename, 'a') as file:
                if new_line:
                    file.write(
                        "\n{}{}".format(
                            data,
                            ',' if file_type == 'csv' else ''
                        )
                    )
                else:
                    file.write(
                        "{}{}".format(
                            data,
                            ',' if file_type == 'csv' else ''
                        )
                    )
            return True
        except:
            return False


    @staticmethod
    def replace_in_file(filename:str, data:str, replace_data:str, file_type:str, row:int = None, column:int = None) -> bool:
        content = None
        if file_type == 'csv':
            try:
                with open(filename, newline = '') as file:
                    content = list(csv.reader(file))
                    content[row - 1][column - 1] = content[row - 1][column - 1].replace(replace_data, data)

                with open(filename, 'w') as file:
                    writer = csv.writer(file)
                    writer.writerows(content)

                return True
            except:
                return False

        elif file_type == 'txt':
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    content = content.replace(replace_data, data)

                with open(filename, 'w+') as file:
                    file.write(content)

                return True
            except:
                return False

    @staticmethod
    def get_ext(filename:str):
        return filename.split('.')[1]
