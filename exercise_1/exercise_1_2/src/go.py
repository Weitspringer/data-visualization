import re
import csv
import itertools


LABELS = ["PIN", "name", "ICC", "Club", "Grade", "Tournament", "Nw", "Ng", "IGoR", "FGoR"]
SEPARATOR = ","
PATH_TO_DATA = "exercise_1/exercise_1_2/data/"
ENCODING = "utf-8"


def convert_hst_to_csv():
    f = open(PATH_TO_DATA + "all.hst", "r", encoding=ENCODING)
    csv = open(PATH_TO_DATA + "all.csv", "w", encoding=ENCODING)
    lines = f.readlines()
    for line in lines:
        splitted_line = list(filter(lambda a: a != "", re.split('\\s+', line)))
        if lines.index(line) == 0 or len(splitted_line) == 0:
            continue
        if len(splitted_line) == 11:
            for entry in splitted_line:
                if splitted_line.index(entry) != len(splitted_line) - 1:
                    csv.write(entry + SEPARATOR)
                else:
                    csv.write(entry + "\n")
        else:
            print("Line too long") # Observation: The name is only consisting of 1 word


def read_csv():
    parsed_lines = []
    with open(PATH_TO_DATA + "all.csv", encoding=ENCODING) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        line_number = 0
        for row in reader:
            if line_number > 0:
                row_dict = {}
                for label in LABELS:
                    row_dict.update({label: row[LABELS.index(label)]})
                parsed_lines.append(row_dict)
            line_number += 1
        csv_file.close()
    return parsed_lines


if __name__ == "__main__":
    convert_hst_to_csv()
    pl = read_csv()
    print(pl[1])
