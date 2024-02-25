#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

void CheckNum(int nNum, int nOrder) {

    //모듈화..
    //약수 벡터
    vector<int> vecNum;

    //약수 벡터 채우기
    for(int i=1; i<=nNum; i++)
    {
        if(nNum % i == 0)
        {
            vecNum.push_back(i);
        }

    }

    cout << vecNum[nOrder - 1];

}

int main()
{

    int nNum;
    int nOrder;

    cin >> nNum;
    cin >> nOrder;

    //답 뱉기
    CheckNum(nNum, nOrder);

    return 0;
}