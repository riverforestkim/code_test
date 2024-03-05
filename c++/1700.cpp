#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int nHole;
int nTool;

int nUnplug = 0;

const int MAX = 100 + 1;
int nArrTool[MAX], nArrUse[MAX];

int main()
{
    cin >> nHole;
    cin >> nTool;

    for(int i = 0; i < nTool; i++)
    {
        cin >> nArrTool[i];
    }

    //들어올 순서를 포문으로 돌린다.

    for(int i = 0; i < nTool; i++)
    {

        bool chkPlug = false;

        //콘센트 상태를 체크한다.
        for(int j = 0; j < nHole; j++)
        {
            if (nArrUse[j] == nArrTool[i])
            {
                chkPlug = true;
                break;
            }
        }

        //지금 꽂혀있는 상태면 밑에 로직을 탈 이유가 없다
        if(chkPlug)
        {
            continue;
        }


        //빈 콘센트 확인
        for(int j = 0; j < nHole; j++)
        {
            if (!nArrUse[j])
            {
                //꽂는다
                nArrUse[j] = nArrTool[i];
                chkPlug = true;
                break;
            }
        }

        //지금 꽂혀있는 상태면 밑에 로직을 탈 이유가 없다
        if(chkPlug)
        {
            continue;
        }

        int nIdx, nDeviceIdx = -1;
        //이제 꽉찬 상태에서 뽑을 것을 찾을 차례
        for(int j = 0; j < nHole; j++)
        {
            //남은 벡터에서 가장 적게 남은 것을 뽑으면 된다
            int nLastIdx = 0;

            for (int k = i + 1; k <nTool; k++)
            {
                if (nArrUse[j] == nArrTool[k])
                {
                    break;
                }
                nLastIdx++;
            }

            if (nLastIdx > nDeviceIdx)
            {
                nIdx = j;
                nDeviceIdx = nLastIdx;
            }

        } 
        nUnplug++;

        //가장 적게 남은 것을 빼고 지금 것으로 바꾼다
        nArrUse[nIdx] = nArrTool[i];



    }

    cout << nUnplug;
    return 0;
}