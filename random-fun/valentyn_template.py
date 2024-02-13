import os
from odf.opendocument import load
from odf.style import Style, TextProperties
from odf.text import P

for letter in os.listdir("letters"):
    with open(f"letters/{letter}", "r", encoding="utf-8") as f:
        if ".odt" in letter or ".pdf" in letter:
            continue
        text = f.read()
    lines = [line for line in text.split("\n") if line != ""]

    textdoc = load("letter-template.odt")

    # First paragraph
    first = textdoc.text.getElementsByType(P)[0]

    # Styles
    normalstyle = Style(name="Normal", family="text")
    normalprop = TextProperties(
        attributes={"fontweight": "normal", "fontfamily": "Parisienne"}
    )
    normalstyle.addElement(normalprop)
    boldstyle = Style(name="Bold", family="paragraph")
    boldprop = TextProperties(
        attributes={"fontweight": "bold", "fontfamily": "Parisienne"}
    )
    boldstyle.addElement(boldprop)
    textdoc.styles.addElement(normalstyle)
    textdoc.styles.addElement(boldstyle)

    # Text
    p = P(text=lines[0], stylename=boldstyle)
    first.parentNode.insertBefore(p, first)

    for line in lines[1:]:
        p = P(stylename=normalstyle, text=line)
        first.parentNode.insertBefore(p, first)

    textdoc.save(f"letters/{letter.replace(".txt", ".odt")}")
