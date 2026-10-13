from pathlib import Path

# Gets the folder where your current script is located
script_dir = Path(__file__).parent
print(Path)


# Safely points to the JSON file in the 'Files' subfolder
json_path = script_dir / "Files" / "json_example.json"

print(json_path)
with open(json_path, "r") as file:
    # Your code here
    pass
