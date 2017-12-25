import re
import numpy as np

__russian_word = re.compile("[а-яА-Я]+")

def tokens_to_freq(tokens):
    words, count = np.unique(tokens, return_counts=True)
    return [words, count]


def tokenize(line, stopwords):
    result = line.split(" ")
    if not stopwords:
        return result
    filtered_result = []
    for token in result:
        if token not in stopwords and token != '':# and __russian_word.match(token):
            filtered_result.append(token)
    return filtered_result


def combine_token_sets(tokens_array):
    res = []
    for tokens in tokens_array:
        for token in tokens:
            res.append(token)
    return res


def tokens_freq_to_matrix(tokens_freq, documents_array):
    names = np.unique(combine_token_sets([x[0] for x in tokens_freq]))

#    for k in range(0, len(tokens_freq)):
#        for i in range(0, len(tokens_freq[k][0])):
#            print(str(i) + ": " + tokens_freq[k][0][i])

    documents = []
    for k in range(0, len(tokens_freq)):
        if documents_array:
            documents.append(documents_array[k])
        else:
            documents.append("Unnamed№"+str(k+1))
    tokens = []
    summary = []
    summary_docs = []
    for i in range(0, len(names)):
        word_line = []
        summary_line = 0
        summary_docs_count = 0
        for k in range(0, len(tokens_freq)):
            if len(tokens_freq[k][0]) != 0 and names[i] in tokens_freq[k][0]:
                freq = tokens_freq[k][1][np.where(tokens_freq[k][0] == names[i])[0]][0]
                word_line.append(freq)
                summary_line += freq
                summary_docs_count += 1
            else:
                word_line.append(0)
        tokens.append(word_line)
        summary.append(summary_line)
        summary_docs.append(summary_docs_count)
        #print(str(names[i]) + ":" + str(summary[i])+":"+str(summary_docs_count))

    # for k in range(0, len(tokens_freq)):
    # for i in range(0, len(names)):
    #    print(str(i) + ": " + names[i] + " x "+str(summary_docs[i]))
    return [names, documents, tokens, summary, summary_docs]


def clear_matrix(tokens_matr):
    names = []
    documents = tokens_matr[1]
    tokens = []
    for i in range(0, len(tokens_matr[0])):
        if tokens_matr[4][i] > 1 and tokens_matr[3][i] > 1:
            names.append(tokens_matr[0][i])
            tokens.append(tokens_matr[2][i])
    return [names, documents, tokens]


def remove_punctuations(line):
    first_pass = re.sub("([,.!?+\-*/=()\[\]<>@#№\"$;%:^•«»\n„“—–])", "", line)
    return re.sub("(  )", " ", first_pass)



