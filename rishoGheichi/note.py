import re

text = "12564685312322"

def intcommma(value):
    org = str(value)

    new = re.sub(r"(-?\d+)(\d{3})", r'\g<1>,\g<2>', org)

    if org == new:
        return new
    else:
        return intcommma(new)


print(intcommma(text))