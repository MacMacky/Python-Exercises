
def hello_name(name=""):
    return "Hello " + name + "1"


def make_abba(a="", b=""):
    return a + b + b + a


def make_tags(tag="", word=""):
    return '<' + tag + '>' + word + '</' + tag + '>'


def make_out_word(out, word):
    lenOut = len(out)
    return out[0:lenOut-2] + word + out[lenOut-2:lenOut]


def extra_end(string=""):
    lengtho = len(string)
    return string[lengtho-2:lengtho] * 3


def first_two(string=""):
    return string[0:2]


def first_half(string=""):
    return string[0:len(string)//2]


print(first_half("HelloThere"))
