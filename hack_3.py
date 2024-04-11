"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

vowels = {
    'a' : '@',
    'e' : '3',
    'i' : '¡',
    'o' : '0',
    'u' : 'v'
}
num = '123456789'
r = vowels.items()
print(r)
def fn_hack_3(s):
    for x,y in vowels.items():
        s = s.replace(x,y)
    if s.startswith('3'):
        result = s[0] + s[1].upper()
    elif  len(s) > 4:
        result = s[0].upper() + s[1:7] + s[7].upper()
    elif len(s) ==3:
        result = s[0].upper() + s[1:2] + s[2].upper()
    elif len(s) == 2:
        result = s[0].upper() + s[1]
    
        
    print(result)
    
    
    return result

fn_hack_3('fooziman')
fn_hack_3('barziman')
fn_hack_3('3q')
fn_hack_3('qu')
fn_hack_3('qvx')