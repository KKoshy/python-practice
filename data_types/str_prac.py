"""
This file holds the practice on Dictionary
"""

# swapping case
sample = "Www.HackerRank.com"
print(sample.swapcase())
print(sample.upper())
print(sample.lower())
print(len(sample))
print(sample.replace("Rank", "trade"))

# str is immutable; to modify char at a position.
ex_01 = "filolo"
post = 4
new_char = "a"
print(ex_01[:post]+ new_char + ex_01[post+1:])

# wrapping text
import textwrap
text = """
There shall be showers of blessings; this is the promise of Lord.
There shall be seasons refreshing; send from the saviour above.
Showers of blessings; showers of blessings we need.
Mercy drops round us are falling.
But for the showers we plead.
"""
wrap_text = textwrap.wrap(text=text, width=20)
print(wrap_text)

fill_text = textwrap.fill(text=text, width=20)
print(fill_text)
