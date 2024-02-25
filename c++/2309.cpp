#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int nTemp;
    int nSum = 0;
    vector<int> vecLen;

    for (int i=0; i<9; i++)
    {
        cin >> nTemp;
        vecLen.push_back(nTemp);
        nSum += nTemp;
    }
    

    sort(vecLen.begin(), vecLen.end());
    
    int nAIdx;
    int nBIdx;
    

    //키의 합이 100이 되어야한다.
    //브루트포스, 모든 경우의 수를 구해서 제외 인덱스 두개를 구해낸다.
    for (int i=0; i<9; i++)
    {
        for (int j=0; j<9; j++)
        {
            if (nSum - (vecLen[i] + vecLen[j]) == 100 )
            {
                nAIdx = i;
                nBIdx = j;
            }
        }
    }
    
    for (int i=0; i<9; i++)
    {
        if (i != nAIdx && i != nBIdx)
        {
            cout << vecLen[i] << endl;
        }
    }
    
    return 0;
}