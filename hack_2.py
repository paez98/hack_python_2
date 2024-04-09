"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

vowels = 'aeiou'
def fn_hack_2(s):
    new_string = ''.join(x for x in s if x not in vowels)
    print(new_string)
    return new_string


fn_hack_2('fooziman')
fn_hack_2('barziman')
fn_hack_2('qux')