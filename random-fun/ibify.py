#!/usr/bin/python

import argparse

ADDITIONAL_SYMBOLS = [
    "int", "sum", "bigcup", "bigcap", "partial", "prod"
]


def main():
    parser = argparse.ArgumentParser(
        prog='IBify',
        description='Converts LaTeX file to IB notation.'
    )
    parser.add_argument('filename')
    parser.add_argument('-d', '--display_only', action='store_true')

    args = parser.parse_args()

    file_in = open(args.filename, 'r', encoding='utf-8')
    name, extension = tuple(args.filename.split('.'))
    file_out = open(f'{name}_ib.{extension}', 'w+', encoding='utf-8')

    reading_math = False
    file_contents = file_in.read()

    index = 0
    while index < len(file_contents):
        symbol = file_contents[index]
        if symbol == r'$' and not args.display_only:
            reading_math = not reading_math
            file_out.write(symbol)
            index += 1
            continue
        if (symbol == '\\' and file_contents[index + 1] == '[' and not
                reading_math):
            reading_math = True
            index += 2
            file_out.write('\\[')
            print("Start display math")
            continue
        if (symbol == '\\' and file_contents[index + 1] == ']' and
                reading_math):
            reading_math = False
            index += 2
            file_out.write('\\]')
            print("End display math")
            continue
        if not reading_math:
            file_out.write(symbol)
            index += 1
            continue

        text_to_write = symbol
        if text_to_write in ['(', '[', ')', ']']:
            text_to_write = r'\reflectbox{' + text_to_write + '}'

        if symbol == '\\':
            index += 1
            while (index < len(file_contents) and
                   file_contents[index].isalpha()):
                text_to_write += file_contents[index]
                index += 1
            text_to_write += file_contents[index]

            if text_to_write[1:-1] in ["left", "right"]:
                print(text_to_write)
                if text_to_write[-1] in ['(', '[', '{', ')', ']', '}']:
                    text_to_write = r'\reflectbox{' + text_to_write + '}'

            if len(text_to_write) == r'\{':
                text_to_write = r'\reflectbox{' + text_to_write + '}'

            if text_to_write[1:-1] in ADDITIONAL_SYMBOLS:
                text_to_write = (r'\reflectbox{' + text_to_write[:-1] + '}' +
                                 text_to_write[-1])

        file_out.write(text_to_write)
        index += 1

    file_in.close()
    file_out.close()


if __name__ == '__main__':
    main()
