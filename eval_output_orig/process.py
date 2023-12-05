import json
import csv

def filter_and_save_to_csv(jsonl_file, output_csv):
    filtered_records = []
    title_context_mapping = {}

    with open(jsonl_file, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            record = json.loads(line.strip())

            # Remove records where predicted_answer is present in the answers' text
            if record["predicted_answer"] not in record["answers"]["text"]:
                filtered_records.append(record)

                # Build title-context mapping
                title_context_mapping[record["title"]] = record["context"]

    # Save filtered records to CSV
    with open(output_csv, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write header for the first sheet
        csv_writer.writerow(["Title", "Question", "Answer Text", "Predicted Answer"])

        for record in filtered_records:
            csv_writer.writerow([record["title"],
                                record["question"],
                                record["answers"]["text"],  # Assuming one text entry for simplicity
                                record["predicted_answer"]])

# Example usage
jsonl_file_path = 'eval_predictions.jsonl'
output_csv_path = './output.csv'

filter_and_save_to_csv(jsonl_file_path, output_csv_path)
