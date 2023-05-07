class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];

        for (String s : strs) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i++){
                if (i > prefix.length() - 1){
                    break;
                }
                if (prefix.charAt(i) != s.charAt(i)){
                    break;
                }
                sb.append(s.charAt(i));
            }
            prefix = sb.toString();
        }
        return prefix;
    }
}