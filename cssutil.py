#
#   Written By Dan Monaghan 04/2022 onwards
#

class Project: 
    def __init__(self, name, version, author, github) -> None:
        self.name = name
        self.version = version
        self.author = author
        self.github = github

project = Project(
    'CssUtil', 
    0.2, 
    'Dan Monaghan', 
    'https://github.com/mowglixx/cssutil'
    )

# setup alphabet constant for filename checking
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_UPPER = []
for letter in ALPHABET:
    ALPHABET_UPPER.append(letter.upper())
ALPHABET_UPPER.extend(ALPHABET)


# global css string for output and appending to with header
css = f'''/*
########################################

{project.name} version: {project.version}
By {project.author} <{project.github}>

########################################
*/'''
class_list = [
    '# ', project.name, ' v', str(project.version), '\n',
    '#### Author: ', project.author, ' - ',
    '[Github](', project.github, ')\n',
    '## Class List\n\nThis is the auto generated class list',
    ]
css += '''
:root {
    /* Light and dark colors */
    --light-color: #fff;
    --dark-color: #222;

    /* global color saturation value */
    --color-saturation: 100%;

    /* colors as hsl hue variables*/
    --red-color: 0; 
    --orange-color: 30;
    --yellow-color: 60; 
    --grass-color: 90; 
    --green-color: 120; 
    --teal-color: 150; 
    --cyan-color: 180; 
    --azure-color: 210; 
    --blue-color: 240; 
    --violet-color: 270; 
    --magenta-color: 300;
    --rose-color: 330;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-size: 1em;
    font-family: Arial, sans-serif;
    text-decoration: none;
    border: none;
    cursor: cursor;
}

/* cursor sanity */
button:hover, a:hover{
    cursor: pointer;
}
'''

# hsl in css is a 360deg wheel of color
# below is the 12 distinct colors paired with the degree on the color wheel
hue_colors = {
    0: 'red',
    30: 'orange',
    60: 'yellow',
    90: 'grass',
    120: 'green',
    150: 'teal',
    180: 'cyan',
    210: 'azure',
    240: 'blue',
    270: 'violet',
    300: 'magenta',
    330: 'rose'
}

sizes = [
    0,
    0.5,
    1,
    1.5,
    2,
    3,
    5,
    6.5,
    9]
measuring_step = 0.5

class CSS_Selector:

    def __init__(self, class_name: str = 'class-name', properties: list[str] = ['property: value']) -> str:
        global css
        global class_list

        self.class_name = class_name
        self.properties = properties

        class_list.append(f'\n- `.{self.class_name}`\n')
        for property in properties:
            class_list.append(f'  - `{property}`\n')
        class_list.append(f'\n')
        css += self.return_string()
        # print(f'.{self.class_name}', 'added to css!')

    def return_string(self):
        selector = f'\n.{self.class_name}'+"{\n"
        for i in self.properties:
            selector += f'    {i};\n'
        selector += '}'
        return selector

    def properties(self):
        return self.properties

    def class_name(self):
        return self.class_name


def output_css():

    def check_filename():
        global filename
        global ALPHABET
        legal_symbols = ['.', ' ', '[', ']', '-', '/']
        filename = input('Please input a filename: [main.css]')

        if filename == '':
            filename = 'main.css'

        for char in filename:
            if filename[0] != '.' and char not in ALPHABET and char not in legal_symbols:
                check_filename()
        # if all goes well with the char check, we then check our extension
        strings = filename.split('.')
        if strings[-1].lower() != 'css':
            strings.append('css')
            filename = '.'.join(strings)
        return filename

    def min_filename():
        global filename
        strings = filename.split('.')
        strings.insert(-1, 'min')
        return '.'.join(strings)

    filename = check_filename()

    f = open(filename, "w")  # open the file
    f_min = open(min_filename(), "w")  # open the file
    f.write(css)  # saving the file
    f_min.write(css.strip().replace('\n', '').replace(
        '    ', ''))  # saving the file
    print(f'"./{filename}" and "./{min_filename()}"', 'written successfully!')
    f.close()  # close the file


