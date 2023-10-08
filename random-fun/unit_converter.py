class UnitConverter:
    def __init__(self):
        self.unit_types = {
            'a': 'Area',
            'd': 'Data',
            'e': 'Energy',
            'f': 'Frequency',
            'o': 'Force',
            'l': 'Length',
            'n': 'Number Systems',
            'w': 'Power',
            'p': 'Pressure',
            's': 'Speed',
            't': 'Temperature',
            'i': 'Time',
            'v': 'Volume',
            'm': 'Weight and Mass'
        }
        self.prefixes = {
            'Q': 10**30,
            'R': 10**27,
            'Y': 10**24,
            'Z': 10**21,
            'E': 10**18,
            'P': 10**15,
            'T': 10**12,
            'G': 10**9,
            'M': 10**6,
            'k': 10**3,
            'h': 10**2,
            'da': 10**1,
            'dk': 10**1,
            '': 1,
            'd': 10**-1,
            'c': 10**-2,
            'm': 10**-3,
            'u': 10**-6,
            'n': 10**-9,
            'p': 10**-12,
            'f': 10**-15,
            'a': 10**-18,
            'z': 10**-21,
            'y': 10**-24,
            'r': 10**-27,
            'q': 10**-30
        }
        self.bases = {
            'a': 'm2',
            'd': 'b',
            'e': 'J',
            'f': 'Hz',
            'o': 'N',
            'l': 'm',
            'n': 'dec',
            'w': 'W',
            'p': 'Pa',
            's': 'm/s',
            't': 'K',
            'i': 's',
            'v': 'm3',
            'm': 'g'
        }
        self.base_conversions = {
            'a': {
                'm2': 1,
                'a': 10**2
            },
            'd': {
                'b': 1,
                'B': 8
            },
            'e': {
                'J': 1,
                'cal': 4186.8,
                'Wh': 3600,
                'eV': 1.602176634*10**-19
            },
            'f': {
                'Hz': 1,
                'rpm': 1/60
            },
            'o': {
                'N': 1,
                'kgf': 9.80665,
                'dyn': 1/100000
            },
            'l': {
                'm': 1,
                'in': 0.0254,
                'ft': 0.3048,
                'yd': 0.9144,
                'ly': 9460730472580044,
                'au': 149597870691,
                'pc': 30856775812799588,
                'mi': 1609.344,
            },
            'w': {
                'W': 1,
                'hp': 745.69987158227022,
                'cal/h': 0.001162,
            },
            'p': {
                'Pa': 1,
                'bar': 100000,
                'atm': 101325,
                'mmHg': 133.322
            },
            't': {
                'K': (1, 0),
                'C': (1, 273.15),
                'F': (5/9, 459.67),
            },
            'i': {
                's': 1,
                'min': 60,
                'h': 3600,
                'd': 86400,
                'w': 604800,
                'y': 31536000,
                'dec': 315360000,
                'cent': 3153600000
            },
            'v': {
                'm3': 1,
                'l': 0.001,
                'gal': 0.00378541,
                'qt': 0.000946353,
                'tsp': 0.00000492892,
                'tbsp': 0.0000147868,
                'vk': 0.0005
            },
            'm': {
                'g': 1,
                't': 1000000,
                'oz': 28.3495,
                'lb': 453.592,
            }
        }
        self.digits = [
            str(d) for d in range(10)
        ] + [
            letter for letter in map(chr, range(ord('A'), ord('Z')+1))
        ]
        self.conversion_functions = {
            '': self.__typical_convert,
            's': self.__speed_convert,
            'n': self.__number_base_convert,
            't': self.__temperature_convert
        }
        self.precision = 5
        self.max_digits = 9
        self.unit_type = ''
        self.exit = False

    def __typical_convert(self, conversion_data):
        quantity, prefix1, base1, prefix2, base2 = conversion_data[:-1]

        quantity = quantity * self.prefixes[prefix1]
        base1_quantity = (quantity *
                          self.base_conversions[self.unit_type][base1])
        base2_quantity = (base1_quantity /
                          self.base_conversions[self.unit_type][base2])
        prefix2_quantity = base2_quantity / self.prefixes[prefix2]

        return prefix2_quantity

    def __speed_convert(self, conversion_data):
        quantity, prefix_l1, base_l1, base_t1, prefix_l2, base_l2, base_t2 = (
            conversion_data[:-1])

        quantity = quantity * self.prefixes[prefix_l1]
        base_l1_quantity = (quantity *
                            self.base_conversions['l'][base_l1])
        base_t1_quantity = (base_l1_quantity /
                            self.base_conversions['i'][base_t1])
        base_t2_quantity = (base_t1_quantity *
                            self.base_conversions['i'][base_t2])
        base_l2_quantity = (base_t2_quantity /
                            self.base_conversions['l'][base_l2])
        prefix_l2_quantity = base_l2_quantity / self.prefixes[prefix_l2]

        return prefix_l2_quantity

    def __to_decimal(self, number, base):
        result = 0

        power = len(number) - 1
        for digit in number:
            if digit not in self.digits[:base]:
                print('Invalid digit {} for base {}.'.format(digit, base))
                return None
            result += self.digits.index(digit) * base**power
            power -= 1
        return result

    def __from_decimal(self, number: int, base: int) -> str:
        result = ''
        while number:
            result += self.digits[int(number % base)]
            number //= base
        return result[::-1]

    def __number_base_convert(self, conversion_data):
        quantity, base1, base2 = conversion_data[:-1]

        decimal = self.__to_decimal(quantity, base1)
        if decimal is None:
            return None
        return self.__from_decimal(decimal, base2)

    def __temperature_convert(self, conversion_data):
        quantity, prefix1, base1, prefix2, base2 = conversion_data[:-1]

        quantity = quantity * self.prefixes[prefix1]
        base1_quantity = (
            (quantity + self.base_conversions['t'][base1][1]) *
            self.base_conversions['t'][base1][0]
        )
        base2_quantity = (
            (base1_quantity / self.base_conversions['t'][base2][0])
            - self.base_conversions['t'][base2][1]
        )
        prefix2_quantity = base2_quantity / self.prefixes[prefix2]

        return prefix2_quantity

    def print_unit_types(self):
        print('List of unit types:')
        for key, value in self.unit_types.items():
            print('{} - {}'.format(key, value))

    def split_unit(self, unit):
        if not len(unit):
            return ('', '')

        if len(unit) == 1 or unit in self.base_conversions[self.unit_type]:
            return ('', unit)

        if unit[:2] in self.prefixes and len(unit) > 2:
            return (unit[:2], unit[2:])

        return (unit[0], unit[1:])

    def split_speed_unit(self, unit):
        if '/' not in unit:
            return ('', '', '')

        unit_l, base_t = unit.split('/')
        prefix_l, base_l = self.split_unit(unit_l)
        return (prefix_l, base_l, base_t)

    def typical_conversion(self, quantity, unit1, unit2):
        conversion_data = quantity,
        for unit in unit1, unit2:
            prefix, base = self.split_unit(unit)
            if base == '':
                print('Invalid unit. Base left empty.')
                return None
            if base not in self.base_conversions[self.unit_type]:
                print(
                    ('Invalid unit. Base {} unknown for unit'.format(base) +
                     ' type {}.'.format(self.unit_types[self.unit_type]))
                )
                return None
            if prefix not in self.prefixes:
                print('Invalid unit. Prefix {} unknown.'.format(prefix))
                return None
            conversion_data += (prefix, base)

        if self.unit_type == 't':
            return conversion_data + ('t',)
        return conversion_data + ('',)

    def speed_conversion(self, quantity, unit1, unit2):
        conversion_data = quantity,
        for unit in unit1, unit2:
            prefix_l, base_l, base_t = self.split_speed_unit(unit)
            if (prefix_l == '' and base_l == '' and base_t == ''):
                print('Invalid unit of speed. Possibly a missing "/"?')
                return None
            if base_l == '':
                print('Invalid unit of length. Base left empty.')
                return None
            if base_t == '':
                print('Invalid unit of time. Base left empty.')
                return None
            if base_l not in self.base_conversions['l']:
                print(
                    ('Invalid unit of length. ' +
                     'Base {} unknown for '.format(base_l) +
                     'unit type {}.'.format(self.unit_types['l']))
                )
                return None
            if base_t not in self.base_conversions['i']:
                print(
                    ('Invalid unit of time. ' +
                     'Base {} unknown for '.format(base_t) +
                     'unit type {}.'.format(self.unit_types['i']))
                )
                return None
            if prefix_l not in self.prefixes:
                print('Invalid unit of length. Prefix {} unknown.'
                      .format(prefix_l))
                return None
            conversion_data += (prefix_l, base_l, base_t)
        return conversion_data + ('s',)

    def number_base_conversion(self, quantity, unit1, unit2):
        if '.' in str(quantity):
            print('Invalid number to convert. Decimals not yet supported. :(')
            return None
        conversion_data = quantity,
        for unit in unit1, unit2:
            try:
                base = int(unit)
            except ValueError:
                print(('Invalid numeral system base. Enter a whole number ' +
                       'greater or equal to 2.'))
                return None

            if base < 2:
                print(('Invalid numeral system base. Enter a whole number ' +
                       'greater or equal to 2.'))
                return None

            conversion_data += (base,)
        return conversion_data + ('n',)

    def convert(self, conversion_data):
        return self.conversion_functions[conversion_data[-1]](conversion_data)

    def get_unit_type(self):
        answer = input(('Enter unit type, "L" to see list of available unit ' +
                        'types, "P" to change maximum precision or leave ' +
                        'blank to exit: '))
        if answer == '':
            self.exit = True
            return

        if answer == 'L':
            self.print_unit_types()
            self.get_unit_type()
            return

        if answer == 'P':
            self.change_precision()
            self.get_unit_type()
            return

        if answer not in self.unit_types:
            print('Invalid unit type.')
            self.get_unit_type()
            return

        self.unit_type = answer

    def get_conversion_data(self):
        print(('Enter desired conversion as "quantity unit_from unit_to" ' +
               '(like "100 m km") or leave blank to exit.'))

        answer = input('Enter conversion: ')
        if answer == '':
            self.exit = True
            return None

        try:
            quantity, unit1, unit2 = answer.split()
        except ValueError:
            print('Invalid conversion format.')
            return None

        if self.unit_type == 'n':
            return self.number_base_conversion(quantity, unit1, unit2)

        try:
            quantity = eval(quantity)
            quantity = float(quantity)
        except Exception:
            print('Invalid quantity. Failed to evaluate expression or the ' +
                  'expression equals not a number.')
            return None

        if self.unit_type == 's':
            self.unit_type = 'l'
            return self.speed_conversion(quantity, unit1, unit2)

        return self.typical_conversion(quantity, unit1, unit2)

    def change_precision(self):
        answer = input('Enter new precision: ')
        try:
            self.precision = int(answer)
        except ValueError:
            print('Invalid precision. Enter an integer.')
            return

        print('Precision changed to {}.'.format(self.precision))


uc = UnitConverter()
uc.print_unit_types()
while not uc.exit:
    uc.get_unit_type()
    if uc.exit:
        break

    conversion_data = uc.get_conversion_data()
    if uc.exit:
        break
    if not conversion_data:
        continue

    try:
        result = uc.convert(conversion_data)
    except Exception:
        print('Unknown error.')
        continue

    if result is None:
        continue

    if uc.unit_type == 'n':
        print('Result: {}'.format(result))
        continue

    if len(str(result)) > uc.max_digits:
        print('Result: {:.{prec}e}'.format(result, prec=uc.precision))
    else:
        print('Result: {}'.format(round(result, uc.precision)))
