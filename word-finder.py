import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid number of arguments.")
    else:
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
        
        with open("normalized-words.txt", "r", encoding="utf-8") as f:
            filtered = f.read().splitlines()
            
            if included_chars:
                filtered = [word for word in filtered if 0 not in [c in word for c in included_chars]]

            if forbidden_chars:
                filtered = [word for word in filtered if 1 not in [c in word for c in forbidden_chars]]

            if known_chars:
                filtered = [word for word in filtered if 0 not in [kchar[1]== word[int(kchar[0])-1] for kchar in known_chars]]
            
            if forbidden_char_loc:
                filtered = [word for word in filtered if 1 not in [forbidden[1] == word[int(forbidden[0])-1] for forbidden in forbidden_char_loc]]

            print(set(filtered))

    
