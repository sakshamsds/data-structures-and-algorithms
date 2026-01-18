class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Map<Integer, Integer> speed_map = new HashMap<>();
        int num_pos = position.length;
        for (int i = 0; i < num_pos; i++) {
            speed_map.put(position[i], speed[i]);
        }

        Arrays.sort(position);

        int fleets = 0;
        double prev_target_time = -1;
        for (int i = num_pos - 1; i > -1; i--) {
            double cur_target_time = (double) (target - position[i]) / speed_map.get(position[i]);
            if (cur_target_time > prev_target_time) {
                fleets++;
                prev_target_time = cur_target_time;
            }
        }
        return fleets;
    }
}