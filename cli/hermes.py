#!/usr/bin/env python

import argparse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import subprocess

cred = credentials.Certificate("servicekey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

language_extensions = {
    "py": "python",
    "java": "java",
    "cpp": "c++",
    "c": "c",
    "html": "html",
    "css": "css",
    "js": "javascript",
    "php": "php",
    "rb": "ruby",
    "swift": "swift",
    "kt": "kotlin",
    "scala": "scala",
    "pl": "perl",
    "go": "go",
    "rust": "rust",
    "lua": "lua",
    "ts": "typescript",
    "r": "r",
    "sh": "shell",
    "sql": "sql",
    "asm": "assembly",
    "json": "json",
    "xml": "xml",
    "yaml": "yaml",
    "ini": "ini",
    "md": "markdown",
    "tex": "tex",
    "svg": "svg",
    "csv": "csv",
    "xls": "excel",
    "xlsx": "excel",
    "doc": "word",
    "docx": "word",
    "pdf": "pdf"
}

def delete_all_documents_in_collection():
    f = open("username.txt", "r")
    username = f.read()
    docs = db.collection("hermesdb/users/" + username).stream()
    for doc in docs:
        doc.reference.delete()


def uploadtofirebase(file_paths):
    delete_all_documents_in_collection()
    for file_path in file_paths:
        filename = file_path.split("/")[-1]
        print("File path:", file_path, "\n")

        f = open(file_path, "r")
        contents = f.read()     
        filetype = file_path.split(".")[-1]

        data = {
            "filename": filename,
            "content": contents,
            "filetype": language_extensions[filetype]
        }
        path = "hermesdb/users/"
        f = open("username.txt", "r")
        username = f.read()
        path = path + username

        db.collection(path).add(data)
    
    website = "https://hacknite.vercel.app/" + username
    print("Visit ", website)

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

def setusername(command):
    with open('username.txt', 'w') as file:
        file.write(command)


parser = argparse.ArgumentParser(description="A simple script with argument parsing")

parser.add_argument("operation", choices=["upload", "run", "set"] ,help="debug")


group_upload = parser.add_argument_group("Upload to Firebase")
group_set = parser.add_argument_group("Set the debug command")

group_upload.add_argument("-f", "--file",dest="file_paths", nargs="+", help="File Name")
group_set.add_argument("-s", "--set", dest="set_command", help="run command")
group_set.add_argument("-u", "--username", dest="username", help="run command")

args = parser.parse_args()

if args.operation=="upload" and args.file_paths:
    uploadtofirebase(args.file_paths)
elif args.operation=="set" and args.set_command:
    setcommand(args.set_command) 
elif args.operation=="set" and args.username:
    setusername(args.username) 
elif args.operation=="run":
    runcommand()



args = parser.parse_args()


