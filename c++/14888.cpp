#include <iostream>
#include <vector>
#include <climits>

using namespace std;

// 수 개수
int nCount;

// 수 벡터
vector <int> vecNum;
// 연산자 벡터
vector <int> vecOp;

int nTemp;
int nMax = INT_MIN;
int nMin = INT_MAX;

// 입력받은 모든 수 모두 써야 답이 나오니 DFS를 사용한다.
// 재귀적으로 쓸 수 있도록 짠다
// 인덱스와 누적 결과값을 계속 전달하며 진행한다.
void DFS(int n, int result)
{
	if (n == nCount - 1)
	{
		//마지막까지 돌았으면 result를 비교하고 뱉는다
		nMax = max(nMax, result);
		nMin = min(nMin, result);
	}

	//연산자 4가지
	for(int i = 0; i<4; i++)
	{
		//연산자가 있는지 체크한다.
		if(vecOp[i] > 0)
		{
			//depth, 깊이 우선으로 내려가는 시점에서 연산자 수를 사용한 만큼 빼고 전달한다.
			vecOp[i] = vecOp[i] - 1;

			//+
			if(i==0)
			{
				DFS(n+1, result + vecNum[n+1]);
			}
			//-
			else if (i==1)
			{
				DFS(n+1, result - vecNum[n+1]);
			}
			//*
			else if (i==2)
			{
				DFS(n+1, result * vecNum[n+1]);
			}
			// /
			else if (i==3)
			{
				DFS(n+1, result / vecNum[n+1]);
			}	
			
			//branch, 옆 브랜치 전달시 depth 이전 시점으로 연산자 수를 복구한다
			vecOp[i] = vecOp[i] + 1;
		}
	
	}

}


int main() {

	cin >> nCount;

	for (int i = 0; i < nCount; i++) {
		cin >> nTemp;
		vecNum.push_back(nTemp);
	}

	for (int i = 0; i < 4; i++) {
		cin >> nTemp;
		vecOp.push_back(nTemp);
	}

	//첫 수를 던져서 진행한다
	DFS(0, vecNum[0]);

	cout << nMax << '\n';
	cout << nMin << '\n';


	return 0;
	
}