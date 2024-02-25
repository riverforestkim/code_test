#include <iostream>
using namespace std;
 
int main() {
    int T, n;
    cin >> T;
 
    while (T--) {
        cin >> n;
        int digit = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                cout << digit << " ";
            }
            n /= 2;
            digit++;
        }
    }
}