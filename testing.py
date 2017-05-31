from mpeds.open_ended_coders import SizeCoder

test = SizeCoder()

text_1 = "A crowd of five hundred"
text_2 = 'Five hundred protesters'

sizes_1 = test.getProtestSize(text_1, as_str = True)
sizes_2 = test.getProtestSize(text_2, as_str = True)

print(sizes_1)
print(sizes_2)
