import json
import random

def filter_and_sample(input_jsonl, output_jsonl, sample_size=20):
    # Read the input JSONL file
    with open(input_jsonl, 'r', encoding='utf-8') as file:
        data = [json.loads(line.strip()) for line in file]

    # Filter out records where predicted_answer is present in the answers' text
    filtered_data = [record for record in data if record["predicted_answer"] not in record["answers"]["text"]]

    # Randomly sample 20 records from the remaining data
    sampled_data = random.sample(filtered_data, min(sample_size, len(filtered_data)))

    # Write the sampled data to a new JSONL file
    with open(output_jsonl, 'w', encoding='utf-8') as file:
        for record in sampled_data:
            file.write(json.dumps(record, ensure_ascii=False) + '\n')

# Example usage
input_jsonl_path = 'eval_predictions.jsonl'
output_jsonl_path = 'error_samples.jsonl'
filter_and_sample(input_jsonl_path, output_jsonl_path)
