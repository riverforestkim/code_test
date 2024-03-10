#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string sWord;
string sPattern;

//kmp

vector<int> getPi(string sTempPattern)
{

    int cLen = sTempPattern.size();
    int j = 0;
    vector<int> Pi(cLen, 0);


    for(int i = 1; i < cLen; i++)
    {

        while(j > 0 && sTempPattern[i] != sTempPattern[j])
        {
            j = Pi[j - 1];
        }

        if (sTempPattern[i] == sTempPattern[j])
        {
            Pi[i] = ++j;
        }

    }

    return Pi;

}

void kmp(string sTempWord, string sTempPattern)
{
    vector<int> pi = getPi(sTempPattern);
    int wLen = sTempWord.size();
    int cLen = sTempPattern.size();
    int j = 0;

    for(int i = 0; i < wLen; i++)
    {
        while(j>0 && sTempWord[i] != sTempPattern[j])
        {
            j = pi[j-1];
        }
        if (sTempWord[i] == sTempPattern[j])
        {
            if(j == cLen - 1)
            {
                j = pi[j];
                cout << 1;
                return; 
            }
            else 
            {
                j++;
            }
        }
    }

    cout << 0;
    return;
}


int main()
{

    cin >> sWord;
    cin >> sPattern;

    
    kmp(sWord, sPattern);

    

    return 0;
}