import numpy 
import pandas

def operate() :
    author_publication = pandas.read_csv('author_publications_no_co-authors.csv', header=0, index_col=0)
    known_authors = pandas.read_csv('known_author_list.csv', header=0, index_col=0)

    papers = list(author_publication)
    authors = list(author_publication.axes[0])

    author_list = list(known_authors.loc[:, 'authors'])
    # print(author_list)


    for known_author in author_list : 
        try :
            all_publications = author_publication.loc[known_author]
            index = 0
            for i in all_publications :
                if i == 1 :
                    # print(papers[index])
                    # print("Now dropping the publication column")
                    try :
                        author_publication = author_publication.drop(papers[index], axis=1)
                    except : 
                        pass
                        # print("paper not present!")
                    # print("Dropped paper " + papers[index])
                    # print("-"*10)
                index += 1            
            # print("Now dropping row for " + known_author)
            try :
                author_publication = author_publication.drop(known_author)
            except :
                pass
                # print("No row found for " + known_author)
            # print("Dropped row for " + known_author)
        except :
            pass
            # print(known_author + " not present!")

    author_publication.to_csv('alien_citations_no_co-authors.csv')



