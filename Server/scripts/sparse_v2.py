import csv

class Node(object):

    def __init__(self, row=None, columns=None, next_node=None):
        self.row = row
        self.columns = columns
        self.next_node = next_node

    def set_data(self, row, columns, next_node) :
        self.row = row
        self.columns = columns
        self.next_node = next_node

    def get_data(self):
        return [self.row, self.columns]

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
        find_node = self.search_row(row)
        if find_node is not None :
            appended = find_node.get_data()[1]
            appended.append(column)
            find_node.set_data(find_node.get_data()[0], appended, find_node.get_next())
        else :
            new_node = Node(row, [column])
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
        if current_row is not None :
            col = current_row.get_data()[1]
            sparse_list.delete_all_columns(col)
        else :
            break


def search_and_delete_v2(sparse_list, known_index) :
    current_row = sparse_list.search_row(known_index)
    if current_row is not None :
        for col in current_row.get_data()[1] :
            delete_all_columns(col)
    

    
def get_known_authors() :
    with open('known_author_list.csv') as known_csv :
        known_authors = list(csv.reader(known_csv))
        del known_authors[0]
        return known_authors

def create_sparse_list() :
    with open('author_publications_no_co-authors.csv') as csv_file :
        data = list(csv.reader(csv_file))
        publications = data[0].copy()
        del publications[0]

        #create sparse
        sparse_list = LinkedList()
        row_num = 0
        for row in data :
            column_num = 0
            for col in row :
                if column_num is not 0 and col == "1" :
                    sparse_list.insert(row[0], publications[column_num])
                column_num += 1
            row_num += 1

        return sparse_list

# sparse_list, authors = create_sparse_list()
# sparse_list = create_sparse_list()
# head = sparse_list.head
# temp = head
# while temp is not None :
#     r, c = temp.get_data()
#     print(str(r) + " " + str(c))
#     temp = temp.get_next()

def operate(sparse_list, known_authors) :
    
    for i in known_authors :
        search_and_delete_v2(sparse_list, i[1])
    return sparse_list

# operate()

# sparse_list = operate(create_sparse_list(), get_known_authors())
# head = sparse_list.head
# temp = head
# while temp is not None :
#     r, c = temp.get_data()
#     print(str(r) + " " + str(c))
#     temp = temp.get_next()
        
 

    