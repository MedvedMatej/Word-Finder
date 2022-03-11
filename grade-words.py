from collections import defaultdict

letter_grades = {}
with open("./word-files/letter-frequencies.txt", "r", encoding="utf-8") as f:
    letters = f.read().splitlines()
    letter_grades = {letter.split(':')[0]: float(letter.split(':')[1]) for letter in letters}

with open("./word-files/normalized-words.txt", "r", encoding="utf-8") as f:
    with open("./word-files/graded-words.txt", "w", encoding="utf-8") as fw:
        words = f.read().splitlines()
        for word in words:
            letters = {char for char in word}
            score = 0
            for letter in letters:
                score += letter_grades[letter]
            fw.write("{}:{:.5f}\n".format(word,score))