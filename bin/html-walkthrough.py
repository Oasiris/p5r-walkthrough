#!/usr/bin/python3
import sys
import subprocess

HEADER = '\n'.join((
    '<!doctype html>',
    '<html lang="en">',
    '<head>',
    '<meta charset="utf-8">',
    '<title>Persona 5 Royal Walkthrough - {}</title>',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<link rel="icon" type="image/x-icon" href="/favicon.ico">',
    '<link rel="stylesheet" type="text/css" href="normalize.css">',
    '<link rel="stylesheet" type="text/css" href="style.css">',
    # '<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&display=swap" rel="stylesheet">',
    # '<link href="https://fonts.googleapis.com/css2?family=Darker+Grotesque:wght@700;800&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700;900&display=swap" rel="stylesheet">',
    '</head>',
    '<body>',
    '<div>',
    '<h1>Persona 5 Walkthrough - Version {}</h1>',
    '<h2>Navigation</h2>',
    '<ul id="navigation">',
    '<li><a href="/">Home</a></li>'
))

PAGES = [
    ('src/introduction', 'Introduction'),
    ('src/overworld', 'Overworld'),
    ('src/metaverse', 'Metaverse'),
    ('dist/walkthrough', 'Walkthrough'),
    ('dist/ace-walkthrough', 'All Confidant Events Walkthrough'),
    ('src/confidants', 'Confidants'),
    ('src/achievements', 'Achievements')
]

NAVBAR = '\n'.join(['<li><a href="{}">{}</a></li>'.format(
    x[0].split('/')[1] + '.html',
    x[1]
) for x in PAGES])

VERSION = sys.argv[1]

for src, title in PAGES:
    fname = 'dist/' + src.split('/')[1] + '.html'
    subprocess.call(['npx', 'showdown', 'makehtml', '--tables', '-i', src + '.md', '-o', fname])

    with open(fname) as htmlfile:
        lines = htmlfile.read()

    if src == 'src/achievements':
        print(lines)

    lines = '\n'.join([
        HEADER.format(title, VERSION),
        NAVBAR,
        '</ul>',
        lines,
        '</div>\n</body>\n</html>'
    ])

    with open(fname, 'w+') as htmlfile:
        htmlfile.write(lines)
