Bicycle Generator
This project generates all possible bicycle configurations from an Excel file and outputs them as a JSON string. It includes automated tests to verify the output.
Prerequisites

Python: Version 3.10 or higher
Libraries:
Install required libraries using pip:pip install pandas openpyxl





Setup and Usage

Ensure Excel File:

Place Bicycle.xlsx at C:\Nidhieee\projects\BicycleGenerator\Bicycle.xlsx.
The file should contain sheets: ID, GENERAL, 1 (Brakes), 2 (Wheels), 3 (Frame size), 4 (Groupset), 5 (Suspension), 6 (Color).


Run the Generator:

Open a terminal in C:\Nidhieee\projects\BicycleGenerator.
Run:python bicycle_generator.py


This reads Bicycle.xlsx, generates 5508 bicycle configurations, and saves them to bicycles.json.


Run Tests:

Run:python -m unittest test_bicycle_generator.py


This verifies the JSON output (count, structure, and specific entries).



Output

File: bicycles.json in C:\Nidhieee\projects\BicycleGenerator.
Format: A JSON string containing a list of 5508 bicycle dictionaries, each with fields like ID, Manufacturer, Brake type, Frame color, etc.
Example Entry:{
    "ID": "CITY-R26SSH1-01",
    "Manufacturer": "Bikes INC",
    "Brake type": "Rim",
    "Frame color": "RED",
    ...
}
<img width="1195" height="293" alt="image" src="https://github.com/user-attachments/assets/84fd96c8-3f07-4182-b5a0-4c013004be61" />
<img width="1478" height="979" alt="image" src="https://github.com/user-attachments/assets/e7da332f-fb3a-45e6-8101-023462b7c491" />




