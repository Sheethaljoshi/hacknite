
# Hermes

A streamlined approach to debugging for developers. It combines a command-line tool and a browser extension to simplify the process. Users can generate a link from their terminal, which they can then paste onto platforms like Stack Overflow. This link provides access to an interface where users can view and edit code files directly. The browser extension allows users to see the link as an embedded webpage, enabling them to make edits, copy code, find errors, and collaborate with others in real-time. 






## Installation

Unzip the file. 

In linux,

```bash
  sudo cp -f cli/hermes.py /usr/local/bin/hermes 
  chmod +x hermes
  sudo pip install firebase_admin
```
Load unpacked extension in Google Chrome via [chrome://extensions/](chrome://extensions/)

    
## Usage

```bash
    sudo hermes set -u mishal
    hermes upload -f filename.py filename.js
```
