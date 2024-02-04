import sys
import time

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        return words
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def count_words(word_list):
    if not word_list:
        return None

    start_time = time.time()

    word_count = {}
    for word in word_list:
        # Remove punctuation and convert to lowercase for case-insensitive counting
        cleaned_word = word.strip('.,!?"\'()[]{}:;')
        cleaned_word = cleaned_word.lower()

        # Count the words
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

    elapsed_time = time.time() - start_time

    return word_count, elapsed_time

def write_results_to_file(results):
    with open('WordCountResults.txt', 'w') as file:
        for word, count in results.items():
            file.write(f"{word}: {count}\n")
        file.write(f"Elapsed Time: {results['elapsed_time']:.6f} seconds\n")

def main():
    # Req 5: Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    words = read_file(file_path)

    # Req 3: Handle invalid data
    if words is None:
        sys.exit(1)

    results = dict(zip(
        ["word_count", "elapsed_time"],
        count_words(words)
    ))

    # Req 7: Print elapsed time on the screen
    print(f"Elapsed Time: {results['elapsed_time']:.6f} seconds")

    for word, count in results["word_count"].items():
        # Req 2: Print results on the screen
        print(f"{word}: {count}")

    # Req 7: Write results to file
    write_results_to_file(results["word_count"])

if __name__ == "__main__":
    main()
