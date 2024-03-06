#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int N, S;
vector<int> vecNum;

int nBuffer;

int main()
{
    cin >> N;
    cin >> S;

    for(int i=0; i<N; i++)
    {
        cin >> nBuffer;
        vecNum.push_back(nBuffer);
    }

    int nStart = 0, nEnd = 0, nSum = 0, nMinLen = -1;

    while(nStart <= nEnd)
    {
        //현재 값이 이미 목표치와 같거나 넘어섰으면 빼준다
        if(nSum >= S)
        {   
            if(nMinLen == 0 || nMinLen == -1)
            {
                nMinLen = nEnd - nStart;
            }
            else
            {
                nMinLen = min(nMinLen, nEnd - nStart);
            }
            
            nSum -= vecNum[nStart++];
        }
        // 끝까지 돌았으면, break
        else if(nEnd == N)
        {
            break;
        }
        // end 값을 더해준다
        else
        {
            nSum += vecNum[nEnd++];
        }
    }

    if (nMinLen == -1)
    {
        cout << 0;
    }
    else
    {
        cout << nMinLen;
    }

    return 0;
}