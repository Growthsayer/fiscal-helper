import pandas as pd
import json

# Read the CSV file
dir = "fiscal_calendar_helper/"
input_file = dir + "fiscal_calendar.csv"
output_file = dir + "fiscal_calendar.py"

print('Reading fiscal calendar from CSV...')
df = pd.read_csv(input_file)

# Convert DataFrame to a list of dictionaries
calendar = df.to_dict(orient='records')

# Convert list to JSON format for easy writing
calendar_json = json.dumps(calendar, indent=4)

# Write to a Python file
with open(output_file, mode='w', encoding='utf-8') as file:
    file.write(f"calendar = {calendar_json}")

print(f"Converted {input_file} to {output_file}")
