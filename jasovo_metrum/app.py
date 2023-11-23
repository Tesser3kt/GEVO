import json
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_text as tf_text
import pickle


def filter_train(line):
    split = tf.strings.split(line, ",", maxsplit=3)
    return split[1] == "train" and split[2] != "N"


def build_vocabulary(ds_train):
    vocabulary = set()
    vocabulary.update(["sostoken"])
    vocabulary.update(["eostoken"])

    for line in ds_train:
        split = tf.strings.split(line, ",", maxsplit=3)
        text = split[3]
        tokenized_text = tokenizer.tokenize(text.numpy().decode("utf-8").lower())
        vocabulary.update(tokenized_text)

    return vocabulary


poem = json.load(open("corpusCzechVerse/ccv/0001.json", "r", encoding="utf-8"))

ds_train = tf.data.TextLineDataset("data.csv")
ds_test = tf.data.TextLineDataset("data.csv")

tokenizer = tf_text.WhitespaceTokenizer()

# Build vocabulary and save it
vocabulary = build_vocabulary(ds_train)
voc_file = open("vocabulary.obj", "wb")
pickle.dump(vocabulary, voc_file)
