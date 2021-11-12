import re

LABELS = ["PIN", "name", "ICC", "Club", "Grade", "Tournament", "Nw", "Ng", "IGoR", "FGoR"]
SEPARATOR = ","

if __name__ == "__main__":
    f = open("exercise_1/data/all.hst", "r", encoding="utf-8")
    csv = open("exercise_1/data/all.csv", "w", encoding="utf-8")
    for label in LABELS:
        if LABELS.index(label) != len(LABELS) - 1:
            csv.write(label + SEPARATOR)
        else:
            csv.write(label + "\n")
    for line in f.readlines():
        splitted_line = re.split('\\s+', line)
        if len(splitted_line) == 13:
            for entry in splitted_line:
                if entry != "" and splitted_line.index(entry) != len(splitted_line) -2:
                    if splitted_line.index(entry) != 2:
                        csv.write(entry + SEPARATOR)
                    else:
                        csv.write(entry + "\xA0")
                elif splitted_line.index(entry) == len(splitted_line) -2:
                    csv.write(entry + "\n")
