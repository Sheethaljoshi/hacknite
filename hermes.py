#!/usr/bin/env python

import argparse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import subprocess

cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

def delete_all_documents_in_collection():
    docs = db.collection("hermesdb").stream()
    for doc in docs:
        doc.reference.delete()


def uploadtofirebase(file_path):
    filename = file_path.split("/")[-1]
    print("File path:", file_path, "\n")

    f = open(file_path, "r")
    contents = f.read()     
    filetype = file_path.split(".")[-1]

    data = {
        "filename": filename,
        "content": contents,
        "filetype": filetype
    }
    delete_all_documents_in_collection()
    db.collection("hermesdb").add(data)

def runcommand():
    with open('runcommand.txt', 'r') as file:
        command = file.read()
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            output = result.stdout
            print("No errors detected")
            return
        except subprocess.CalledProcessError as e:
            output = e.stderr
            print(output)
            name_error_index = output.find("File")
            if name_error_index != -1:
                output = output[name_error_index:]
        print(output)
        
        return output

def setcommand(command):
    with open('runcommand.txt', 'w') as file:
        file.write(command)


parser = argparse.ArgumentParser(description="A simple script with argument parsing")

parser.add_argument("operation", choices=["upload", "run", "set"] ,help="debug")


group_upload = parser.add_argument_group("Upload to Firebase")
group_set = parser.add_argument_group("Set the debug command")

group_upload.add_argument("-f", "--file",dest="file_path", help="File Name")
group_set.add_argument("-s", "--set", dest="set_command", help="run command")

args = parser.parse_args()

if args.operation=="upload" and args.file_path:
    uploadtofirebase(args.file_path)
elif args.operation=="set" and args.set_command:
    setcommand(args.set_command) 
elif args.operation=="run":
    runcommand()



args = parser.parse_args()


