from langchain_community.embeddings import LocalAIEmbeddings


def embbeding_model(embeddings,text):

    if embeddings == "multiqa":
        emb = LocalAIEmbeddings(openai_api_base="http://IP_ADDRESS:8001/v1", 
                model="multi-qa-mpnet-base-dot-v", 
                openai_api_key="custom"
            )
    elif embeddings == "allmini_l12":
        emb = LocalAIEmbeddings(
                openai_api_base="http://IP_ADDRESS:8001/v1", 
                model="all-MiniLM-L12-v2", 
                openai_api_key="custom"
            )
    elif embeddings == "gtr":
        emb = LocalAIEmbeddings(
            openai_api_base="http://IP_ADDRESS:8001/v1", 
            model="gtr-t5-large", 
            openai_api_key="custom"
            )
    else: 
        print("Embbeding model eror")


    text = text
    query_result = emb.embed_query(text)
    print(query_result)


# Example model 1
embbeding_model(
    embeddings="multiqa",
    text="Hallo testing model 1"
)


# Example model 2
embbeding_model(
    embeddings="allmini_l12",
    text="Hallo testing model 2"
)


# Example model 3
embbeding_model(
    embeddings="gtr",
    text="Hallo testing model 3"
)
