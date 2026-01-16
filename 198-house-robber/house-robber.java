/*
    1       2           3           1
    nr      nr+2        
    r       (r, nr)

*/

class Solution {
    public int rob(int[] nums) {
        int no_rob = 0;
        int rob = 0;

        for (int num : nums) {
            int tmp = no_rob;
            no_rob = Math.max(no_rob, rob);
            rob = tmp + num;
        }

        return Math.max(no_rob, rob);
    }
}