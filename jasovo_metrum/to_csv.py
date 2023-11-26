import json
import csv
import os
import pyphen
import unidecode as ud

# Load the JSON poem
with open("data.csv", "w", encoding="utf-8") as f:
    index = 0
    csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["index", "type", "metre", "text"])
<<<<<<< HEAD
    dic = pyphen.Pyphen(lang="cs_CZ")
    for book_json in os.listdir("corpusCzechVerse/ccv"):
        # for book_json in ["0001.json"]:
=======
    for book_json in os.listdir("corpusCzechVerse/ccv"):
>>>>>>> 234d6d09a06d1f32ff20f07bf17e192dc1f51a20
        book = json.load(
            open("corpusCzechVerse/ccv/" + book_json, "r", encoding="utf-8")
        )
        for poem in book:
            poem_body = poem["body"]
            for stanza_index, stanza in enumerate(poem_body):
                for line_index, line in enumerate(stanza):
                    text = line["text"]
                    text = "".join([c for c in text if c.isalpha() or c == " "])
                    words = text.split(" ")
                    for word_index, word in enumerate(words):
                        if word.lower() in ["k", "s", "z", "v"]:
                            words[word_index] = ""
                            continue
                        words[word_index] = dic.inserted(word)
                    syllables = []
                    for word in words:
                        syllables.extend(word.split("-"))
                    text = " ".join(
                        syllable for syllable in syllables if syllable != ""
                    )
                    text = '"' + ud.unidecode(text.lower()) + '"'
                    csv_writer.writerow([index, "test", line["metre"][0]["type"], text])
                    index += 1
