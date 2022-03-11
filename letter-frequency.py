from collections import defaultdict

with open("./word-files/normalized-words.txt", "r", encoding="utf-8") as f:
    with open("./word-files/letter-frequencies.txt", "w", encoding="utf-8") as fw:
        words = f.read().splitlines()
        counted_letters = defaultdict(int)
        for word in words:
            for char in word:
                counted_letters[char]+=1
        
        for k,v in counted_letters.items():
            fw.write("{}:{:.5f}\n".format(k,(v/(len(words)*5))))

