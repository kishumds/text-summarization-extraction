from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def read_article(file_name):
    file = open(file_name, "r")

    filedata = file.readlines()
    article = filedata[0].split(". ")

    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))

    return sentences


def sentence_similarity(sent1, sent2, stop_words=None):
    if stop_words == None:
        stop_words = []

    sent1 = [w.lower() for w in sent1 ]
    sent2 = [w.lower() for w in sent2 ]
    all_words = list(set(sent1 + sent2))

    vector1 = [0]*len(all_words)
    vector2 = [0]*len(all_words)

    for w in sent1:
        if w in stop_words:
            continue
        vector1[all_words.index(w)] += 1
    
    for w in sent2:
        if w in stop_words:
            continue
        vector2[all_words.index(w)] += 1
    
    return 1 - cosine_distance(vector1, vector2)


def gen_sim_matrix(sentence, stop_words):
    sim_matrix = np.zeros([len(sentence), len(sentence)])
    for idx1 in range(len(sentence)):
        for idx2 in range(len(sentence)):
            sim_matrix[idx1][idx2] = sentence_similarity(sentence[idx1], sentence[idx2], stop_words)
    return sim_matrix


def generate_summary(file_name, top_n):
    stopword = stopwords.words('english')
    summary = []
    sentences = read_article(file_name)
    if len(sentences) < top_n:
        print("Please enter less number of sentences (top_n) for generating summary and Try again.")
        exit()
    sentence_sim_matrix = gen_sim_matrix(sentences, stopword)
    sentence_sim_graph = nx.from_numpy_array(sentence_sim_matrix)
    scores = nx.pagerank(sentence_sim_graph)
    ranked_sent = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(top_n):
        summary.append(" ".join(ranked_sent[i][1]))
    summary.append(" ")
    print(". ".join(summary))

generate_summary("sample.txt", 25)