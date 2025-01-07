class Solution {
    public List<String> stringMatching(String[] words) {
        // HashSet<String> ans = new HashSet<>();
        // for (int i = 0; i < words.length; i++) {
        //     for (int j = 0; j < words.length; j++) {
        //         if (i == j){
        //             continue;
        //         }
        //         if (words[j].contains(words[i])){
        //             ans.add(words[i]);
        //             break;
        //         }
        //     }
        // }
        // return new ArrayList<>(ans);
        String str = String.join(" ", words);
        List<String> res = new ArrayList<>();
        for(int i = 0; i < words.length; i++){
            if(str.indexOf(words[i]) != str.lastIndexOf(words[i])){
                res.add(words[i]);
            }
        }
        return res;
    }
}