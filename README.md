source ./webapp/bin/activate
python api/__init__.py


```
curl https://localhost:5000/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Your text string goes here",
    "model": "text-embedding-ada-002"
  }'
```

- docker-compose
- db setup
