import pandas as pd
import ast

def clean_string(s):
    # Remove extra quotes and spaces around a string
    s = s.strip('\'" ')
    # Remove an extra single quote if present at the beginning
    if s.startswith("'"):
        s = s[1:]
    # Remove an extra single quote if present at the end
    if s.endswith("'"):
        s = s[:-1]
    return s

def update_error_type(input_csv_path, output_csv_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv_path)

    # Iterate through each row
    for index, row in df.iterrows():
        answer_text_list = ast.literal_eval(row["Answer Text"])

        # Clean each string in the Answer Text list
        cleaned_answer_text = [clean_string(text) for text in answer_text_list]

        # Check if any string in Answer Text is present in Predicted Answer or vice versa
        if any(text in row["Predicted Answer"] or row["Predicted Answer"] in text for text in cleaned_answer_text):
            df.at[index, "Error Type"] = "Technically Correct"

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_csv_path, index=False)

# Example usage
input_csv_path = 'output.csv'
output_csv_path = 'output_new.csv'
update_error_type(input_csv_path, output_csv_path)
