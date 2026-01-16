/*
    1   2   3   10  4   2   3   5
 */

class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        // for every left pointer, find the right pointer
        // as the left pointer increases, right should increase or remain the same
        // if right does not increase then the deletion window becomes shorter

        int l = 0;
        int r = arr.length - 1;
        while (l < r && arr[r - 1] <= arr[r]) {
            r--;
        }

        int shortest = r;
        while (l < r) {
            while (r < arr.length && arr[l] > arr[r]) {
                r++;
            }
            shortest = Math.min(shortest, r - l - 1);
            // System.out.println(l + " " + r + " " + shortest);
            if (arr[l] > arr[l + 1]) {
                break;
            }
            l++;
        }

        return shortest;
    }
}