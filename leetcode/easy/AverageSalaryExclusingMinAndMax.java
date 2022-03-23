package easy;

// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
// 1491. Average Salary Excluding the Minimum and Maximum Salary

public class AverageSalaryExclusingMinAndMax {

    public static void main(String[] args) {

        int[] salary = new int[] { 4000, 3000, 1000, 2000 };
        System.out.println(average(salary));

    }

    public static double average(int[] salary) {
        // Approach1: if we sort and then add, it will take O(NlogN)
        // Approach2: O(n)

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        double average = 0;

        for(int sal : salary){
            average += sal;
            min = Math.min(min, sal);
            max = Math.max(max, sal);
        }
    
        average -= (min + max);

        return average/(salary.length-2);
    }

}
