#!/usr/bin/python3

def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    # Vérifier si vide
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Boucle sur les invités
    for i, person in enumerate(attendees, start=1):
        content = template

        name = person.get("name", "N/A")
        title = person.get("event_title", "N/A")
        date = person.get("event_date") or "N/A"
        location = person.get("event_location", "N/A")

        content = content.replace("{name}", str(name))
        content = content.replace("{event_title}", str(title))
        content = content.replace("{event_date}", str(date))
        content = content.replace("{event_location}", str(location))

        filename = f"output_{i}.txt"

        with open(filename, "w") as f:
            f.write(content)
