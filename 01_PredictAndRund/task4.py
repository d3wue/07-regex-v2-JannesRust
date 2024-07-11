import re

reg = re.compile("([A-Z][a-z]+) ([A-Z]*)( )?([A-Z][a-z]+)")
m = reg.match("Hanna J Gruber")
print(m)
print(m.group(2))

m = reg.match("Hanna Gruber")
print(m)
print(m.group(4))

m = reg.match("Hanna Jana Gruber")
print(m)
print(m.group(4))

m = reg.match("Albert KD Klein")
print(m)
print(m.group(2))

m = reg.match("Christoph M Flath")
print(m)
print(m.group(2))

m = reg.search("Hanna J Gruber, PhD")
print(m)
print(m.group(2))

m = reg.search("xw. Alfred Nobel")
print(m)
print(m.group(2))