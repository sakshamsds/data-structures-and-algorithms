class FirstUnique {

    private List<Integer> numList;
    private Map<Integer, Integer> freqMap;
    private int uniqIdx;

    public FirstUnique(int[] nums) {
        numList = new ArrayList<>();
        freqMap = new HashMap<>();
        for (int num : nums) {
            add(num);
        }
        uniqIdx = 0;
    }
    
    public int showFirstUnique() {
        while (uniqIdx < numList.size() && freqMap.get(numList.get(uniqIdx)) > 1) {
            uniqIdx++;
        }
        if (uniqIdx < numList.size()) return numList.get(uniqIdx);
        return -1;
    }
    
    public void add(int value) {
        numList.add(value);
        freqMap.put(value, freqMap.getOrDefault(value, 0) + 1);
    }
}

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique obj = new FirstUnique(nums);
 * int param_1 = obj.showFirstUnique();
 * obj.add(value);
 */