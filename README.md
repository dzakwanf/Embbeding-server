
# Embbeding server

This project aims to create a server capable of generating vector representations (embeddings) of sentences using the Sentence Transformer model in the Python environment. The Sentence Transformer model is employed to transform text into semantic vectors that can better represent the meaning of sentences.


## Run project

Clone the project

```bash
  https://github.com/dzakwanf/Embbeding-server.git
```

Go to the project directory

```bash
  cd Embbeding Model
```

Build docker images 

```bash
  docker-compose build
```

Start the embbeding server

```bash
  docker-compose up -d
```


## Authors

- [@dzakwanf](https://www.github.com/octokatherine)


## Features

- Open AI Support
- Langchain Integrated
- Model 1: multi-qa-mpnet-base-dot-v
- Model 2: all-MiniLM-L12-v2
- Model 3: gtr-t5-large



## Usage/Examples


### testing script

```python
python test_embbding.py
```

###  Model 1


```bash
curl -X 'POST' \
  'http://IP_ADDRESS:8001/v1/embeddings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "substratus.ai provides the best LLM tools",
  "model": "multi-qa-mpnet-base-dot-v1"
}'
```

###  Model 2

```bash
curl -X 'POST' \
  'http://IP_ADDRESS:8002/v1/embeddings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "substratus.ai provides the best LLM tools",
  "model": "all-MiniLM-L12-v2"
}'
```


###  Model 3

```bash
curl -X 'POST' \
  'http://IP_ADDRESS:8003/v1/embeddings' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "input": "substratus.ai provides the best LLM tools",
  "model": "gtr-t5-large"
}'
```


### Python langchain_community

```python
from langchain_community.embeddings import LocalAIEmbeddings

def embbeding_model(embeddings,text):

    if embeddings == "multiqa":
        embd = LocalAIEmbeddings(
                openai_api_base="http://IP_ADDRESS:8000/v1", model="multi-qa-mpnet-base-dot-v", 
                openai_api_key"sk-"
            )
    elif embeddings == "allmini_l12":
        embd = LocalAIEmbeddings(
                openai_api_base="http://IP_ADRESS:8002/v1", model="all-MiniLM-L12-v2", 
                openai_api_key"sk-"
            )
    elif embeddings == "gtr":
        embd = LocalAIEmbeddings(
                openai_api_base="http://IP_ADDRESS:8003/v1", 
                model="gtr-t5-large", 
                openai_api_key"sk-"
            )
    else: 
        print(embedding eror)


    text = text
    query_result = embd.embed_query(text)
    print(query_result)


# Example model 1
embbeding_model(
    embeddings"multiqa",
    text="Hallo testing model 1"
)


#Example model 2
embbeding_model(
    embeddings"allmini_l12",
    text="Hallo testing model 2"
)


# Example model 3
embbeding_model(
    embeddings"gtr",
    text="Hallo testing model 3"
)

```

### Java For langchain4j
``` Java
import dev.langchain4j.data.embedding.Embedding;
import dev.langchain4j.model.embedding.EmbeddingModel;
import dev.langchain4j.model.localai.LocalAiEmbeddingModel;
import dev.langchain4j.model.output.Response;



public class App {

    public static void main( String[] args ) {

    EmbeddingModel embeddingModel = LocalAiEmbeddingModel.builder()
            .baseUrl("http://IP_ADREESS:8001/v1")
            .modelName("multi-qa-mpnet-base-dot-v")
            .logRequests(true)
            .logResponses(true)
            .build();

    Response<Embedding> response = embeddingModel.embed("Selamat siang mas ainul");
    System.out.println(response);
    }
}

```