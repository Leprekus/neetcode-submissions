class Solution {
   public:
      int search(std::vector<int>& nums, int target) {
         int size = nums.size();
         int L = 0;
         int R = size - 1;
         while(L < R) {
            int i = (L + R) / 2;
            if(nums.at(i) < target) {
               L = std::min(i + 1, size - 1);
            } else if (nums.at(i) > target) {
               R = std::max(i - 1, 0);
            } else {
               return i;
            }
         }
         
         if(L == R && 0 <= L && L < size && nums.at(L) == target) {
            return L;
         }
         return -1;
      }
};