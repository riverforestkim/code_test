#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;


int main()
{
    int nH, nW, nTotal = 0, nTemp = 0, nSum = 0;

    vector<int> vecRoad;

    cin >> nH;
    cin >> nW;

    for(int i = 0; i < nW; i++)
    {
        cin >> nTemp; 
        vecRoad.push_back(nTemp);
    }

    for(int i = 0; i < vecRoad.size(); i++)
    {
      
        if(i==0 || i == vecRoad.size() -1 )
        {
        continue;
        }

        // 내 기준 좌 / 우 max 값 중 작은 값을 기반으로 쌓인 것을 확인한다.
        vector<int> vecLeft(vecRoad.begin(), vecRoad.begin() + i);
        vector<int> vecRight(vecRoad.begin() + i, vecRoad.end());

        int nLeftMax = *max_element(vecLeft.begin(), vecLeft.end());
        int nRightMax = *max_element(vecRight.begin(), vecRight.end());

        if (nLeftMax < nRightMax)
        {
            nTemp = nLeftMax - vecRoad[i];
        }
        else
        {
            nTemp = nRightMax - vecRoad[i];
        }
 
        // 지금 인덱스의 길이가 최소 값보다 길면, 빗물이 쌓이지 않는다
        if (nTemp < 0)
        {
            continue;
        }
        
        nTotal += nTemp;

    }

    cout << nTotal;

}