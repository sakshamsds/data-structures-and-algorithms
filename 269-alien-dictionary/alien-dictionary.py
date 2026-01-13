'''
    t -> f
    w -> e
    e -> r
    r -> t
'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2:        # edge case
                return ''
            for j in range(min_len):
                if w1[j] != w2[j]:      # calculate an edge
                    adj_list[w1[j]].add(w2[j])
                    break

        in_degrees = {k: 0 for k in adj_list.keys()}
        for v in adj_list.values():
            for c in v:
                in_degrees[c] = in_degrees.get(c, 0) + 1

        # print(in_degrees)
        q = collections.deque() 
        for c, in_degree in in_degrees.items():
            if in_degree == 0:
                q.append(c)

        order = []
        while q:
            cur = q.popleft()
            order.append(cur)
            for nbr in adj_list[cur]:
                in_degrees[nbr] -= 1
                if in_degrees[nbr] == 0:
                    q.append(nbr)

        return '' if sum(in_degrees.values()) != 0 else ''.join(order)