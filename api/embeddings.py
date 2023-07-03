import pickle

import pandas as pd
import tiktoken
from openai.embeddings_utils import (
    chart_from_components,
    distances_from_embeddings,
    get_embedding,
    indices_of_nearest_neighbors_from_distances,
    tsne_components_from_embeddings,
)

embedding_encoding = "cl100k_base"

# set path to embedding cache
embedding_cache_path = "api/data/recommendations_embeddings_cache.pkl"

EMBEDDING_MODEL = "text-embedding-ada-002"

# load the cache if it exists, and save a copy to disk
try:
    embedding_cache = pd.read_pickle(embedding_cache_path)
except FileNotFoundError:
    embedding_cache = {}
with open(embedding_cache_path, "wb") as embedding_cache_file:
    pickle.dump(embedding_cache, embedding_cache_file)

encoding = tiktoken.get_encoding(embedding_encoding)


def remove_non_alnum(s):
    return "".join(c for c in s if c.isalnum() or c.isspace())


# define a function to retrieve embeddings from the cache if present, and otherwise request via the API
def embedding_from_string(
    string: str, model: str = EMBEDDING_MODEL, embedding_cache=embedding_cache
) -> list:
    """Return embedding of given string, using a cache to avoid recomputing."""
    # embedding_cache = {}
    parsed_str = remove_non_alnum(string)
    print(parsed_str)
    print(len(parsed_str))
    # n_tokens = len(encoding.encode(string))
    if (parsed_str, model) not in embedding_cache.keys():
        print("Getting new embedding")
        embedding_cache[(parsed_str, model)] = get_embedding(parsed_str, model)
        with open(embedding_cache_path, "wb") as embedding_cache_file:
            pickle.dump(embedding_cache, embedding_cache_file)
    return embedding_cache[(parsed_str, model)]


def print_recommendations_from_strings(
    strings: list[str],
    index_of_source_string: int,
    k_nearest_neighbors: int = 1,
    model=EMBEDDING_MODEL,
) -> list[int]:
    """Print out the k nearest neighbors of a given string."""
    # get embeddings for all strings
    embeddings = []
    for string in strings:
        embedding = embedding_from_string(string, model=model)
        if embedding:
            embeddings.append(embedding)
    # get the embedding of the source string
    query_embedding = embeddings[index_of_source_string]
    # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
    distances = distances_from_embeddings(
        query_embedding, embeddings, distance_metric="cosine"
    )
    # get indices of nearest neighbors (function from embeddings_utils.py)
    indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(
        distances
    )

    # print out source string
    query_string = strings[index_of_source_string]
    print(f"Source string: {query_string}")
    # print out its k nearest neighbors
    k_counter = 0
    for i in indices_of_nearest_neighbors:
        # skip any strings that are identical matches to the starting string
        if query_string == strings[i]:
            continue
        # stop after printing out k articles
        if k_counter >= k_nearest_neighbors:
            break
        k_counter += 1

        # print out the similar strings and their distances
        print(
            f"""
        --- Recommendation #{k_counter} (nearest neighbor {k_counter} of {k_nearest_neighbors}) ---
        String: {strings[i]}
        Distance: {distances[i]:0.3f}"""
        )

    return indices_of_nearest_neighbors
