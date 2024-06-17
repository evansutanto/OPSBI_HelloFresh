import pandas as pd
import json
import re
import os

def to_minutes(time):
    match = re.match(r"PT((?P<hours>\d+)H)?((?P<minutes>\d+)M)?", time)
    if not match:
        return -1 # accounts for PT and empty strings
    hours = int(match.group("hours")) if match.group("hours") else 0
    minutes = int(match.group("minutes")) if match.group("minutes") else 0
    return hours * 60 + minutes

def assign_difficulty(time):
    if time > 60:
        return "Hard"
    elif time < 60 and time > 30:
        return "Medium"
    elif time < 30 and time > 0:
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
    chili_df.loc[:, "totalTime"] = chili_df["prepTime"].apply(to_minutes) + chili_df["cookTime"].apply(to_minutes)
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