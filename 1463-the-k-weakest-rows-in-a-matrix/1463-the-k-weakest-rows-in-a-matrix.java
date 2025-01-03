class RowPower{
    int power, index;
    public RowPower(int power, int index) {
        this.power = power;
        this.index = index;
    }
}
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        RowPower[] rowPower= new RowPower[mat.length];
        for(int i = 0; i < mat.length; i++){
            int count = 0;
            for(int j = 0; j < mat[0].length; j++){
                count += mat[i][j];
            }
            rowPower[i] = new RowPower(count * 100 + i, i);
        }
        
        int[] ans = new int[k];
        Arrays.sort(rowPower, new Comparator<RowPower>(){
            public int compare(RowPower a, RowPower b){
                return a.power - b.power;
            }
        });
        for(int i = 0; i < k; i++){
            ans[i] = rowPower[i].index;
        }
        return ans;
    }
}