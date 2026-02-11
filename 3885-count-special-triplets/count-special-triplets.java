/*
    10    5       10
    10 - 1          10 - 1
    2               5
 */

class Solution {

    private final int MODULO = 1_000_000_000 + 7;

    public int specialTriplets(int[] nums) {
        Map<Integer, Integer> left = new HashMap<>();
        Map<Integer, Integer> right = new HashMap<>();

        for (int num : nums) {
            right.put(num, right.getOrDefault(num, 0) + 1);
        }

        long num_triplets = 0;
        for (int num : nums) {
            if (right.containsKey(num)) {
                int freq = right.get(num);
                if (freq == 1) {
                    right.remove(num);
                } else {
                    freq--;
                    right.put(num, freq);
                }
            }

            // calculate
            int freqL = left.getOrDefault(num * 2, 0);
            int freqR = right.getOrDefault(num * 2, 0);
            num_triplets = (num_triplets + 1L * freqL * freqR) % MODULO;

            left.put(num, left.getOrDefault(num, 0) + 1);
        }

        return (int) num_triplets;
    }
}