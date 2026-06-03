class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int n = landStartTime.length;
        int m = waterStartTime.length;

        // Case 1: Do water then land
        int finishWater = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            finishWater = Math.min(finishWater, waterStartTime[i] + waterDuration[i]);
        }

        int waterLandFinish = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            waterLandFinish = Math.min(waterLandFinish, Math.max(landStartTime[i], finishWater) + landDuration[i]);
        }

        // Case 2: Do land then water
        int finishLand = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            finishLand = Math.min(finishLand, landStartTime[i] + landDuration[i]);
        }

        for (int i = 0; i < m; i++) {
            waterLandFinish = Math.min(waterLandFinish, Math.max(waterStartTime[i], finishLand) + waterDuration[i]);
        }

        return waterLandFinish;
    }
}