import uuid
import matplotlib.pyplot as plt
from typing import List

from bloom import BloomFilter

# so the murmur hash,
# return different value for same string every time,
# how murmur hash or any other type hash can be use as string match or bloom filter
# It's because of seed that you are passing, if seed is same,
# then the hash that any hash function will return will be the same on same string


def plot_graph(
    x: List[int],
    y: List[int],
    title: str = "Line Plot",
    x_axis: str = "X-axis",
    y_axis: str = "Y-axis",
):
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, marker="o", linestyle="-", color="b", label="Custom Line")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.title(title)


def main():
    data = [str(uuid.uuid4()) for _ in range(1000)]
    data_map_exists = {key: True for key in data[:500]}
    data_map_not_exists = {key: False for key in data[500:]}

    print(f"Len of dict is {len(data_map_exists)}, {len(data_map_not_exists)}")
    # For every 10 keys insert, measure the false positivity rate

    bloom_filter_size_data = []
    false_postive_data = []
    for bloom_filter_size in range(100, 10001, 100):
        bloom_filter = BloomFilter(bloom_filter_size)
        for key, _ in data_map_exists.items():
            bloom_filter.add_key(key)

        false_postive = 0

        for key in data:
            is_key_exists = bloom_filter.is_key_exists(key)
            if is_key_exists and (key in data_map_not_exists.keys()):
                false_postive = false_postive + 1

        print(
            f"Filter Size:- {bloom_filter_size}, False positive is {false_postive/len(data)}"
        )
        bloom_filter_size_data.append(bloom_filter_size)
        false_postive_data.append(false_postive / len(data))

    plot_graph(
        bloom_filter_size_data, 
        false_postive_data, 
        "False Positive Graph",
        "Bloom Filter Size",
        "False Postive Ratio"
    )


if __name__ == "__main__":
    main()
