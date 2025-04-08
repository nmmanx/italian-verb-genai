def merge_vocabulary_lists(file1_path, file2_path, output_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as f1:
            words1 = {line.strip() for line in f1}
    except FileNotFoundError:
        print(f"Error: File not found at '{file1_path}'")
        return

    try:
        with open(file2_path, 'r', encoding='utf-8') as f2:
            words2 = {line.strip() for line in f2}
    except FileNotFoundError:
        print(f"Error: File not found at '{file2_path}'")
        return

    all_words = words1.union(words2)

    # sorted_words = sorted(list(all_words))
    sorted_words = all_words

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            for word in sorted_words:
                outfile.write(word + '\n')
        print(f"Successfully merged '{file1_path}' and '{file2_path}' into '{output_path}'")
    except Exception as e:
        print(f"Error writing to output file '{output_path}': {e}")

if __name__ == "__main__":
    file1 = input("first vocabulary list file: ")
    file2 = input("second vocabulary list file: ")
    output_file = input("output merged vocabulary list file: ")

    merge_vocabulary_lists(file1, file2, output_file)