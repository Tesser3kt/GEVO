#include <iostream>

using namespace std;

bool onlyOnesAndZeroes(int num) {
  string numAsString = to_string(num);
  for (int i = 0; i < numAsString.length(); i++) {
    if (numAsString[i] != '0' && numAsString[i] != '1') {
      return false;
    }
  }
  return true;
}

int main() {
  int N, num;

  cout << "Zadejte cislo: ";
  cin >> N;
  cout << endl;
  num = N;

  while (!onlyOnesAndZeroes(num)) {
    num += N;
  }

  cout << num << endl;
}
