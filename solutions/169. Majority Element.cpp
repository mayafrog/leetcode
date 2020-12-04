class Solution
{
public:
   int majorityElement(vector<int> &nums)
   {
      int max = 0;
      int max_index;
      map<int, int> hashmap;
      for (size_t i = 0; i < nums.size(); i++)
      {
         hashmap[nums[i]]++;
      }
      for (auto &j : hashmap)
      {
         cout << j.first << " " << j.second << endl;
         if (j.second > max)
         {
            max = j.second;
            max_index = j.first;
         }
      }
      return max_index;
   }
};
