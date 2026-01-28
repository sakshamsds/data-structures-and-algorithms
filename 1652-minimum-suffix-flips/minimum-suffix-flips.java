class Solution {
    public int minFlips(String target) {
        int flips = 0;
        for (char t : target.toCharArray()) {
            // apply flips to 0
            // if it matches with target then no more flips
            // else flips + 1

            char cur = '0';
            if (flips % 2 == 1) cur = '1';
            if (cur != t) flips += 1;
        } 
        return flips;
    }
}