class Solution
{
public:
    int balancedStringSplit(string s)
    {
        int balance = 0;
        int counter = 0;
​
        for (size_t i = 0; i < s.size(); i++)
        {
            if (s[i] == 'L')
            {
                balance++;
            }
            else
            {
                balance--;
            }
            if (balance == 0)
            {
                counter++;
            }
        }
        return counter;
    }
};
