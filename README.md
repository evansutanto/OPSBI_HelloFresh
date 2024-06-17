# Recipes ETL
This script is in fulfillment of the HelloFresh assessment. The directory includes:

- The main script is saved in a single Python file, namely `script.py`
- The packages are saved in a single Txt file, namely `requirements.txt`

## How to Run
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