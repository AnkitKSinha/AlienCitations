import random
import numpy as np
import json
import pandas

#complete data

def create_data(publication_count, range_of_known_authors) :

    data = {}

    #main author's name
    main_author = "A"
    data["author"] = main_author

    #known author list
    known_authors = ["A"]
    for i in range(100):
        known_authors.append("known-author-" + str(i+1))

    save_authors_df = pandas.DataFrame({'authors' : known_authors})
    save_authors_df.to_csv("known_author_list.csv", sep=",", header=["authors"])
    #publication list for main author
    publications = []

    #choose number of publications .. dynamic depends on size of data
    no_of_publications = publication_count

    #create publications authored by main author
    for i in range(no_of_publications):
        pub = {}
        #publication title
        pub["title"] = "publication-" + str(i+1)
        #create list of authors for the publication
        authors = []
        #select a random number of authors for a publication
        no_of_authors = random.randint(1, 5)
        #obviously, the main author is one of the authors
        authors.append("A")
        #create and add other authors
        for j in range(no_of_authors):
            author_number = random.randint(1, 100)
            authors.append("co-author-" + str(author_number))
        
        #add the author list to the publication
        pub["authors"] = authors

        #create citation data for the publication
        citations = []
        number_of_citations = random.randint(0, 5)
        
        citing_pub_titles = []
        for k in range(number_of_citations):
            citing_pub = {}
            
            while True :
                citing_pub["title"] = "citing-publication-" + str(random.randint(1, 100))
                if citing_pub["title"] not in citing_pub_titles :
                    citing_pub_titles.append(citing_pub["title"])
                break

            citing_authors = []
            no_of_citing_authors = random.randint(1, 5)
            for l in range(no_of_citing_authors):
                random_value = random.randint(1, 1000)
                state = "unknown-author"
                known_author_prob = random.randint(1, 1000)
                if known_author_prob in range(random_value-range_of_known_authors, random_value+range_of_known_authors):
                    state = "known-author"
                main_author_prob = random.randint(1, 1000)
                if main_author_prob in range(random_value-int(range_of_known_authors/10), random_value+int(range_of_known_authors/10)):
                    state = "main-author"
                
                if state == "unknown-author":
                    unknown_author_number = random.randint(1, 100)
                    citing_authors.append("unknown-author-" + str(unknown_author_number))
                elif state == "known-author":
                    citing_authors.append(known_authors[random.randint(1, 100)])
                elif state == "main-author":
                    citing_authors.append("A")
            citing_pub["authors"] = citing_authors
            citations.append(citing_pub)
        
        pub["citations"] = citations
        #citation data for the publication is created

        #add the publication to the publication list of the main author
        publications.append(pub)

    data["publications"] = publications

    # print(data)

    with open('./complete_data.json', "w") as write_file:
        json.dump(data, write_file)

    # print("JSON data saved")

# create_data(10, 80)