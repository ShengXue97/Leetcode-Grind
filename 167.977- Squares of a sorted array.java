class Solution {
    public int[] sortedSquares(int[] nums) {
        //int firstPositive = nums.length;
        int left = 0;
        int right = nums.length - 1;

        while (left < right){
            int mid = left + Math.floorDiv(right - left, 2);
            if (nums[mid] < 0){
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        right = left;
        left -= 1;
        int[] res = new int[nums.length];
        int i = 0;
        while (left >= 0 && right < nums.length){
            if (Math.abs(nums[left]) <= Math.abs(nums[right])){
                res[i] = nums[left] * nums[left];
                left -= 1;
            } else {
                res[i] = nums[right] * nums[right];
                right += 1;
            }
            i += 1;
        }

        while (left >= 0){
            res[i] = nums[left] * nums[left];
            left -= 1;
            i += 1;
        }

        while (right < nums.length){
            res[i] = nums[right] * nums[right];
            right += 1;
            i += 1;
        }

        return res;

    }
}