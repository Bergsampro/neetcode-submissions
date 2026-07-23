class Solution {
    public boolean isPalindrome(String s) {
         String b = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
         String a = new StringBuilder(b).reverse().toString();
        return b.equals(a);
        
    }
}
