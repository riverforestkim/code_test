#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int CheckPrime(int n)
{   
    if (n==1)
    {
        return 0;
    }
    
    if (n==2)
    {
        return 1;
    }
    
    for(int i = 2; i < n; i++)
    {
        if(n % i == 0)
        {
            return 0;
        }
    }

    return 1;
    
}

int main()
{
    int nTCCount;
    int nTemp;

    vector<int> vecAnswer;

    cin >> nTCCount;

    for (int i = 0; i < nTCCount; i++)
    {
        cin >> nTemp;

        int result = CheckPrime(nTemp);

        if (result == 1)
        {
            vecAnswer.push_back(nTemp);
        }
    }

    cout << vecAnswer.size();

    return 0;
}
