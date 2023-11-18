from typing import List

from hash import murmur_hash


class BloomFilter:
    def __init__(self, size: int):
        self.bloom_size: int = size
        self.bloom_filter: List[bool] = [False] * size    # TODO optimize this

    def add_key(self, key: str):
        hash_value = murmur_hash(key=key, size=self.bloom_size)
        self.bloom_filter[hash_value] = True

    def is_key_exists(self, key: str) -> bool:
        hash_value = murmur_hash(key=key, size=self.bloom_size)
        return self.bloom_filter[hash_value]
