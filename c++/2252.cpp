#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int M;

vector<int> vecLine[100001];
int inDegree[100001];

void TopologicalSort()
{
    queue<int> q;

    for (int i = 1; i <= N; i++)
    {
        if(!inDegree[i])
        {
            q.push(i);
        }
    }
    while(!q.empty())
    {
        int nNow = q.front();
        q.pop();

        cout << nNow << ' ';

        for (int i = 0; i < vecLine[nNow].size(); i++)
        {
            inDegree[vecLine[nNow][i]]--;
            if(!inDegree[vecLine[nNow][i]])
            {
                q.push(vecLine[nNow][i]);
            }
        }
    }
}

int main()
{

    cin >> N;
    cin >> M;


    for(int i = 0; i < M; i++)
    {
        int a, b;

        cin >> a;
        cin >> b;

        vecLine[a].push_back(b);
        inDegree[b]++;
    }

    TopologicalSort();

    return 0;
}