# initialisation of base classes
CSS_Selector('flex', ['display: flex'])
CSS_Selector('col', ['flex-direction: column'])
CSS_Selector('row', ['flex-direction: row'])
CSS_Selector('flex-wrap', ['flex-wrap: wrap'])
CSS_Selector('flex-nowrap', ['flex-wrap: nowrap'])
CSS_Selector('flex-center', ['justify-content: center'])
CSS_Selector('flex-between', ['justify-content: space-between'])
CSS_Selector('text-center', ['text-align: center'])
CSS_Selector('rounded', ['border-radius: 1em'])
CSS_Selector('bg-dark', ['background-color: var(--dark-color)'])
CSS_Selector('text-dark', ['color: var(--dark-color)'])
CSS_Selector('border-dark', ['border: var(--dark-color) 0.3em solid'])
CSS_Selector('bg-light', ['background-color: var(--light-color)'])
CSS_Selector('text-light', ['color: var(--light-color)'])
CSS_Selector('border-light', ['border: var(--light-color) 0.3em solid'])
CSS_Selector('bright', ['filter: brightness(1)'])
CSS_Selector('bright:hover', ['filter: brightness(1.2)'])
CSS_Selector('active', ['filter: brightness(1.2)'])
CSS_Selector('transition-color', ['transition: color 0.3s'])
CSS_Selector('transition-filter', ['transition: filter 0.3s'])
CSS_Selector('transition-background', ['transition: background 0.3s'])

# uniform sizing (p-*, m-*)
measurements = {
    'm': 'margin',
    'p': 'padding',
    'w': 'width',
    'h': 'height'
}
for (short_bound, bound) in measurements.items():
    count = 0
    while count < 9:
        CSS_Selector(f'{short_bound}-{count}',
                     [f'{bound}: {round(count*measuring_step, 2)}em'])
        count += 1

# individual sizing (.pl-*, .pr-*, .pt-*, pb-*, .ml-*, .mr-*, .mt-*, mb-*)
directions = {'l': 'left', 'r': 'right', 't': 'top', 'b': 'bottom'}
measurements = {
    'm': 'margin',
    'p': 'padding',
}

for (short_bound, bound) in measurements.items():
    count = 0
    while count < 9:
        for (shortdir, dir) in directions.items():
            CSS_Selector(f'{short_bound}{shortdir}-{count}',
                         [f'{bound}-{dir}: {round(count*measuring_step, 2)}em'])
        count += 1

# combined sizes (px-*, mx-*)
directions = {
    'x': [
        'left',
        'right'],
    'y': [
        'top',
        'bottom']}
measurements = {
    'm': 'margin',
    'p': 'padding'
}

for (axis, dir) in directions.items():
    for (short_bound, property) in measurements.items():
        for mult in range(0, 9):
            CSS_Selector(
                f'{short_bound}{axis}-{mult}',
                [
                    f'{property}-{dir[0]}: {round(mult*measuring_step, 2)}em',
                    f'{property}-{dir[1]}: {round(mult*measuring_step, 2)}em'
                ])

class_list.append('\n\n## Colours / colors\n')
# color generation
for (hue_color, color) in hue_colors.items():
    class_list.append(f'\n### {color.title()}\n')
    css = css + f'\n/*[ {color} ]*/'
    
    shades = range(1000, 0, -100)
    for shade in shades:
        # if the shade is not 0 or 1000
        if shade not in [0, 1000]:
            # do all of these for each color
            # background
            CSS_Selector(
                f'bg-{color}-{shade}',
                [
                    f'background-color: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%)'
                ])
            for pseudo in ['hover', 'active', 'visited']:
                CSS_Selector(
                    f'bg-{color}-{shade}-{pseudo}:{pseudo}',
                    [
                        f'background-color: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%)'
                    ]
                )

            # text
            CSS_Selector(
                f'text-{color}-{shade}',
                [
                    f'color: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%)'
                ])
            for pseudo in ['hover', 'active', 'visited']:
                CSS_Selector(
                    f'text-{color}-{shade}-{pseudo}:{pseudo}',
                    [
                        f'color: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%)'
                    ])

            # borders
            CSS_Selector(
                f'border-{color}-{shade}',
                [
                    f'border: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%) 0.3em solid'
                ])
            for pseudo in ['hover', 'active', 'visited']:
                CSS_Selector(
                    f'border-{color}-{shade}-{pseudo}:{pseudo}',
                    [
                        f'border: hsl(var(--{color}-color), var(--color-saturation), {shade//10}%) 0.3em solid'
                    ])

print('Everything Seemed to go well...')
# writes the class_list.md file
f = open('class_list.md', "w")  # open the file
class_list
f.write(''.join(class_list))  # saving the file
f.close()  # close the file

output_css()