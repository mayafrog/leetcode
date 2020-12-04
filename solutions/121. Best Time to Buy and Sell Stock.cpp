class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if (prices.size() == 0 || prices.size() == 1)
        {
            return 0;
        }
​
        int min = prices[0];
        int maxprofit;
        for (size_t i = 0; i < prices.size(); i++)
        {
            if (prices[i] < min)
            {
                min = prices[i];
            }
            else if (prices[i] - min > maxprofit)
            {
                maxprofit = prices[i] - min;
            }
        }
        return maxprofit;
    }
};
