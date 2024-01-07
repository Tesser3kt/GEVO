import numpy as np
import tensorflow as tf
import pyphen
import unidecode as ud
from config import CAT_TO_METRE


def file_to_dataset(filename, batch_size=32):
    """Reads verses from a file and converts them to a dataset."""

    dic = pyphen.Pyphen(lang="cs_CZ")
    with open(filename, "r", encoding="utf-8") as f:
        verses = []

        for line in f:
            line = line.strip()
            line = "".join([c for c in line if c.isalpha() or c == " "])
            words = line.split(" ")

            for word_index, word in enumerate(words):
                if word.lower() in ["k", "s", "z", "v"]:
                    words[word_index] = ""
                    continue
                words[word_index] = dic.inserted(word)

            syllables = []
            for word in words:
                syllables.extend(word.split("-"))
            text = " ".join(syllable for syllable in syllables if syllable != "")
            text = ud.unidecode(text.lower())
            verses.append(text)

    return (
        tf.data.Dataset.from_tensor_slices(verses)
        .batch(batch_size)
        .prefetch(tf.data.AUTOTUNE)
    )


data = file_to_dataset("verses.txt")
print(list(data)[0])
model = tf.keras.models.load_model("metre_detector.tf")
predictions = model.predict(data)
print(np.argmax(predictions, axis=1))