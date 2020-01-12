#include <iostream>
using namespace std;

int getSum(int array[], int n) {
	cout << "변수는 어디서나 선언이 가능합니다" << endl;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += array[i];
	}
	return 0;
}