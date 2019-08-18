def encode_string(input_str):
    if len(input_str) == 0:
        return ""

    new_char = input_str[0]
    char_count = 0
    output_str = new_char
    for char in input_str:
        if char == new_char:
            char_count += 1
        else:
            output_str = output_str + str(char_count)
            output_str = output_str + char
            new_char = char
            char_count = 1

    output_str = output_str + str(char_count)
    return output_str


out = encode_string("aaaabbbcaaa")
print(out)
# output_str = "a4b3c1a3"


def encode_string_rev(inputString):
    if len(inputString) == 0:
        return ""

    new_char = inputString[0]
    char_count = 0
    output_str = ""
    for char in inputString:
        if char == new_char:
            char_count += 1
        else:
            output_str = output_str + str(char_count)
            output_str = output_str + new_char
            new_char = char
            char_count = 1

    output_str = output_str + str(char_count) + new_char
    return output_str


out = encode_string_rev("aaaabbbcaaa")
# out = encode_string("GGGGGrrrrrrrrrrt")
print(out)
# output_str = "a4b3c1a3"
