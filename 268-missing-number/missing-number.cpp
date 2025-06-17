class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int len=nums.size();
        int x=0;
        for(int i=0;i<len;i++){
            if(nums[i]==x){
                x++;
            }
            else return x;      
    }
    return x;
    }
};