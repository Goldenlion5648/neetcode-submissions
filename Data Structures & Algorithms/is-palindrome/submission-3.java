class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < s.length(); i++) {
            if (Character.isAlphabetic(s.charAt(i)) || Character.isDigit(s.charAt(i))) {
                builder.append(s.charAt(i));
            }
        }
        s = builder.toString();
        System.out.println(s);

        for(int i = 0; i < s.length() / 2; i++) {
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(s.length()-i-1))) {
                return false;
            }
        }
        return true;
    }
}
