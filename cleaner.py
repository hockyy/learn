import re
import codecs
import sys

def clean_srt(file_path):
    try:
        with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
    except UnicodeDecodeError:
        with codecs.open(file_path, 'r', encoding='iso-8859-1') as file:
            content = file.read()

    # Remove BOM if present
    content = content.lstrip('\ufeff')

    # Remove non-printable characters except newlines and CJK characters
    content = re.sub(r'[^\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uff00-\uffef\u1100-\u11ff\u3130-\u318f\ua960-\ua97f\uac00-\ud7af\u4e00-\u9fff\x20-\x7E\n]', '', content)

    # Fix common encoding issues
    content = content.replace('â€™', "'")
    content = content.replace('â€"', "–")
    content = content.replace('â€œ', '"')
    content = content.replace('â€', '"')

    with codecs.open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Cleaned SRT file has been saved as {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file.srt")
        sys.exit(1)

    input_file = sys.argv[1]
    clean_srt(input_file)