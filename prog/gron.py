import json
import sys

def flatten_json(obj, parent_key=''):
    items = {}
    if isinstance(obj, dict):
        if parent_key:  # Add the dictionary itself if it's not the root
            items[parent_key] = {}
        else:
            parent_key = 'json'  # Set the root key as 'json'
        for key, value in obj.items():
            new_key = f"{parent_key}.{key}"
            items.update(flatten_json(value, new_key))
    elif isinstance(obj, list):
        if parent_key:  # Add the list itself
            items[parent_key] = []
        for i, value in enumerate(obj):
            new_key = f"{parent_key}[{i}]"
            items.update(flatten_json(value, new_key))
    else:
        items[parent_key] = obj
    return items

def gron_format(flattened_json):
    output_lines = ["json = {};"]
    for key, value in sorted(flattened_json.items()):
        if key == "json":  # Skip the root key
            continue

        formatted_path = ""
        parts = key.split('.')
        for part in parts:
            if part.isdigit():  # Handle array indices
                formatted_path += f'[{part}]'
            else:  # Handle normal keys
                if formatted_path:  # Add dot if it's not the first element
                    formatted_path += '.'
                formatted_path += part

        # Check the type of value to format correctly
        if isinstance(value, str):
            formatted_value = f'"{value}"'
        elif value == "{}":  # Object
            formatted_value = {}
        elif value == "[]":  # Array
            formatted_value = []
        else:  # Other types (e.g., numbers)
            formatted_value = value

        output_lines.append(f"{formatted_path} = {formatted_value};")
    return "\n".join(output_lines)

def main():
    try:
        if len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as file:
                data = json.load(file)
        else:
            data = json.load(sys.stdin)

        flattened_data = flatten_json(data)
        result = gron_format(flattened_data)
        print(result)
        sys.exit(0)
    except json.JSONDecodeError:
        print("Error: Could not parse JSON.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
