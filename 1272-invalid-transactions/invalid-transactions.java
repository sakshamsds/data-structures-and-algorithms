import java.util.*;

class Solution {

    // helper class
    class Transaction {
        String name;
        int time;
        int amount;
        String city;
        
        public Transaction(String transaction) {
            String[] split = transaction.split(",");
            name = split[0];
            time = Integer.parseInt(split[1]);
            amount = Integer.parseInt(split[2]);
            city = split[3];
        }
    }

    public boolean isValid(Transaction t, List<Transaction> list) {
        // Case 1
        if (t.amount > 1000) {
            return false;
        }
        // Case 2
        for (Transaction other : list) {
            if (!t.city.equals(other.city) && Math.abs(t.time - other.time) <= 60) {
                return false;
            }
        }
        return true;
    }


    public List<String> invalidTransactions(String[] transactions) {
        List<String> invalid = new ArrayList<>();
        Map<String, List<Transaction>> map = new HashMap<>();

        // store using name as the key
        for (String transaction : transactions) {
            Transaction t = new Transaction(transaction);
            map.putIfAbsent(t.name, new ArrayList<>());
            map.get(t.name).add(t);
        }

        // comparisons
        for (String transaction : transactions) {
            Transaction t = new Transaction(transaction);
            if (!isValid(t, map.getOrDefault(t.name, new ArrayList<>()))) {
                invalid.add(transaction);
            }
        }
        return invalid;
    }
}