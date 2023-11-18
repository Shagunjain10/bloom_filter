
from bloom import BloomFilter

# so the murmur hash, 
# return different value for same string every time, 
# how murmur hash or any other type hash can be use as string match or bloom filter
# It's because of seed that you are passing, if seed is same, 
# then the hash that any hash function will return will be the same on same string

def main():
    bloom_filter = BloomFilter(16)

    data = ['a', 'b', 'c']

    for key in data:
        bloom_filter.add_key(key)

    data.append('d')
    for key in data:
        print(bloom_filter.is_key_exists(key))




if __name__ == '__main__':
    main()