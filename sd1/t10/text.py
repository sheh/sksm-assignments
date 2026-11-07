from typing import List

class Text:
    def __init__(self, text):
        self.t = text

    def process(self):
        return Text(self.t.upper())
    
    def trim(self):
        return Text(self.t.strip())
    
    def reverse(self):
        return Text(self.t[::-1])
    
    def length(self):
        return len(self.t)
    
    def __add__(self, other):
        return Text(self.t + other.t)
    
    def to_lower(self):
        return Text(self.t.lower())
    
    def to_upper(self):
        return Text(self.t.upper())
    
    def to_capitalize(self):
        return Text(self.t.capitalize())
    
    def split(self, separator) -> List:
        return [Text(part) for part in self.t.split(separator)]
    
    def __eq__(self, value: object):
        return self.t == value.t