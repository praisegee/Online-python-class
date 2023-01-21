
import json
import sqlite3

def create():
    user_data = []

    website = input("Enter the name of the website: ").lower()
    password = input("Enter the password : ")

    data = {
        'website': website,
        'password': password
    }

    user_data.append(data)

    try:
        with open('data.json', 'r') as f:
            json_data = json.load(f)

            for detail in json_data:
                if detail['website'] == website:
                    detail['password'] = password
            
            with open('data.json', 'w') as f:
                json.dump(json_data, f, indent=4)

    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump(user_data, f, indent=4)


def retreive():
    try:
        with open('data.json', 'r') as f:
            json_data = json.load(f)

            website = input('Enter the name of the website: ').lower()

            for detail in json_data:
                if detail['website'] == website:
                    result = f"Password for {detail['website']} account is `{detail['password']}`."
                    return result

            return f"{website} does not exists! Try again."

    except FileNotFoundError:
        return "No data yet.. Try to create a password first!"


def delete():
    try:
        with open('data.json', 'r') as f:
            json_data = json.load(f)

            website = input('Enter the name of the website you want to delete: ').lower()

            for detail in json_data:
                if detail['website'] == website:
                    json_data.remove(detail)

                    with open('data.json', 'w') as f:
                        json.dump(json_data, f, indent=4)
                        
                    return "Deleted!"

            return "Not found!"

    except FileNotFoundError:
        return "No data yet.. Try to create a password first!"



