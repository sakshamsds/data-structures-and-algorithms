class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        store = collections.defaultdict(list)
        invalid = set()        # store index to accomodate duplicates

        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            for idx in store[name]:
                _, time2, _, city2 = transactions[idx].split(',')
                if city != city2 and abs(int(time) - int(time2)) <= 60:
                    invalid.add(i)
                    invalid.add(idx)
            if int(amount) > 1000:
                invalid.add(i)
            store[name].append(i)
             
        return [transactions[i] for i in invalid]