#include <iostream>
#include <stack>

using namespace std;

int main()
{

    string strData;
    stack<char> sCheck;


    //() 2
    //[] 3
    //(x) 2x
    //[x] 3x
    //()[] 2+3

    cin >> strData;


    int nAnswer = 0;
    //주어진 문장의 값
    int nTemp = 1;


    for(int i = 0; i < strData.length(); i++)
    {
        //모든 경우의 수, [] ()
        if(strData[i] == '(')
        {
            //스택에 넣는다.
            sCheck.push('(');
            //문장 값에 적용한다.
            nTemp *= 2;

        }
        else if(strData[i] == '[')
        {
            //스택에 넣는다.
            sCheck.push('[');
            //문장 값에 적용한다.
            nTemp *= 3;

        }
        else if(strData[i] == ')')
        {
            //비어있거나, 가장 마지막으로 입력받은 괄호 시작부가 다르면 유효하지 않다
            if (sCheck.empty() || sCheck.top() == '[')
            {
                cout << 0;
                return 0;
            }

            sCheck.pop();
            
            //중첩 괄호가 끝나는지 체크, 이러면 밖 괄호 기준의 값으로 원복시키고, 지금 값은 answer 로 더한다.
            if(strData[i - 1] == '(')
            {
                nAnswer += nTemp;
                nTemp /= 2;
            }
            else
            {
                nTemp /= 2;
            }

        }
        else if(strData[i] == ']')
        {
            //비어있거나, 가장 마지막으로 입력받은 괄호 시작부가 다르면 유효하지 않다
            if (sCheck.empty() || sCheck.top() == '(')
            {
                cout << 0;
                return 0;
            }
            sCheck.pop();
            
            //중첩 괄호가 끝나는지 체크, 이러면 밖 괄호 기준의 값으로 원복시키고, 지금 값은 answer 로 더한다.
            if(strData[i - 1] == '[')
            {
                nAnswer += nTemp;
                nTemp /= 3;
            }
            else
            {
                nTemp /= 3;
            }

        }

    }

    //잔존 데이터가 있으면 0 리턴
    if (!sCheck.empty())
    {
        cout << 0;
        return 0;
    }

    cout << nAnswer;
    return 0;

}