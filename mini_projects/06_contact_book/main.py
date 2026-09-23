"""Mini Project 06: Contact Book"""
import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def add_contact(contacts, name, phone, email):
    contacts[name] = {"phone": phone, "email": email}


def find_contact(contacts, name):
    return contacts.get(name)


def main():
    contacts = load_contacts()
    add_contact(contacts, "Sinta", "0812-1111-2222", "sinta@example.com")
    save_contacts(contacts)
    print(find_contact(contacts, "Sinta"))


if __name__ == "__main__":
    main()
