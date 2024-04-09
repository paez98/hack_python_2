"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""
char = ['f','b','n']

def fn_hack_4(s):
    result = ''.join(x for x in s if x not in char)
    print(result)
    return result


fn_hack_4('fooziman')
fn_hack_4('barziman')
fn_hack_4('qux')