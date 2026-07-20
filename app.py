# AI Disaster Response & Resource Management System

incidents = []


def report_incident():
    print("\n--- Report Disaster ---")
    disaster = input("Disaster Type: ")
    location = input("Location: ")
    severity = input("Severity (Low/Medium/High): ")

    incident = {
        "Disaster": disaster,
        "Location": location,
        "Severity": severity,
        "Status": "Pending"
    }

    incidents.append(incident)
    print("\nIncident reported successfully!")


def view_incidents():
    print("\n--- Incident List ---")

    if len(incidents) == 0:
        print("No incidents found.")
        return

    for i, incident in enumerate(incidents, start=1):
        print(f"\nIncident {i}")
        print(f"Disaster : {incident['Disaster']}")
        print(f"Location : {incident['Location']}")
        print(f"Severity : {incident['Severity']}")
        print(f"Status   : {incident['Status']}")


def allocate_resources():
    if len(incidents) == 0:
        print("\nNo incidents available.")
        return

    view_incidents()

    try:
        choice = int(input("\nEnter Incident Number: ")) - 1

        if 0 <= choice < len(incidents):
            resource = input(
                "Assign Resource (Ambulance/Fire Team/Police/Medical Team): "
            )

            incidents[choice]["Status"] = f"Resource Assigned: {resource}"
            print("\nResource allocated successfully.")

        else:
            print("Invalid incident number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n========== AI Disaster Response ==========")
        print("1. Report Disaster")
        print("2. View Incidents")
        print("3. Allocate Resources")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            report_incident()

        elif choice == "2":
            view_incidents()

        elif choice == "3":
            allocate_resources()

        elif choice == "4":
            print("\nThank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
