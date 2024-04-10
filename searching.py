import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]


def linear_search(numbers, number):
    results = {"positions": [], "count": 0}
    for i in range(len(numbers)):
        if number == numbers[i]:
            results["positions"].append(i)
            results["count"] = results["count"]+1
    return results


def pattern_search(sequence, pattern):
    index = set()
    for i in range(len(sequence)):
        if sequence[i:(i + len(pattern))] == pattern:
            index.add(i+1)
    return index


def main():
    dna_sequence = read_data("sequential.json", "dna_sequence")
    # result = linear_search(unordered_numbers, 5)
    vyskyt = pattern_search(dna_sequence, "ATA")
    print(vyskyt)


if __name__ == '__main__':
    main()