def rearrangeTheSentence(sentence):
    dot_exists = False
    if sentence[-1] == ".":
        sentence = sentence[:-1]
        dot_exists = True
    arr = sentence.split(' ')
    n = len(arr)
    arr[0] = arr[0].lower()

    for i in range(1, n):
        word = arr[i]
        j = i - 1
        while j >= 0 and len(word) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = word

    arr[0] = arr[0].title()
    result = " ".join(arr)
    if dot_exists:
        result = result + "."
    return result


if __name__ == "__main__":
    # sentence = "Houston we have a problem"
    sentence = "It is in the sun the beach hottest."
    res = rearrangeTheSentence(sentence)
    print(res)
