class Solution {
    public int reverseBits(int n) {
        String bin1 = Integer.toBinaryString(n);
        String padded = String.format("%32s", bin1).replace(' ', '0');
        String reversed = new StringBuilder(padded).reverse().toString();
        return Integer.parseInt(reversed, 2);
    }
}