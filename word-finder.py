import sys

if __name__ == "__main__":

    included_chars = None
    forbidden_chars = None
    known_chars = None
    forbidden_char_loc = None

    if len(sys.argv) >=2 and sys.argv[1] != "-":
        included_chars = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] != "-":
        forbidden_chars = sys.argv[2]

    if len(sys.argv) >= 4 and sys.argv[3] != "-":
        known_chars = sys.argv[3]
        known_chars = [known_chars[i:i+2] for i in range(0,len(known_chars),2)]

    if len(sys.argv) >= 5 and sys.argv[4] != "-":
        forbidden_char_loc = sys.argv[4]
        forbidden_char_loc = [forbidden_char_loc[i:i+2] for i in range(0,len(forbidden_char_loc),2)]
    
    with open("./word-files/graded-words.txt", "r", encoding="utf-8") as f:
        words = f.read().splitlines()
        filtered = [(line.split(':')[0], float(line.split(':')[1])) for line in words]
        
        if included_chars:
            filtered = [(word,score) for word,score in filtered if 0 not in [c in word for c in included_chars]]

        if forbidden_chars:
            filtered = [(word,score) for word,score in filtered if 1 not in [c in word for c in forbidden_chars]]

        if known_chars:
            filtered = [(word,score) for word,score in filtered if 0 not in [kchar[1]== word[int(kchar[0])-1] for kchar in known_chars]]
        
        if forbidden_char_loc:
            filtered = [(word,score) for word,score in filtered if 1 not in [forbidden[1] == word[int(forbidden[0])-1] for forbidden in forbidden_char_loc]]

        filtered.sort(key=lambda x: x[1], reverse=True)
        words = [word for word,score in filtered]
        print(words)

    
