"""
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.

Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width.
If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.

Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.


lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]
cur = "The-day-began-as-still-as-


reflowAndJustify(lines, 24) "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

reflowAndJustify(lines, 25) "reflow lines and justify to length 25" =>

        [ "The-day-began-as-still-as"
          "the-----night----abruptly"
          "lighted---with--brilliant"
          "flame" ]

reflowAndJustify(lines, 26) "reflow lines and justify to length 26" =>

        [ "The--day-began-as-still-as",
          "the-night-abruptly-lighted",
          "with----brilliant----flame" ]

reflowAndJustify(lines, 40) "reflow lines and justify to length 40" =>

        [ "The--day--began--as--still--as-the-night",
          "abruptly--lighted--with--brilliant-flame" ]

reflowAndJustify(lines, 14) "reflow lines and justify to length 14" =>

        ['The--day-began',
         'as---still--as',
         'the------night',
         'abruptly',
         'lighted---with',
         'brilliant',
         'flame']

reflowAndJustify(lines, 15) "reflow lines and justify to length 15" =>

        ['The--day--began',
         'as-still-as-the',
         'night--abruptly',
         'lighted----with',
         'brilliant-flame']

lines2 = [ "a b", "c d" ]

reflowAndJustify(lines2, 20) "reflow lines2 and justify to length 20" =>

        ['a------b-----c-----d']

reflowAndJustify(lines2, 4) "reflow lines2 and justify to length 4" =>

        ['a--b',
         'c--d']

reflowAndJustify(lines2, 2) "reflow lines2 and justify to length 2" =>

        ['a',
         'b',
         'c',
         'd']

All Test Cases:
                 lines, reflow width
reflowAndJustify(lines, 24)
reflowAndJustify(lines, 25)
reflowAndJustify(lines, 26)
reflowAndJustify(lines, 40)
reflowAndJustify(lines, 14)
reflowAndJustify(lines, 15)
reflowAndJustify(lines2, 20)
reflowAndJustify(lines2, 4)
reflowAndJustify(lines2, 2)

n = number of words OR total characters
"""
def reflowAndJustify(lines, required_length):
    stop_token = '$'
    lines = lines + [stop_token]
    print(f'input lines:{lines}')
    num_words = 0
    final_agg = []
    cur_words = []
    cur_words_length = 0
    token = '-'

    for line in lines:
        for word in line.split(' '):
            cur_words.append(word)
            num_words += 1
            cur_words_length += len(word)

            cur_sentence_length = cur_words_length + (num_words - 1) * len(token)
            # print(cur_words, cur_sentence_length, num_words)
            if cur_sentence_length == required_length:
                final_agg.append(token.join(cur_words))
                cur_words = []
                num_words = 0
                cur_words_length = 0

            elif cur_sentence_length < required_length and word != stop_token:
                continue
            elif cur_sentence_length > required_length or word == stop_token:
                # print(cur_words)
                cur_words.pop()

                if num_words - 1 == 0:
                    print("Error, required_length: {required_length} is too small for word: {word}")
                    return
                elif num_words - 1 == 1:
                    final_agg.append(cur_words[0])

                elif num_words - 1 > 1:
                    cur_sentence_length = (cur_words_length - len(word)) + (num_words - 2) * len(token)
                    remaining = required_length - cur_sentence_length
                    roubin_idx = 0
                    while roubin_idx < remaining:
                        word_idx = roubin_idx % (num_words - 2)
                        cur_words[word_idx] += token
                        roubin_idx += 1
                    final_agg.append(token.join(cur_words))

                cur_words = [word]
                num_words = 1
                cur_words_length = len(word)

    print(f'last:{cur_words}')
    print(final_agg)

lines = ["The day began as still as the",
         "night abruptly lighted with",
         "brilliant flame"]
reflowAndJustify(lines, 26)

lines = ["The day began as still as the", "night abruptly lighted with", "brilliant flame"]
lines2 = ["a b", "c d" ]
reflowAndJustify(lines2, 4)
reflowAndJustify(lines2, 20)


def wrapLines(words, max_length):
    aggregator = []
    cur_word = ''

    for word in words:
        # print(f'cur_word:{cur_word}')
        if cur_word == '':
            new_word = word
        else:
            new_word = f'{cur_word}-{word}'

        if len(new_word) > max_length:
            aggregator.append(cur_word)
            cur_word = word
        else:
            cur_word = new_word

    if cur_word:
        aggregator.append(cur_word)

    print(aggregator)
    print('\n')
    return aggregator
