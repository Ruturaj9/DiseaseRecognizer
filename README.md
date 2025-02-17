# Disease Recognizer

## Overview
Disease Recognizer is a GUI-based application that helps users identify diseases based on symptoms. It utilizes a MySQL database to store disease information and Tkinter for the user interface.

## Features
- User-friendly GUI built with Tkinter.
- Connects to a MySQL database to retrieve disease information.
- Identifies diseases based on user-input symptoms.
- Uses PIL for image handling.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- MySQL Server
- Required Python libraries: Tkinter, PIL (Pillow), mysql-connector-python

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/DiseaseRecognizer.git
   cd DiseaseRecognizer/Code
   ```
2. Install dependencies:
   ```sh
   pip install pillow mysql-connector-python
   ```
3. Configure the MySQL database:
   - Create a database named `diseaserecognizer`.
   - Import the provided SQL file (if any) into MySQL.
   - Update `DiseaseRecognizer.py` with your database credentials if needed.

## Usage
Run the application using:
```sh
python DiseaseRecognizer.py
```


