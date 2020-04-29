from c_point import point
import functions as func
import json
import re

txt = [' 123456789123', 'asd asd asd']
for t in txt:
    if re.search("[0-9]{9}", t):
        print("Got")

