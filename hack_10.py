"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(text):
    output = [{str(i*2+1): str(i*2+2)} for i in range(len(text))]
    print(output)
    return output

text = [{"a":"b"},{"c":"d"},{"e":"f"}]
fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}])


# def fn_hack_10(s):
#     result = s
#     #...
#     return result
