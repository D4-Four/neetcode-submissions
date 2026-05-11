class Solution {
   public:
    int binser(vector<int>& num, int tar, int left, int right) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (num[mid] == tar) {
                return mid;
            } else if (num[mid] < tar) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        // binary search to find cut
        int l = 0, r = nums.size() - 1;
        if (nums[l] < nums[r]) {
            return binser(nums, target, l, r);
        } else {
            while (l < r) {
                int m = l + (r - l) / 2;
                if (nums[m] > nums[r]) {
                    // The drop must be to the right of m
                    l = m + 1;
                } else {
                    // m could be the pivot, or the pivot is to the left
                    r = m;
                }
            }
            int pivot = l;
            l = 0, r = nums.size() - 1;
            if (target >= nums[l] && target <= nums[pivot - 1]) {
                r = pivot - 1;
                return binser(nums, target, l, r);
            } else {
                l = pivot;
                return binser(nums, target, l, r);
            }
        }
        return -1;
    }
};
