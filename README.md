# Recipes ETL
This script is in fulfillment of the HelloFresh assessment.
Python version used: `3.12.0`

 The directory includes:

- The main script is saved in a single Python file, namely `script.py`
- The packages are saved in a single Txt file, namely `requirements.txt`

# How to Run
1. The script contains several external packages, namely pandas and regex.
   
   To install the mentioned packages, the following command can be run

   ```
   pip install -r requirements.txt
   ```
2. To run the script, simply run the command

    ```
    python script.py
    ```

    1. The script will ask the path of the dataset, an example of a good path will be shown. 
        
        The script accepts a dataset that follows the format of an object/dictionary in each line.`recipes.json`, provides as an example of the format used.
    2. The script will return an error if the path doesn't exist/not found and exits.
    3. After the script was successful, the script will ask what name would you like to save it in along with the example of a good name. 
    
        The file will be saved as a **CSV** file with a **UTF-8 encoding**.
# How it Works
## script.py
Inside the script, it contains three functions:
1. to_minutes(string)-> int
   
   Required input of string as an input and returns an integer of total minutes

   Changes the string format of "PT**hour**H**minutes**M" to minutes. 1 hour is determined to be 60 minutes. It accepts various format as the hour and minutes are optional regex. *Example of acceptable formats include: PT1H30M, PT1H, PT40M*
   
   If the string doesn't follow the given format (empty or less than 1 minute), the function will return a **negative** number.
2. assign_difficulty(int) -> str
   
   Required input of integer as the input and returns a string of difficulty

   Changes the total minutes of integer into different difficulties.
   The difficulty follows:
      1. Hard: total time more than 60 minutes
      2. Medium: total time more than 30 minutes less than 60 minutes 
      3. Easy: total time less than 30 minutes
      4. Unknown: total time unknown or less than 1 minute
3. main()

    The main function will ask for your dataset that follows the format of `recipes.json`.
    ** If path doesn't exist, the script will exit **
    Main function will run the other function accordingly.
    Main function will create field of total time (prepTime + cookTime) in minutes
    Main function will create field of difficulty based on the totalTime field
    Main function will delete the totalTime field
    Main function will ask for your desired name for saving the CSV file.

