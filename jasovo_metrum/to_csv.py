import json
import csv
import os
from subprocess import check_output
import unidecode as ud
from config import METRE_TO_CAT
import time


# Load the JSON poem
# Convert poems to list of lines
with open("lines.txt", "w", encoding="utf-8") as lines:
    for book_json in os.listdir("corpusCzechVerse/ccv"):
        book = json.load(
            open("corpusCzechVerse/ccv/" + book_json, "r", encoding="utf-8")
        )
        for poem in book:
            poem_body = poem["body"]
            for stanza_index, stanza in enumerate(poem_body):
                for line_index, line in enumerate(stanza):
                    lines.write(line["text"] + "\n")

# Syllabify all lines
t = time.time()
with open("syllabified_lines.txt", "w", encoding="utf-8") as f:
    f.write(check_output("python sekacek.py lines.txt", shell=True).decode("utf-8"))
print(time.time() - t)

with open("data.csv", "w", encoding="utf-8") as data:
    with open("syllabified_lines.txt", "r", encoding="utf-8") as lines:
        index = 0
        csv_writer = csv.writer(
            data, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow(["index", "type", "metre", "text"])
        for book_json in os.listdir("corpusCzechVerse/ccv"):
            book = json.load(
                open("corpusCzechVerse/ccv/" + book_json, "r", encoding="utf-8")
            )
            for poem in book:
                poem_body = poem["body"]
                for stanza_index, stanza in enumerate(poem_body):
                    for line_index, line in enumerate(stanza):
                        text = lines.readline().strip()
                        text = "".join(
                            [c for c in text if c.isalpha() or c in [" ", "~", "/"]]
                        )
                        words = text.split(" ")
                        for word_index, word in enumerate(words):
                            if word.lower() in ["k", "s", "z", "v"]:
                                words[word_index] = ""
                                continue
                            if (tilde_index := word.find("~")) != -1:
                                words[word_index] = word[tilde_index + 1:]
                        syllables = []
                        for word in words:
                            syllables.extend(word.split("/"))
                        text = " ".join(
                            syllable for syllable in syllables if syllable != ""
                        )
                        text = '"' + ud.unidecode(text.lower()) + '"'
                        metre = line["metre"][0]["type"]
                        if metre == "N":
                            continue
                        csv_writer.writerow([index, "test", METRE_TO_CAT[metre], text])
                        index += 1
