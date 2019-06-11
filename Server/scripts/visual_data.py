import json

def create_visual(filename) :
  with open (filename) as complete_data :
    data = json.load(complete_data)
    final_data = {}
    final_data["nodes"] = []
    final_data["edges"] = []

    all_ids = []
    all_cite_ids = []
    all_citing_authors = []

    nodes = []
    edges = []

    item = {}
    item["label"] = data["author"]
    item["id"] = data["author"]
    nodes.append(item)

    main_author_id = item["id"]
    all_ids.append(main_author_id)
    all_citing_authors.append(main_author_id)

    pubs = data["publications"]

    for pub in pubs :
      node = {}
      node["label"] = pub["title"]
      node["id"] = pub["title"]
      node["color"] = "#5c7a5a"
      # node["font"] = "4px arial #fff"
      edge = {}
      edge["from"] = main_author_id
      edge["to"] = node["id"]
      nodes.append(node)
      edges.append(edge)

      citations = pub["citations"]

      for cite in citations : 
        node = {}
        node["label"] = cite["title"]
        node["id"] = cite["title"]
        node["color"] = "#545572"
        # node["font"] = "4px arial #fff"
        edge = {}
        edge["from"] = pub["title"]
        edge["to"] = node["id"]
        if node["id"] not in all_cite_ids :
          nodes.append(node)
          all_cite_ids.append(node["id"])
        edges.append(edge)
        
        citing_authors = cite["authors"]
        author_index = 0
        for citing_author in citing_authors :
          node = {}
          node["label"] = citing_author
          node["id"] = citing_author
          node["color"] = "#6e5472"

          # author_index += 1
          edge = {}
          edge["from"] = cite["title"]
          edge["to"] = node["id"]
          if node["id"] not in all_citing_authors :
            nodes.append(node)
            all_citing_authors.append(node["id"])
          edges.append(edge)
        
    final_data["nodes"] = nodes
    final_data["edges"] = edges

    # print(final_data)

    with open('../Server/public/results/visual_data.json', "w") as write_file:
      json.dump(final_data, write_file)

    # print("JSON data saved")