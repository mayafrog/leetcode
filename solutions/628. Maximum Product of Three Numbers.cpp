class Solution
{
public:
   int maximumProduct(vector<int> &nums)
   {
      sort(nums.begin(), nums.end());
      int index = nums.size() - 1;
​
      int min1 = nums[0];
      int min2 = nums[1];
​
      int max1 = nums[index];
      int max2 = nums[index - 1];
      int max3 = nums[index - 2];
​
      if (max1 * max2 * max3 > max1 * min1 * min2)
      {
         return max1 * max2 * max3;
      }
      else
      {
         return max1 * min1 * min2;
      }
   }
};
