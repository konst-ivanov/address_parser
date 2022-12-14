"""
This script transforms address strings consisting of street names and house numbers into JSON objects, i.e.:
    "Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
    "Am Bächle 23"  -> {"street": "Am Bächle",   "housenumber": "23"}

The script should be executed with the arguments:
    -i <input_file_path>  : path to the file containing address strings, one on each row
    -o <output_file_path> : path to the JSON file where the result will be saved
"""
import argparse
import json
import re


def parse_addresses(address_list: list[str]) -> list[dict]:
    """
    Parse address strings into dictionaries
    :param address_list: list of address strings
    :return: list of address dictionaries
    """
    re_str_num = re.compile(r"(?P<street>.+)(?<! No)[, ]+?(?=No |\d)(?P<housenumber>.+)")
    re_num_str = re.compile(r"(?P<housenumber>\d+)[, ]+(?P<street>.+)")
    result = [
        (re_num_str if line[0].isdigit() else re_str_num).match(line).groupdict() for line in address_list
    ]
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", type=str)
    parser.add_argument("-o", type=str)
    args = parser.parse_args()
    input_file = args.i
    output_file = args.o
    with open(input_file, "r", encoding="utf8") as f:
        address_lines = f.read().splitlines()
    complex_addresses = parse_addresses(address_lines)
    with open(output_file, "w", encoding="utf8") as f:
        json.dump(complex_addresses, f, ensure_ascii=False)
