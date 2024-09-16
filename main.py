import compoments.utils as utils
# import compoments.WordDictionnary as dictio


# test = utils.SecretWord()
# print(test)

import re


input_string = "Hello, World!"
symbol = "*"
modified_str = re.sub(r".", symbol, input_string)
print(modified_str)  # Output: *************