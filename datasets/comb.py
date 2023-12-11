import json
def combine_jsonl_files(file_paths, output_file_path):
    combined_data = []
    
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            
            data = [json.loads(line) for line in input_file]
            combined_data.extend(data)
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for item in combined_data:
            json_line = json.dumps(item, ensure_ascii=False)
            output_file.write(json_line + '\n')
    print(f"Combined data has been saved to {output_file_path}")
file_paths = ['squad_train.jsonl', 'squad_train_adv.jsonl', 'squad_train_cf.jsonl']
output_file_path = 'squad_train_comb.jsonl'
combine_jsonl_files(file_paths, output_file_path)
