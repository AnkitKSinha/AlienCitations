import data_creation
import operation
import matrix_create
import time
import matplotlib.pyplot as plt
import brute_force
import sparse
import pandas as pd
import numpy as np

time_taken_matrix = []
time_taken_brute = []
time_taken_sparse = []
publication_count = []
eigen_values = []
aci_values = []

colors = ['r', 'b', 'g', 'y', 'c']
min_y = 0
max_y = 0

for j in range(0, 5) :
    print("running for j : ", j)
    publication_count = []
    eigen_values = []
    for i in range(1,80) :
        publication_count.append(i*10)
        data_creation.create_data(i*10, j*30)
        matrix_create.generate_matrix()

        # calculate svd 
        data = pd.read_csv("author_publications_no_co-authors.csv")
        publications = data.columns 
        authors = data.iloc[0]
        data = data.drop(['Unnamed: 0'], axis='columns')
        data = np.array(data)
        u, s, vh = np.linalg.svd(data, full_matrices=True)
        if(round((s[0] + s[1] + s[2] + s[3] + s[4])/5,5) > max_y):
            max_y = round((s[0] + s[1] + s[2] + s[3] + s[4])/5,5) + 1
        eigen_values.append(round((s[0] + s[1] + s[2] + s[3] + s[4])/5, 5))


        #begin sparse operations
        sparse_list = sparse.create_sparse_list()
        sparse_known_authors = sparse.get_known_authors()
        #calculate operation time
        start = time.time()
        before_size, after_size = sparse.operate(sparse_list, sparse_known_authors)
        end = time.time()
        # aci = after_size / before_size
        print(before_size, after_size)
        # aci_values.append(aci)
        time_taken_sparse.append(end-start)
    if j == 1 or j == 4 or j == 0:
        plt.plot(publication_count, eigen_values, colors[j])

plt.yticks(np.arange(0, max_y, 0.5))
plt.show()

    # start = time.time()
    # operation.operate()
    # end = time.time()
    # time_taken_matrix.append(end-start)

    #begin brute force operation
    # bf_known_authors = brute_force.get_known_authors()
    #calculate operation time
    # start = time.time()
    # brute_force.brute_force(bf_known_authors)
    # end = time.time()
    # time_taken_brute.append(end - start)

# print(aci_values)
# plt.plot(publication_count, time_taken_matrix, 'r')
# # plt.plot(publication_count, time_taken_brute, 'b')
# plt.plot(publication_count, time_taken_sparse, 'g')
# plt.xlabel("No of articles published")
# plt.ylabel("Alien citations extraction time in seconds")
# plt.legend(['Matrix', 'Linked List'])
# plt.show()


# fig, ax1 = plt.subplots()

# color = 'tab:red'
# ax1.set_xlabel('publications')
# ax1.set_ylabel('SVD_ACI', color=color)
# ax1.plot(publication_count, eigen_values, color=color)
# ax1.tick_params(axis='y', labelcolor=color)

# ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

# color = 'tab:blue'
# ax2.set_ylabel('ACI', color=color)  # we already handled the x-label with ax1
# ax2.plot(publication_count, aci_values, color=color)
# ax2.tick_params(axis='y', labelcolor=color)

# fig.tight_layout()  # otherwise the right y-label is slightly clipped
# plt.show()
