class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 1;
        int right = 1;
        int prev = nums[0];
        boolean canUse = true;

        while (right < nums.length){
            if (nums[right] == prev){
                if (!canUse){
                    right += 1;
                    continue;
                }
                canUse = false;
            }

            if (nums[right] != prev){
                canUse = true;
            }

            nums[left] = nums[right];
            prev = nums[left];
            left += 1;
            right += 1;
        }
        return left;
    }
}