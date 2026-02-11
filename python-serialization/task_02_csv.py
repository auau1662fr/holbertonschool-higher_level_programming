#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read data from a CSV file and convert it to JSON format.
    Writes the JSON data to 'data.json'.

    Returns True if successful, False if there is an exception.
    """
    try:
        # Lire les données CSV
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        # Écrire les données JSON dans data.json
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
