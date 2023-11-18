
# SHA function is slow than Murmur has function, 
# because SHA is cryptographic hash function which is 
# slow to compuate compare to non-cryptographic function e.g. murmur

import mmh3


def murmur_hash(key: str, size: int) -> int:
    result = mmh3.hash(key=key, seed=42) # TODO:- update seed value 
    
    result = result % size
    return result



