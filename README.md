source ./api/bin/activate
pip install -r requirements.txt
python3 api/__init__.py


```
curl http://localhost:5000/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Your text string goes here",
    "model": "text-embedding-ada-002"
  }'
```


# What are embeddings
- Text embeddings measure how related text strings are to each other. They are commonly used for recommendation, clustering, and classification.
- Embeddings are simple vectors of floating point numbers, with distances between two points indicating their relatedness

Price:
- Model	Usage Ada v2	$0.0004 / 1K tokens

The guide https://platform.openai.com/docs/guides/embeddings/use-cases has a bunch of good use cases. Notably, we will try following this guide for learning how to compare text

https://github.com/openai/openai-cookbook/blob/main/text_comparison_examples.md



# TODO

## Setup embeddings for search
1. Split text into chunks smaller than token limit
2. Embed each chunk
3. Store embeddings in vector engine

- OpenAI recommends fine-tuning versus embedding for text classification. When we're going to do tags, maybe we look into that later


## Dev stuff
- docker-compose
- db setup
- Vercel deployment
- Hook up front and back-end
