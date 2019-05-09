from argparse import ArgumentParser
from csv import writer
from os import path
from random import choice, randrange


def random_line(index):
    colors = ("red", "Blue", "BLACK", "O-ran-ge")
    tools = ("Hammer", "drill", "Poça", "KNI?FE")
    index = str(index + 1).zfill(6)
    return index, " ".join(map(choice, (colors, tools)))


def create_csv(file_path, lines):
    with open(file_path, "w") as handler:
        csv_writer = writer(handler)
        for index in range(lines):
            csv_writer.writerow(random_line(index))


def filesize(size):
    sizes = {9: "Gb", 6: "Mb", 3: "Kb", 0: "bytes"}
    for power in range(9, -1, -3):
        if size >= 10 ** power:
            size = size // 10 ** power
            return f"{size:,}{sizes.get(power)}"
    return f"0{sizes.get(0)}"


if __name__ == "__main__":

    parser = ArgumentParser(description="A tool to create CSV samples")
    parser.add_argument("filename")
    parser.add_argument("-l", "--lines", type=int)

    args = parser.parse_args()
    if path.exists(args.filename):
        raise RuntimeError(f"{args.filename} already exists.")

    lines = args.lines or randrange(50, 150) * 10 ** 3
    create_csv(args.filename, lines)
    size = filesize(path.getsize(args.filename))
    print(f"👍  {args.filename} was created with {lines:,} lines ({size})")
