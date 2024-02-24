#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>

using namespace std;

int CheckValid(string str) {
    
    // 정상적으로 괄호가 닫히는지 확인하는 로직
    stack<char> sTC;

    for(int j = 0; j < str.size(); j++)
    {
        if(str[j] == '(')
        {
            sTC.push(str[j]);
        }
        else
        {
            //만약 큐에 ( 가 남아있지 않다면, 잘못된 케이스다
            if(sTC.empty())
            {
                cout << "NO" << endl;
                return 0;
            }
            else
            {
                sTC.pop();
            }
        }
    } 

    if (!sTC.empty())
    {
        cout << "NO" << endl;
        return 0;
    }

    // 만약 맞다면, 스트링 출력
    cout << "YES" << endl;
    return 0;
}

int main()
{
    vector<string> vecTC;
    int nCount;
    string Temp;

    // TC 개수를 구한다
    cin >> nCount;

    //TC를 입력하고 벡터에 넣는다
    for(int i = 0; i < nCount; i++)
    {
        cin >> Temp;
        vecTC.push_back(Temp);
    }

    //백터 내 TC 를 꺼내서 판단한다
    for_each(vecTC.begin(), vecTC.end(), CheckValid);


    return 0;
}