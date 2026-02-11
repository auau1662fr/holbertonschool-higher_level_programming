#!/usr/bin/python3
"""Serialization and Deserialization using XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML and save it to a file.
    Each key becomes a tag, each value becomes the text of that tag.
    """
    # Créer l'élément racine
    root = ET.Element("data")

    # Ajouter chaque élément du dictionnaire comme sous-élément
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Tout est converti en string

    # Créer l'arbre et écrire dans le fichier
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Lire un fichier XML et reconstruire un dictionnaire Python.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text  # Les valeurs restent des chaînes

    return data
