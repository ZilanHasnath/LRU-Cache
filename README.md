# LRU Cache Implementation

An implementation of a Least Recently Used (LRU) Cache in Python featuring $O(1)$ average time complexity for both `get` and `put` operations.

## Features
- **Positive Capacity**: Initialized with a fixed capacity.
- **Fast Lookups & Updates**: `get(key)` and `put(key, value)` execute in $O(1)$ average time.
- **Automatic Eviction**: Automatically removes the least recently used item when the cache exceeds capacity.

## Data Structures Used & Why
1. **Hash Map (Python Dictionary):** 
   - Used to store keys mapped directly to their corresponding doubly linked list nodes. This allows for $O(1)$ time complexity when checking if a key exists and retrieving its node.
2. **Doubly Linked List:** 
   - Used to maintain the recency of usage order. Nodes closer to the head are most recently used, while nodes closer to the tail are least recently used. A doubly linked list enables $O(1)$ insertions, deletions, and updates of nodes.

## How LRU Ordering is Maintained
- **On `get(key)`:** If the key exists, the corresponding node is detached from its current position and moved to the front (right after the head), marking it as the most recently used.
- **On `put(key, value)`:** 
  - If the key already exists, its value is updated and the node is moved to the front.
  - If the key is new and the cache has reached capacity, the node right before the tail (the least recently used item) is removed from both the linked list and the hash map. Then, the new node is inserted at the front.

## Complexity
- **Time Complexity:** $O(1)$ for both `get()` and `put()` operations.
- **Space Complexity:** $O(\text{capacity})$ to store the cache items and nodes up to the defined capacity limit.

## How to Run
1. Make sure you have Python installed.
2. Run the script from your terminal:
   ```bash
   python lru_cache.py