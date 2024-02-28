#include <iostream>
#include <vector>

using namespace std;

int CheckPrime(int n)
{   
    if (n==1)
    {
        return 0;
    }
    
    if (n==2)
    {
        return 1;
    }
    
    for(int i = 2; i < n; i++)
    {
        if(n % i == 0)
        {
            return 0;
        }
    }

    return 1;
    
}

int main()
{
    //1 22 333 .. 이런 수열을 만들어야함

    vector<int> vecData;

    int nStart;
    int nEnd;

    int answer = 0;

    cin >> nStart;
    cin >> nEnd;

    int minPrime = nEnd;

    for(int i = nStart; i <= nEnd; i++)
    {
        int result = CheckPrime(i);

        if(result == 1)
        {
            answer += i;

            if( i < minPrime )
            {
                minPrime = i;
            }
        }
    }


    if(answer != 0)
    {
        cout << answer << endl;
        cout << minPrime << endl;

    } 
    else
    {
        cout << -1;
    }

    return 0;

}