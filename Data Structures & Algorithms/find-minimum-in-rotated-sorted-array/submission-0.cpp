class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0, r = nums.size()-1;
        if(nums[l]>nums[r]){
            while(l != (r-1)){
                int m = (l+r)/2;
                if(nums[m]>nums[r]){
                    l = m;
                }
                else{
                    r = m;
                }
            }
            cout << nums[l] << l << endl << nums[r] << r <<endl;
            return min(nums[l], nums[r]);
        }
        else return nums[l];
    }
};
