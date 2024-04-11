"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    if len(s) > 3:
        result = s[0] + s[1].upper() + s[2:4] + s[4].upper() + s[5:]
    elif len(s) == 3:
        result = s[0] + s[1].upper() + s[2:]
        
    else:
        result = s
    print(result)
    return result

fn_hack_1('fooziman')
fn_hack_1('qux')
fn_hack_1('eq')