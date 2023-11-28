import json
import pandas as pd

# Load your CSV data
csv_file_path = '/path/to/your/log_file.csv'  # Replace with the path to your CSV file
csv_data = pd.read_csv(csv_file_path)


# Function to safely parse JSON from a string
def parse_json(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None


# Function to find valid JSON
def find_valid_json(json_str):
    for i in range(len(json_str)):
        try:
            return json.loads(json_str[:i + 1])
        except json.JSONDecodeError:
            continue
    return None


# Function to transform log entry
def transform_log_entry(log_entry):
    prefix = "LogFrontEndInfo: "
    m_value = log_entry.get("@m", "")

    if m_value.startswith(prefix):
        json_str = m_value[len(prefix):]
        parsed_json = find_valid_json(json_str)
        if parsed_json is not None:
            log_entry["@m"] = parsed_json
            return True
        else:
            print("Valid JSON not found in '@m' field.")
            return False
    else:
        print("The '@m' field does not start with the expected prefix.")
        return False


# Transforming CSV to JSON with nested handling
complete_transformed_json = []

for index, row in csv_data.iterrows():
    # Parse the ResultDescription column as JSON
    parsed_result = parse_json(row['ResultDescription'])

    # Create a JSON object for each row
    if parsed_result:
        json_obj = {
            "date": row['TimeGenerated [UTC]'],
            "log": parsed_result
        }
        if transform_log_entry(json_obj['log']):
            complete_transformed_json.append(json_obj)
        else:
            print(f"Error processing row {index + 1}")

# Output file path
output_json_file = '/path/to/your/transformed_from_csv_raw.json'

# Write the transformed data to the output JSON file
with open(output_json_file, 'w') as f:
    json.dump(complete_transformed_json, f, indent=4)

print(f"Transformation complete. JSON data saved to {output_json_file}")
