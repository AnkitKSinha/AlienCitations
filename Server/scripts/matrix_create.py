import json
import numpy
import pandas

def findIndex(array, val):
	"returns index of val in list"
	try:
		index = array.index(val)
	except ValueError:
		index = -1
	return index

#Considering all authors in the data
# def initMatrix(rows, cols, obj, author_rows, pub_cols):
#   for article in obj["publications"]:
#     # pub_cols.append(article["title"])
#     for author in article["authors"]:
#       if(findIndex(rows, author) == -1):
#         rows.append(author)
#         cols.append(author)
#       # else:
#       #   print("Repeating Author")
#     for citation in article["citations"]: 
#       pub_cols.append(citation["title"])
#       for author in citation["authors"]:
#         if(findIndex(rows, author) == -1):
#           author_rows.append(author)
#           rows.append(author)
#           cols.append(author)
#         # else:
#         #   # print("Repeating citation-author")
#   print("article")
#   return

#Considering only citing and main author
def initMatrix(rows, cols, obj, author_rows, pub_cols):
    for article in obj["publications"]:
        # pub_cols.append(article["title"])
        # for author in article["authors"]:
        #   if(findIndex(rows, author) == -1):
        #     rows.append(author)
        #     cols.append(author)
        # else:
        #   print("Repeating Author")
        for citation in article["citations"]: 
            pub_cols.append(citation["title"])
            for author in citation["authors"]:
                if(findIndex(rows, author) == -1):
                    author_rows.append(author)
                    rows.append(author)
                    cols.append(author)
                # else:
                #   # print("Repeating citation-author")
    # print("Matrices initialized!...")
    return


# 	# pandasMatrix = pandas.DataFrame(matrix)
# 	# pandasMatrix.to_csv("referencedMatrix1v2.csv", sep=',', header=cols)
#Considering all authors
# def consumeMatrix(matrix, rows, cols, obj, pub_2d, author_rows, pub_cols) :
#   for article in obj["publications"] :
#     for citation in article["citations"] :
#       for citing_author in citation["authors"] :
#         for cited_author in article["authors"] :
#           print(findIndex(pub_cols, article["title"]))
#           print(cited_author)
#           print(findIndex(author_rows, cited_author))
#           pub_2d[findIndex(author_rows, citing_author)][findIndex(pub_cols, citation["title"])] = 1
#           # print(findIndex(rows, citing_author))
#           # print(findIndex(cols, cited_author))
#           matrix[findIndex(rows, citing_author)][findIndex(cols, cited_author)] = 1
#           print("Done")
#   return 

#considering only citing and main author
def consumeMatrix(main_author, matrix, rows, cols, obj, pub_2d, author_rows, pub_cols) :
    for article in obj["publications"] :
        for citation in article["citations"] :
            for citing_author in citation["authors"] :
                # print(findIndex(pub_cols, citation["title"]))
                # print(cited_author)
                # print(findIndex(author_rows, cited_author))
                pub_2d[findIndex(author_rows, citing_author)][findIndex(pub_cols, citation["title"])] = 1
                # print(findIndex(rows, citing_author))
                # print(findIndex(cols, cited_author))
                matrix[findIndex(rows, citing_author)][findIndex(cols, main_author)] = 1
                # print("Done")
    # print("Matrices consumed!..")
    return 




def generate_matrix(filepath) :
    datafile = "complete_data.json"
    if filepath :
        datafile = filepath
    
    with open(datafile) as jsonArticle :
        root = json.load(jsonArticle)
        rows = []
        cols = []
        pub_cols = []
        author_rows = []
        author_rows.append(root["author"])
        rows.append(root["author"])
        cols.append(root["author"])
        initMatrix(rows, cols, root, author_rows, pub_cols)
        array2D = numpy.zeros((len(rows), len(cols)), dtype=int)
        publication2D = numpy.zeros((len(author_rows), len(pub_cols)), dtype=int)
        consumeMatrix(root["author"], array2D, rows, cols, root, publication2D, author_rows, pub_cols)
        # print(publication2D)

        # matrix = numpy.asmatrix(publication2D)
        # matrix = numpy.asmatrix(array2D)
        author_publications = numpy.asmatrix(publication2D)


        # pandas_citation_matrix = pandas.DataFrame(matrix)
        pandas_author_publications = pandas.DataFrame(author_publications)

        # pandas_citation_matrix.to_csv("citation_matrix_no_co-authors.csv", sep=",", header=cols)
        # author_rows.append('sadas')
        # print(len(author_rows))
        pandas_author_publications.insert(loc=0, column='', value=author_rows)
        pub_cols.insert(0, '')
        pandas_author_publications.to_csv("author_publications_no_co-authors.csv", sep=",", header=pub_cols, index=False, index_label=author_rows)
        return pandas_author_publications

  

# generate_matrix()


