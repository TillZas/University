import fileloader as fl
import StemmerPorter as sp
import textEdition as te
from sklearn.feature_extraction.text import TfidfTransformer
from mpl_toolkits.mplot3d import Axes3D
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

from sklearn.datasets import fetch_20newsgroups

# ##############################################################################
# categories = [
#     'alt.atheism',
#     'talk.religion.misc',
#     'comp.graphics',
#     'sci.space',
# ]
#
# print("Loading 20 newsgroups dataset for categories:")
# print(categories)
#
# dataset = fetch_20newsgroups(subset='all', categories=categories,
#                              shuffle=True, random_state=42)
#
# print("%d documents" % len(dataset.data))
# print("%d categories" % len(dataset.target_names))
# print()
# ##############################################################################

draw_words = True
draw_words_names = True

draw_article_names = True

draw_3D = True

swords = []
file = open("stopwords.txt", "r")
for line in file:
    swords.append(line[:len(line)-1])
file.close()

colors=['#FF0000', '#FF00FF', '#0000FF', '#00E6FF', '#00FF3C', '#E6FF00', '#FF9100', '#DCAFAF']
#colors = ListedColormap(['#FF0000', '#FF00FF', '#0000FF', '#00E6FF', '#00FF3C', '#E6FF00', '#FF9100', '#DCAFAF'])

tfidf = TfidfTransformer(smooth_idf=False)
documents_color = []
documents_names = []
groups = []
counts = []
groupAmount = fl.get_groups_amount()
for dir_id in range(0, groupAmount):
    files, groupName = fl.get_group(dir_id, True)
    groups.append(groupName)
    print("Group "+groupName+" processing!")
    for fileName in files:
        file = open(fileName[0], "r")#, encoding='utf-8')
        tokens = []
        for line in file:
            tokens = te.combine_token_sets(
                [tokens,
                 te.tokenize(te.remove_punctuations(line), swords)]
            )
        file.close()
        #tokens = [sp.stem(x) for x in tokens]
        counts.append(te.tokens_to_freq(tokens))
        documents_color.append(dir_id)
        documents_names.append(fileName[1])
    print("Done!")
    print("-----------------------------------------")
print("Calculating")
res = te.tokens_freq_to_matrix(counts, documents_names)
res = te.clear_matrix(res)
matrix = res[2]
#matrix = tfidf.fit_transform(matrix).toarray()
u, s, v = linalg.svd(matrix,compute_uv=True, full_matrices=True)
print("Done!")
print("-----------------------------------------")
# print(str(len(u))+":"+str(len(u[0])))
# print(s)
# print(str(len(v))+":"+str(len(v[0])))

print("Drawing")

draw_matr = []
for i in range(0, groupAmount):
    draw_matr.append([])

for i in range(0, len(documents_color)):
    draw_matr[documents_color[i]].append([v[0][i], v[1][i], v[2][i]])


fig = plt.figure()

if draw_3D:
    ax = fig.add_subplot(111, projection='3d')
    if draw_words:
        if draw_words_names:
            for i in range(0,len(u[0])):
                ax.text(u[i][0], u[i][1],u[i][2], res[0][i], fontsize=10)
                #ax.text(u[0][i], u[1][i], u[2][i], res[0][i], fontsize=10)
        ax.plot([x[0] for x in u], [x[1] for x in u], [x[2] for x in u], 'bs', label='Words')
        #ax.plot([x for x in u[0]], [x for x in u[1]], [x for x in u[2]], 'bs', label='Words')
    for i in range(0, groupAmount):
        ax.scatter([x[0] for x in draw_matr[i]], [x[1] for x in draw_matr[i]], [x[2] for x in draw_matr[i]],
                   color=colors[i], label=groups[i])

    if draw_article_names:
        for i in range(0, len(v[0])):
            ax.text(v[0][i], v[1][i],v[2][i], res[1][i], fontsize=10)
    ax.legend()
    ax.grid(True)
else:
    ax = fig.add_subplot(111)
    if draw_words:
        if draw_words_names:
            for i in range(0,len(u[0])):
                ax.text(u[i][0], u[i][1], res[0][i], fontsize=10)
                #ax.text(u[0][i], u[1][i], res[0][i], fontsize=10)
        ax.plot([x[0] for x in u], [x[1] for x in u], 'bs', label='Words')
        #ax.plot([x for x in u[0]], [x for x in u[1]], 'bs', label='Words')

    for i in range(0, groupAmount):
        ax.scatter([x[0] for x in draw_matr[i]], [x[1] for x in draw_matr[i]],
                   color=colors[i], label=groups[i])

    if draw_article_names:
        for i in range(0, len(v[0])):
            ax.text(v[0][i], v[1][i], res[1][i], fontsize=10)
    ax.legend()
    ax.grid(True)
plt.show()

# for i in range(0, len(u)):
#     print(res[0][i])
