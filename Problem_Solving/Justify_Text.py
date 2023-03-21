# Atharv Kolhar
# Python Bytes


"""
Justify Text:
Given a sequence of words and an integer line length k, return a list of strings which represents each line,
fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between
each word. Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def justify(word_list, line_length):
    line_list = []
    line = []
    length_remaining = line_length
    space = 0
    for word in word_list:
        if length_remaining <= len(word) + space:
            line_list.append(line)
            line = []
            length_remaining = line_length
            space = 0
        line.append(word)
        length_remaining -= len(word)
        space += 1

    line_list.append(line)

    for l in line_list:
        len_char = len("".join(l))
        spaces_available = line_length - len_char

        spaces = " " * (spaces_available // (len(l)-1))
        print(spaces_available)
        f_l = spaces.join(l)
        print(len(f_l))


    return line_list


a = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
lines = justify(a, 16)
print(lines)
for line in lines:
    print(len(line))