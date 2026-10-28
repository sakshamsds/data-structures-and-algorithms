class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, node: int) -> int:
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2) -> bool:
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        emailToAccount = {}         # email to account Idx
        uf = UnionFind(len(accounts))

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i

        connectedEmails = collections.defaultdict(list)
        for email, account in emailToAccount.items():
            connectedEmails[uf.find(account)].append(email)
            # connectedEmails[uf.parent[account]].append(email)

        res = []
        for parent, emails in connectedEmails.items():
            res.append([accounts[parent][0]] + sorted(emails))
        return res
        