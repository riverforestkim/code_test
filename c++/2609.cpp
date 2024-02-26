#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

void GetMaxDiv(int aNum, int bNum)
{

    int nBiggerNum;
    int nMaxDiv = 0;

    if (aNum >= bNum)
    {
        nBiggerNum = aNum;
    }
    else
    {
        nBiggerNum = bNum;
    }

    // 두 수 모두의 약수면서 가장 큰 약수를 구한다.
    for(int i = 1; i<=nBiggerNum; i++)
    {
        if(aNum % i ==0 && bNum % i ==0 )
        {
            nMaxDiv = i;
        }
    }

    cout << nMaxDiv << endl;
    
    return;
}


void GetMinMul(int aNum, int bNum)
{

    int nSmallerNum;
    int nNum;
    int nMinMul = aNum * bNum;

    if (aNum <= bNum)
    {
        nSmallerNum = aNum;
        nNum = bNum;
    }
    else
    {
        nNum = aNum;
        nSmallerNum = bNum;
    }
    //최소 공배수를 구한다.
    //결국 가장 큰 경우의 수가 서로 곱한 것이니, 그 조건으로 포문을 돌린다
    for(int i = 1; i<=nSmallerNum; i++)
    {
        if ((nNum * i) % nSmallerNum == 0 && (nNum * i) < nMinMul)
        {
            nMinMul = nNum * i;
        }
    }

    cout << nMinMul << endl;
    
    return;
}


int main()
{
    int nANum;
    int nBNum;

    cin >> nANum;
    cin >> nBNum;

    GetMaxDiv(nANum, nBNum);
    GetMinMul(nANum, nBNum);


    return 0;
}
