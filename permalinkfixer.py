import re
import unicodedata
import argparse

def normalize_string(s):
    # Turkish character mapping
    # Türkçe karakter eşleştirmesi
    tr_map = {
        'ş': 's', 'Ş': 'S', 'ı': 'i', 'İ': 'I', 'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C'
    }

    # Replace Turkish characters
    # Türkçe karakterleri değiştir
    for key, value in tr_map.items():
        s = s.replace(key, value)

    # Convert to lowercase
    # Küçük harfe çevir
    s = s.lower()

    # Remove accents
    # Aksanları kaldır
    s = ''.join(c for c in unicodedata.normalize('NFD', s)
                if unicodedata.category(c) != 'Mn')

    # Remove years and specific words
    # Yılları ve belirli kelimeleri kaldır
    s = re.sub(r'\b\d{4}(\'(te|da|de))?\b', '', s)
    s = re.sub(r'\b(ocak|subat|mart|nisan|mayis|haziran|temmuz|agustos|eylul|ekim|kasim|aralik)\b', '', s)
    s = re.sub(r'\b(fiyat|tarih|yil|sene)\b', '', s)

    # Replace non-alphanumeric characters with hyphen
    # Alfanümerik olmayan karakterleri tire ile değiştir
    s = re.sub(r'[^a-z0-9]+', '-', s)

    # Remove leading and trailing hyphens
    # Baştaki ve sondaki tireleri kaldır
    s = s.strip('-')

    # Replace multiple hyphens with single hyphen
    # Birden fazla tireyi tek tire ile değiştir
    s = re.sub(r'-+', '-', s)

    return s

def fix_permalink(url):
    # Split the URL into parts
    # URL'yi parçalara ayır
    parts = url.split('/')

    # Find the last non-empty part (which should be the permalink)
    # Son boş olmayan parçayı bul (bu permalink olmalı)
    for i in range(len(parts) - 1, -1, -1):
        if parts[i]:
            # Normalize this part
            # Bu parçayı normalize et
            parts[i] = normalize_string(parts[i])
            break

    # Join the parts back together
    # Parçaları tekrar birleştir
    return '/'.join(parts)

def process_input(input_text, is_url=False):
    if is_url:
        return fix_permalink(input_text)
    else:
        return normalize_string(input_text)

def main():
    parser = argparse.ArgumentParser(description='Normalize Turkish text or fix permalinks.')
    parser.add_argument('input', nargs='?', help='Input text or URL to process')
    parser.add_argument('--url', action='store_true', help='Treat input as URL')
    parser.add_argument('--file', help='Input file to process')
    parser.add_argument('--output', help='Output file to write results')

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        processed_lines = [process_input(line.strip(), args.url) for line in lines]

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                for line in processed_lines:
                    f.write(line + '\n')
        else:
            for line in processed_lines:
                print(line)
    elif args.input:
        result = process_input(args.input, args.url)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result + '\n')
        else:
            print(result)
    else:
        print("No input provided. Use --help for usage information.")

if __name__ == "__main__":
    main()
