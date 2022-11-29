ini_string = input().split()

string_list = [ini_string, [], [], [], []]
puncs_list = ['.', '!', '?', ',']

for i in range(len(puncs_list)):
    for word in string_list[i]:
        if puncs_list[i] in word:
            new_words = []

            if word.index(puncs_list[i]) == 0:
                new_words.append(puncs_list[i])

            new_words_cut = word.split(puncs_list[i])

            for new_word in new_words_cut:
                if new_word != '':
                    new_words.append(new_word)
                    new_words.append(puncs_list[i])

            if word[-1] != puncs_list[i]:
                new_words.pop(-1)

            for new_word in new_words:
                string_list[i+1].append(new_word)

        else:
            string_list[i+1].append(word)

ini_sep_string = string_list[-1]

ini_sep_string[0] = ini_sep_string[0][0].upper() + ini_sep_string[0][1:]

for sign in puncs_list[0: 3]:
    for i in range(1, len(ini_sep_string)):
        if ini_sep_string[i - 1] == sign:
            ini_sep_string[i] = ini_sep_string[i][0].upper() + ini_sep_string[i][1:]

sep_string_list = [ini_sep_string, [], [], [], []]
for j in range(len(puncs_list)):
    for i in range(len(sep_string_list[j])):
        if i != len(sep_string_list[j]) - 1 and sep_string_list[j][i + 1] == puncs_list[j]:
            sep_string_list[j + 1].append(sep_string_list[j][i] + puncs_list[j])
        elif sep_string_list[j][i] != puncs_list[j]:
            sep_string_list[j + 1].append(sep_string_list[j][i])

print(' '.join(sep_string_list[-1]))
