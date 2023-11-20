import sys
import os
import argparse
# Extension: multiple files

def count_words_chars_lines(text):
    lines = text.split('\n')
    if lines and lines[-1] == '':
        line_count = len(lines) - 1
    else:
        line_count = len(lines)
    words = text.split()
    chars = len(text)
    return line_count, len(words), chars

def display_files_content(file_list):
    for filename in file_list:
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
                print(f"Contents of {filename}:\n{text}")
                print("\n" + "-"*40 + "\n")  
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

def process_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        return text, count_words_chars_lines(text)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return "", (None, None, None)

def main():
    parser = argparse.ArgumentParser(description='Count lines, words, and characters in a file.')
    parser.add_argument('files', nargs='*', help='List of files to process')
    args = parser.parse_args()

    total_lines = total_words = total_chars = 0
    file_processed = False

    if args.files:
        for filename in args.files:
            file_content, (line_count, word_count, char_count) = process_file(filename)
            if file_content:
                filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
                print(f"{line_count}\t{word_count}\t{char_count}\t{filename_without_ext}")
                total_lines += line_count
                total_words += word_count
                total_chars += char_count
                file_processed = True

        if file_processed and len(args.files) > 1:
            print(f"{total_lines}\t{total_words}\t{total_chars}\ttotal")

    else:
        text = sys.stdin.read()
        line_count, word_count, char_count = count_words_chars_lines(text)
        print(f"{line_count}\t{word_count}\t{char_count}")

if __name__ == "__main__":
    main()