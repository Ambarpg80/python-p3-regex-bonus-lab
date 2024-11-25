import re

my_pattern = r"[A-z]*\'*[A-z]\s[A-z' ]*today'*[a-z, ]*[.\?]+"
my_regex = re.compile(my_pattern)
print(my_regex)
# ([A-z]\'[A-z]\.)|([A-z]\'[A-z]\,[A-z]\?)
#"It's such a lovely day today.|Some weather we're having today\, huh\?|Maybe today's just not my day."