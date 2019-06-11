
import pandas
import json

def get_known_authors() :
    known_authors = pandas.read_csv('known_author_list.csv', header=0, index_col=0)
    return list(known_authors.loc[:, 'authors'])

def brute_force(author_list) :
    # author_list = list(known_authors.loc[:, 'authors'])
    with open("complete_data.json") as jsonArticle :
        root = json.load(jsonArticle)
        alien_data = {}
        publications = []
        for article in root["publications"] :
            alien_citations = []
            for citation in article["citations"] :
                flag = False
                for citing_author in citation["authors"] :
                    if citing_author in author_list :
                        flag = True
                        break
                if flag == False :
                    alien_citations.append(citation)
            alien_article = article
            alien_article["citations"] = alien_citations
            publications.append(alien_article)
        alien_data = root
        alien_data["publications"] = publications
        # with open('./alien_data.json', "w") as write_file:
        #     json.dump(alien_data, write_file)
