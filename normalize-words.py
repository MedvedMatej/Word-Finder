from unidecode import unidecode
from collections import defaultdict

with open("words.txt", "r", encoding="utf-8") as fr:
    with open("normalized-words.txt", "w", encoding="utf-8") as fw:
        lines = fr.readlines()

        chars = set('čšž')
        prev_line = None
        for line in lines:
            char_locations = defaultdict(lambda:[])

            if '.' in line or '-' in line:
                continue

            if any((c in chars) for c in line):
                for i,char in enumerate(line):
                    if char in chars:
                        char_locations[char].append(i)
                
            line = unidecode(line)
            for k,values in char_locations.items():
                  for value in values:
                      line = line[:value] + k + line[value+1:]

            if prev_line != line:
                fw.write(line.lower())
                prev_line = line


