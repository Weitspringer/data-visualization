import re
import csv
import matplotlib.pyplot as plt
import numpy as np


LABELS = ["PIN", "name", "ICC", "Club", "Grade", "Tournament", "Nw", "Ng", "IGoR", "FGoR"]
SEPARATOR = ","
PATH_TO_DATA = "exercise_1/exercise_1_2/data/"
ENCODING = "utf-8"


def convert_hst_to_csv():
    f = open(PATH_TO_DATA + "all.hst", "r", encoding=ENCODING)
    csv = open(PATH_TO_DATA + "all.csv", "w", encoding=ENCODING)
    csv.seek(0)
    csv.truncate()
    lines = list(filter(lambda a: len(a) != 1, f.readlines()))
    for line in lines:
        splitted_line = list(filter(lambda a: a != "", re.split('\\s+', line)))
        if lines.index(line) == 0 or len(splitted_line) == 0:
            continue
        if len(splitted_line) == 11:
            i = 0
            for entry in splitted_line:
                if i != len(splitted_line) - 1 and i != 1:
                    csv.write(entry + SEPARATOR)
                elif i == 1:
                    csv.write(entry + ' ')
                else:
                    csv.write(entry)
                i += 1
            csv.write("\n")
        elif len(splitted_line) == 10: # In this case, the player name consists of a single string
            i = 0
            for entry in splitted_line:
                if i != len(splitted_line) - 1:
                    csv.write(entry + SEPARATOR)
                else:
                    csv.write(entry + "\n")
                i += 1


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


def get_data_for_player(table, player_name):
    return list(filter(lambda line: line.get(LABELS[1]) == player_name, table))


def extract_tournament_dates(table):
    dates = []
    date_regex = re.compile("\d+")
    for entry in table:
        dates.append(date_regex.search(entry.get(LABELS[5])).group())
    return dates


def get_gor_values(table):
    gors_before = []
    gors_after = []
    for entry in table:
        gors_before.append(int(entry.get(LABELS[8])))
        gors_after.append(int(entry.get(LABELS[9])))
    return gors_before, gors_after


if __name__ == "__main__":
    pl = read_csv()
    pl_filtered = get_data_for_player(pl, 'Cech Tim')
    dates = extract_tournament_dates(pl_filtered)
    gors_before, gors_after = get_gor_values(pl_filtered)

    gors = []
    double_dates = []
    for i in gors_before:
        gors.append(i)
        gors.append(gors_after[gors_before.index(i)])
    for d in dates:
        double_dates.append(d)
        double_dates.append(d)

    fig, ax = plt.subplots()
    ax.plot(double_dates, gors)
    plt.show()
