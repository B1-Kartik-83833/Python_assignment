def find_longest_word(word_list):

    if not word_list:
        return 0, None
    max_len = len(word_list[0])
    longest_word = word_list[0]
    for word in word_list:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    return max_len, longest_word


words = ['one', 'two', 'three', 'four', 'five']
longest_length, longest_word = find_longest_word(words)
print(f"length of longest word :{longest_length},word:{longest_word}")