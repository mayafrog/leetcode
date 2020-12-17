class Solution
{
public:
    vector<int> smallerNumbersThanCurrent(vector<int> &nums)
    {
        std::vector<int> result(nums.size());
        int counter = 0;
        for (size_t i = 0; i < nums.size(); i++)
        {
            for (size_t j = 0; j < nums.size(); j++)
            {
                if (nums[i] > nums[j] && i != j)
                {
                    counter++;
                }
            }
            result[i] = counter;
            counter = 0;
        }
        return result;
    }
};
