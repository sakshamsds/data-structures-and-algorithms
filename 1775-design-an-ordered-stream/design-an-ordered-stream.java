class OrderedStream {

    private Map<Integer, String> map;
    private int currentKey;

    public OrderedStream(int n) {
        map = new HashMap<>();
        currentKey = 1;
    }
    
    // O(n) -> hashmap, add the first key
    public List<String> insert(int idKey, String value) {       
        map.put(idKey, value);

        List<String> answer = new ArrayList<>();
        while (map.containsKey(currentKey)){
            answer.add(map.get(currentKey));
            currentKey++;
        }
        return answer;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */