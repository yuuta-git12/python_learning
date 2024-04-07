import string

s = """\
Hi $name.
$contents
Have a good day
"""

# Template()関数
# 標準ライブラリのstringをimportすることで使用可能
t = string.Template(s)
contents = t.substitute(name='Mike', contents='How are you?')
print(contents)

with open('/usr/src/app/design/email_template.txt') as f:
    t2 = string.Template(f.read())

contents = t2.substitute(name='Mike', contents='How are you?')
print(contents)