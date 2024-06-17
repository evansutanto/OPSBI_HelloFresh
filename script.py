import pandas as pd
import json
import re
import os

def to_minutes(time_string: str) -> int:
    """Converts a time string format to minutes using regex.
    Args:
        time_string: A string representing a time.

    Returns:
        int: The total time in minutes.
        0: If the time string is invalid.
    """
    match = re.match(r"PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?", time_string)
    if not match:
        return 0
    hours = int(match.group("hours")) if match.group("hours") else 0
    minutes = int(match.group("minutes")) if match.group("minutes") else 0
    return hours * 60 + minutes

def assign_difficulty(minutes: int) -> str:
    """Assigns a difficulty level based on the total time.
    Args:
        minutes: An integer representing the total time in minutes.
    Returns:
        str: The difficulty level of the recipe (Easy, Medium, Hard, Unknown).
    """
    if minutes > 60:
        return "Hard"
    elif minutes <= 60 and minutes >= 30:
        return "Medium"
    elif minutes < 30 and minutes > 0:
        return "Easy"
    else:
        return "Unknown"

def main():
    print("Hello, Fresh! Let's filter some chili recipes.")
    inp_path = input("What path is your dataset stored at? (e.g. recipes.json)\n")

    if not os.path.exists(inp_path):
        print("Invalid path. Please provide a valid path to your dataset.")
        return
    
    print("Path is valid. Proceeding to read the dataset.")
    recipes = []
    with open(inp_path, "r") as file:
        for line in file:
            json_data = json.loads(line)
            recipes.append(json_data)
    df = pd.DataFrame(recipes)
    
    print("Dataset read successfully. Proceeding to filter chili recipes.")
    chili_df = df[df["ingredients"].str.contains("chile|chilies|chili|chiles", case=False)].copy()
    # Add a new column for total time in minutes
    chili_df.loc[:, "totalTime"] = chili_df["prepTime"].apply(to_minutes) + chili_df["cookTime"].apply(to_minutes)
    # Assign difficulty level based on total time
    chili_df.loc[:, "difficulty"] = chili_df["totalTime"].apply(assign_difficulty)
    chili_df = chili_df.drop(columns=["totalTime"])
    
    print("Chili recipes filtered successfully. Proceeding to save the dataset.")
    saved_path = input("What name would you like to save your CSV? (e.g. filtered_recipes)\n")
    if (saved_path.endswith(".csv")):
        saved_path = saved_path[:-4]

    chili_df.to_csv(saved_path + '.csv', index=False, encoding="utf-8")
    print("Dataset saved successfully. Exiting script.")

if __name__ == "__main__":
    main()