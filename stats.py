def word_split(text):
    split_words = text.split()
    return split_words

def stats(text):
    lowered_text = text.lower()
    count = {}
    for i in lowered_text:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    res = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    return res