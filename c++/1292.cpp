#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //1 22 333 .. 이런 수열을 만들어야함

    vector<int> vecData;

    int nStart;
    int nEnd;

    int answer = 0;

    //1 ≤ A ≤ B ≤ 1,000
    for (int i = 1; i < 1001; i++)
    {
        //1 22 333 이런 구조를 만들기 위해 중첩 포문
        for(int j = 0; j < i; j++)
        {
            vecData.push_back(i);
        }
    } 
    
    cin >> nStart;
    cin >> nEnd;
    
    for(int i = nStart -1; i <= nEnd -1; i++)
    {
        answer += vecData[i];
    }

    cout << answer;

    return 0;

}