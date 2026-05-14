class TimeMap {

    /*
     key -> [(timestamp, value)]

        k1 -> [(t1, v1), (t2, v2)]
        k2 -> [(t3, v3), (t4, v4)]
    */

    private Map<String, List<Pair<Integer, String>>> store;

    public TimeMap() {
        store = new HashMap<>(); 
    }
    
    public void set(String key, String value, int timestamp) {
        if (!store.containsKey(key)) {
            store.put(key, new ArrayList<>());
        }
        store.get(key).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if (!store.containsKey(key)) {
            return "";
        }
        int left = 0, right = store.get(key).size();

        while (left < right) {
            int mid = left + (right - left) / 2;
            int timestampPrev = store.get(key).get(mid).getKey();
            if (timestampPrev <= timestamp) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        if (left == 0) {
            return "";
        }
        return store.get(key).get(left - 1).getValue();
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */