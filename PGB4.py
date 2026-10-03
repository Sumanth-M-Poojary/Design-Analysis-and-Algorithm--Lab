import heapq

chars = ['A', 'B', 'C', 'D', 'E']
probs = [0.1, 0.1, 0.2, 0.2, 0.4]

heap = [[p, [c, ""]] for c, p in zip(chars, probs)]

heapq.heapify(heap)

while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)

    for pair in lo[1:]:
        pair[1] = '0' + pair[1]

    for pair in hi[1:]:
        pair[1] = '1' + pair[1]

    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])


print("Char | Probability | Huffman Code")
print("-" * 35)

huffcode = dict(heap[0][1:])

for c, p in zip(chars, probs):
    print(f"{c}    | {p}         | {huffcode[c]}")