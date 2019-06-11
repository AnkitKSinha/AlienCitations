import matrix_create
import time
import sparse
import pandas as pd
import numpy as np
import visual_data


matrix_create.generate_matrix("../Server/public/datasets/dataset")
visual_data.create_visual("../Server/public/datasets/dataset")

# calculate score/
data = pd.read_csv("author_publications_no_co-authors.csv")
publications = data.columns 
authors = data.iloc[0]
data = data.drop(['Unnamed: 0'], axis='columns')
data = np.array(data)
u, s, vh = np.linalg.svd(data, full_matrices=True)

score = (round((s[0] + s[1] + s[2] + s[3] + s[4])/5, 5))
sparse_list = sparse.create_sparse_list()
sparse_known_authors = sparse.get_known_authors("../Server/public/datasets/list")
start = time.time()
before_size, after_size = sparse.operate(sparse_list, sparse_known_authors)
end = time.time()

aci = after_size/before_size
print(score)
print(aci)

def compute() :
    matrix_create.generate_matrix("complete_data.json")
    # visual_data.create_visual("complete")

    #calculate score
    data = pd.read_csv("author_publications_no_co-authors.csv")
    publications = data.columns 
    authors = data.iloc[0]
    data = data.drop(['Unnamed: 0'], axis='columns')
    data = np.array(data)
    u, s, vh = np.linalg.svd(data, full_matrices=True)

    score = (round((s[0] + s[1] + s[2] + s[3] + s[4])/5, 5))
    sparse_list = sparse.create_sparse_list()
    sparse_known_authors = sparse.get_known_authors("known_author_list.csv")
    start = time.time()
    before_size, after_size = sparse.operate(sparse_list, sparse_known_authors)
    end = time.time()

    aci = after_size/before_size
    return score, aci



