import json
import csv
import os

# Load the JSON poem
with open("data.csv", "w", encoding="utf-8") as f:
    index = 0
    csv_writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["index", "type", "metre", "text"])
    for book_json in os.listdir("corpusCzechVerse/ccv"):
        book = json.load(
            open("corpusCzechVerse/ccv/" + book_json, "r", encoding="utf-8")
        )
        for poem in book:
            poem_body = poem["body"]
            for stanza_index, stanza in enumerate(poem_body):
                for line_index, line in enumerate(stanza):
                    text = '"' + line["text"] + '"'
                    csv_writer.writerow([index, "test", line["metre"][0]["type"], text])
                    index += 1
