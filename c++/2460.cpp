#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //10개의 역을 거치면서 각각 총 탑승객 수 벡터
    vector<int> vecTotalCount;

    int nQuit;
    int nEnter;
    int nDiff;
    int nMax = 0;

    for (int i = 0; i < 10; i++)
    {
        cin >> nQuit;
        cin >> nEnter;

        //첫 번째 역에서는 과거 데이터가 없기 때문에 그냥 더한다
        if (i==0)
        {
            nDiff = nEnter-nQuit;
            
        }
        else
        {
            nDiff = vecTotalCount[i-1] + (nEnter-nQuit);
        }

        vecTotalCount.push_back(nDiff);

        if (nDiff > nMax)
        {
            nMax = nDiff;
        }
    }


    cout << nMax;

    return 0;
}