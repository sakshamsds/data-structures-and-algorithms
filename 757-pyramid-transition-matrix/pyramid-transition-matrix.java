class Solution {

    private Map<String, List<Character>> store;
    private Map<String, Boolean> memo;

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        // create mapping one, two -> list(three)
        memo = new HashMap<>();
        store = new HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0, 2);
            Character value = s.charAt(2);
            if (!store.containsKey(key)) {
                store.put(key, new ArrayList<>());
            }
            store.get(key).add(value);
        }
        return backtrack(0, bottom, "");
    }

    private boolean backtrack(int i, String curStr, String nextStr) {
        if (i == curStr.length() - 1) {
            i = 0;
            curStr = nextStr;
            nextStr = "";
        }

        if (i == 0 && curStr.length() == 1) {
            return true;
        }

        String memoKey = String.valueOf(i) + "," + curStr + "," + nextStr;
        if (memo.containsKey(memoKey)) {
            return memo.get(memoKey);
        }
        boolean valid = false;

        String key = curStr.substring(i, i + 2);
        if (!store.containsKey(key)) return false;
        for (char c : store.get(key)) {
            if (backtrack(i + 1, curStr, nextStr + c)) {
                valid = true;
                break;
            }
        }

        memo.put(memoKey, valid);
        return valid;
    }
}