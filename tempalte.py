#template.py
import fileinput, re

field_pat = re.compile(r'\[(.+?)\]')

scope = {}

def replacement(match):
    code = match.group(1)
    try:
        return print(str(eval(code, scope)))
    except SyntaxError:
        return ''

if __name__ == "__main__":
    m = re.match(field_pat, '[2+3]')
    replacement(m)
