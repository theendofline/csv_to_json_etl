import json

# Define the input and output file paths
input_json_file = '/path/to/your/transformed_from_csv_raw.json'  # Replace with the path to your input JSON file
output_json_file = '/path/to/your/transformed_from_raw_valid.json'  # Replace with the path where you want to


# save the output JSON file


def find_valid_json(json_str):
    for i in range(len(json_str)):
        try:
            # Attempt to parse the string up to the current position
            return json.loads(json_str[:i + 1])
        except json.JSONDecodeError:
            # Continue if the current substring is not valid JSON
            continue
    return None


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


def transform_nested_json(input_file, output_file):
    try:
        # Read the input JSON file
        with open(input_file, 'r') as f:
            data = json.load(f)

        transformed_data = []

        for index, item in enumerate(data):
            log_data = item.get("log", {})

            if transform_log_entry(log_data):
                transformed_data.append(item)
            else:
                print(f"Error processing row {index + 1}")

        # Write the transformed data to the output JSON file
        with open(output_file, 'w') as f:
            json.dump(transformed_data, f, indent=4)

        print(f"Transformation complete. JSON data saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Call the function to perform the transformation
transform_nested_json(input_json_file, output_json_file)
