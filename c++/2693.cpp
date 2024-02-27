#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int main()
{
    int nTCCount;
    int nTemp;

    vector<int> vecAnswer;

    cin >> nTCCount;

    for (int i = 0; i < nTCCount; i++)
    {
        vector<int> vecTemp;
        
        for (int j = 0; j < 10; j++)
        {
            cin >> nTemp;
            vecTemp.push_back(nTemp);
        }
        sort(vecTemp.begin(), vecTemp.end());
        vecAnswer.push_back(vecTemp[7]);
    }

    for (int i = 0; i < nTCCount; i++)
    {
        cout << vecAnswer[i] << endl;
    }


    return 0;
}
