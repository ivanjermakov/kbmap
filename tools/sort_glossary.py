with open('../../kbmap.wiki/Glossary.md') as f:
    sep = '\n\n'
    for l in sorted(f.read().split(sep)):
        print(l, end=('%s' % sep))
