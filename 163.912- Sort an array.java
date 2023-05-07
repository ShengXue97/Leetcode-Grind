import java.util.Arrays;

class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1){
            return nums;
        }
        int mid = Math.floorDiv(nums.length, 2);
        int[] left = Arrays.copyOfRange(nums, 0, mid);
        int[] right = Arrays.copyOfRange(nums, mid, nums.length);

        left = sortArray(left);
        right = sortArray(right);
        int[] res = new int[left.length + right.length];

        int leftIndex = 0;
        int rightIndex = 0;
        int resIndex = 0;
        while (leftIndex < left.length || rightIndex < right.length){
            if (leftIndex == left.length){
                res[resIndex] = right[rightIndex];
                rightIndex += 1;
            } else if (rightIndex == right.length){
                res[resIndex] = left[leftIndex];
                leftIndex += 1;
            } else if (left[leftIndex] <= right[rightIndex]){
                res[resIndex] = left[leftIndex];
                leftIndex += 1;
            } else {
                res[resIndex] = right[rightIndex];
                rightIndex += 1;
            }
            resIndex += 1;
        }
        return res;
    }
}