import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid number of arguments.")
    else:
        included_chars = sys.argv[1]
        known_chars = None
        forbidden_chars = sys.argv[2]
        if(len(sys.argv) >= 4):
            known_chars = sys.argv[3]
            known_chars = [known_chars[i:i+2] for i in range(0,len(known_chars),2)]
        with open("normalized-words.txt", "r", encoding="utf-8") as f:
            words = f.read().splitlines()
            filtered = [word for word in words if 0 not in [c in word for c in included_chars]]
            filtered = [word for word in filtered if 1 not in [c in word for c in forbidden_chars]]
            if known_chars:
                filtered = [word for word in filtered if 0 not in [kchar[1]== word[int(kchar[0])-1] for kchar in known_chars]]
            print(filtered)

    
