#!/usr/bin/env python

import argparse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()


data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

db.collection("hermesdb").add(data)


parser = argparse.ArgumentParser(description="A simple script with argument parsing")

parser.add_argument("-f", "--file", help="File Name", required=True)

args = parser.parse_args()

file_path = args.file

print("File path:", file_path, "\n")

f = open(file_path, "r")
print(f.read())     
