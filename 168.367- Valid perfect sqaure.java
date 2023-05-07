class Solution {
    public boolean isPerfectSquare(int num) {
        double l = 0;
        double r = num;

        while(l <= r){
            double mid = l + Math.floor((r - l) / 2);
            double prod = mid * mid;
            if (prod == num){
                return true;
            } else if (prod < num){
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return false;
    }
}