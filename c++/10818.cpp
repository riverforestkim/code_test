#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;
 
int main() {
    int nCount;
    string strTemp;
 
    cin >> nCount;
    vector<int> vecNum;

    for(int i = 0; i < nCount; i++ )
    {
        cin >> strTemp;
        vecNum.push_back(stoi(strTemp));
    }

    sort(vecNum.begin(), vecNum.end());

    cout << vecNum[0] << " " << vecNum[nCount-1];

    return 0;
}