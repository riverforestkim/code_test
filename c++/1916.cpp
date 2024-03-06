#include<iostream>
#include<vector>
#include<algorithm>
#include <queue>
#include <climits>

#define MAX 1001
#define BMAX 100001
#define INF 987654321

using namespace std;

int N, M;
int dist[MAX];
string strBuffer;

int nStart, nEnd;
vector<pair<int, int>> busVec[MAX];

void Dijkstra()
{
    priority_queue<pair<int, int>> pQueue;
    pQueue.push(make_pair(nStart, 0));


    while(!pQueue.empty())
    {
        int nNow = pQueue.top().first;
        int nCost = pQueue.top().second;
        pQueue.pop();

        //최소 코스트가 아니라 진행할 의미가 없다.
        if(dist[nNow] < nCost)
        {
            continue;
        }

        for(int i = 0; i < busVec[nNow].size(); i++)
        {
            int nArrive = busVec[nNow][i].first;
            int nBusCost = busVec[nNow][i].second + nCost;
            
            //같은 목적지의 코스트가 지금보다 크면 지금이 최소 값이므로 설정
            if(dist[nArrive] > nBusCost )
            {   
                dist[nArrive] = nBusCost;
                pQueue.push(make_pair(nArrive, nBusCost));
            }
        }
    }

    cout << dist[nEnd];

}

int main()
{

    //도시 개수
    cin >> N;
    //버스 개수
    cin >> M;

    for(int i = 0; i < M; i++)
    {
        vector<string> vecTemp;

        cin >> strBuffer;
        int nStartIdx = stoi(strBuffer);

        cin >> strBuffer;
        int nEndIdx = stoi(strBuffer);
        
        cin >> strBuffer;
        int nTempCost = stoi(strBuffer);

        busVec[nStartIdx].push_back(make_pair(nEndIdx, nTempCost));
    }

    //출발점
    cin >> nStart;
    //도착점
    cin >> nEnd;

    for(int i=1; i<=N; i++){
        dist[i]=INF;
    }

    Dijkstra();

    return 0;
}