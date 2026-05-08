class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // first loop
        int left = 0, right = matrix.size()-1;
        while(left <= right){
            int kiri = 0, kanan = matrix[0].size()-1;
            int mid = (left + right) / 2;
            if(target > matrix[mid][kanan]){
                left = mid+1;
            }
            else if(target < matrix[mid][kiri]){
                right = mid-1;
            }
            else{
                while(kiri <= kanan){
                    int tengah = (kiri+kanan) / 2;
                    if(matrix[mid][tengah] == target){
                        return true;
                    }
                    else if(matrix[mid][tengah] < target){
                        kiri = tengah+1;
                    }
                    else{
                        kanan = tengah-1;
                    }
                }
                return false;
            }
        }
        return false;
    }
};
