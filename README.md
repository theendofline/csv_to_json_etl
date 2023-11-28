# Log Data Transformation modules

These modules are just for transforming and restructuring log data in two stages.

## Modules

### CSV to JSON Conversion Module
- **Functionality:** Converts log data from CSV files into JSON, handling nested JSON structures within the CSV data.
- **Usage:** Set the `csv_file_path` and `output_json_file` variables to your input CSV file and output JSON file paths. Run the script to process and convert the CSV data into JSON format.

### Nested JSON Logs Transformation Module
- **Functionality:** Processes nested JSON structures within log entries from JSON files and transforms them into a more readable JSON format.
- **Usage:** Set the `input_json_file` and `output_json_file` variables to your input and output JSON file paths. Run the script to transform the nested JSON data.

## Requirements
- Python 3.x
- Pandas library
- JSON library (included in the standard Python library)

## Installation
Ensure Python 3.x is installed on your system and install Pandas using pip:
```pip install pandas```

## Examples
- **CSV to JSON Module:** Processes CSV file containing log data, extracting and transforming JSON structures from specified columns, saving the output as a JSON file.
- **Nested JSON Module:** Takes an input JSON file with nested log entries, processes each entry, and writes the output to a specified JSON file.

## Contributing
Welcome contributions to enhance the application, whether it's improving existing modules or adding new functionalities. Fork this repository and submit pull requests for any proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Acknowledge any individuals, resources, or third-party libraries that were instrumental in the development of this application.

