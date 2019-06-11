import csv
import json


class Node(object):

    def __init__(self, row=None, column=None, next_node=None):
        self.row = row
        self.column = column
        self.next_node = next_node

    def get_data(self):
        return [self.row, self.column]

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def set_head(self, head=None) :
        self.head = head
    
    def insert(self, row, column):
        new_node = Node(row, column)
        new_node.set_next(self.head)
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search_row(self, row):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data()[0] == row:
                found = True
            else:
                current = current.get_next()
        return current
    
    def search_column(self, column):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data()[1] == column:
                found = True
            else:
                current = current.get_next()
        return current

    def delete_using_row(self, row):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data()[0] == row:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def delete_all_columns(self, column):
        current = self.head
        previous = None
        # print("deleting column " + str(column))
        while current:
            if current.get_data()[1] == column:
                # print("Found and deleting column " + str(column))
                if previous is None :
                    self.head = current.get_next()
                else :
                    previous.set_next(current.get_next())
                current = current.get_next()
            else:
                previous = current
                current = current.get_next()
    


def search_and_delete(sparse_list, known_index) :
    while True :
        current_row = sparse_list.search_row(known_index)
        # print("Deleting for author : " + str(known_index))
        if current_row is not None :
            col = current_row.get_data()[1]
            sparse_list.delete_all_columns(col)
        else :
            # print("current is none")
            break
    # print("deleted all acquaintences for " + str(known_index))
    # print("Current sparse_list size : " + str(sparse_list.size()))
    # print("\n")

def search_and_delete_v2(sparse_list, known_index) :
    current_row = sparse_list.search_row(known_index)
    while True :
        if current_row is None or current_row.get_data()[0] is not known_index:
            break
        else :
            sparse_list.delete_all_columns(current_row.get_data()[1])
            current_row = current_row.get_next()
    

    
def get_known_authors(filename) :
    inputlist = "known_author_list.csv"
    if filename :
        inputlist = filename
    with open(inputlist) as known_csv :
        known_authors = list(csv.reader(known_csv))
        del known_authors[0]
        return known_authors

def create_sparse_list() :
    with open('author_publications_no_co-authors.csv') as csv_file :
        data = list(csv.reader(csv_file))
        publications = data[0].copy()
        # print(publications)
        del publications[0]
        # authors = []
        # del data[0]
        # # for row in data :
        # #     authors.append(row[0])
        # #     # del row[0]

        #create sparse
        sparse_list = LinkedList()
        row_num = 0
        for row in data :
            column_num = 0
            for col in row :
                if column_num is not 0 and col == "1" :
                    sparse_list.insert(row[0], publications[column_num-1])
                column_num += 1
            row_num += 1
        
        # head = sparse_list.head
        # temp = head
        # while temp is not None :
        #     r, c = temp.get_data()
        #     print(str(r) + " " + str(c))
        #     temp = temp.get_next()
        return sparse_list

# sparse_list, authors = create_sparse_list()

def operate(sparse_list, known_authors) :
    # with open('author_publications_no_co-authors.csv') as csv_file :
    #     data = list(csv.reader(csv_file))
    #     publications = data[0].copy()
    #     authors = []
    #     del data[0]
    #     for row in data :
    #         authors.append(row[0])
    #         del row[0]

    #     #create sparse
    #     sparse_list = LinkedList()
    #     row_num = 0
    #     for row in data :
    #         column_num = 0
    #         for col in row :
    #             if col == "1" :
    #                 sparse_list.insert(row_num, column_num)
    #             column_num += 1
    #         row_num += 1
        # print("Created sparse matrix ")
        # print(sparse_list.size())
        # head = sparse_list.head
        # temp = head
        # while temp is not None :
        #     r, c = temp.get_data()
        #     print(str(r) + " " + str(c))
        #     temp = temp.get_next()  

    # known_authors = get_known_authors()
    # print(known_authors)
    before_size = sparse_list.size()
    for i in known_authors :
        # known_index = 0
        # for j in authors :
        #     if i[1] == j :
        #         # print(i[1] + " and " + j + " are equal")
        #         search_and_delete(sparse_list, known_index)
        #     known_index += 1
        search_and_delete(sparse_list, i[1])
        
        # print("Done")
        # print(sparse_list.size())
    # return sparse_list
    head  = sparse_list.head
    temp = head

    histogram_data = {}

    while temp is not None :
        r, c = temp.get_data()
        if r not in histogram_data.keys():
            histogram_data[r] = 1
        else :
            histogram_data[r] += 1
        temp = temp.get_next()
    after_size = sparse_list.size()
    # print(histogram_data)
    # with open('../Server/public/results/histogram_data.json', "w") as write_file:
    #     json.dump(histogram_data, write_file)
    
    return before_size, after_size

# operate()

# sparse_list = operate(create_sparse_list(), get_known_authors())
# head = sparse_list.head
# temp = head
# while temp is not None :
#     r, c = temp.get_data()
#     print(str(r) + " " + str(c))
#     temp = temp.get_next()
        
 

    