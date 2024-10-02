#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> square;

bool canBuild(square sq, vector<vector<int>> map, int R, int S) {
  bool hor, ver;
  // check that square is empty
  if (map[sq.first][sq.second] != 0) {
    return false;
  }

  // check horizontal barricades
  hor = false;
  if (sq.first > 0 && sq.first < R - 1) {
    if (map[sq.first - 1][sq.second] == 1 &&
        map[sq.first + 1][sq.second] == 1) {
      hor = true;
    }
  }

  // check vertical barricades
  ver = false;
  if (sq.second > 0 && sq.second < S - 1) {
    if (map[sq.first][sq.second + 1] > 0 && map[sq.first][sq.second - 1] > 0) {
      ver = true;
    }
  }

  return hor || ver;
}

vector<square> getNeighbors(square sq, vector<vector<int>> map, int R, int S) {
  vector<square> neighbors;

  // determine neighbors
  if (sq.first > 0) {
    neighbors.push_back(square(sq.first - 1, sq.second));
  }
  if (sq.first < R - 1) {
    neighbors.push_back(square(sq.first + 1, sq.second));
  }
  if (sq.second > 0) {
    neighbors.push_back(square(sq.first, sq.second - 1));
  }
  if (sq.second < S - 1) {
    neighbors.push_back(square(sq.first, sq.second + 1));
  }

  return neighbors;
}

void printMap(vector<vector<int>> map, int R, int S) {
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < S; j++) {
      switch (map[i][j]) {
      default:
        cout << '.';
        break;
      case 1:
        cout << '#';
        break;
      case 2:
        cout << 'B';
        break;
      case 69:
        cout << 'C';
        break;
      case -1:
        cout << 'H';
        break;
      case -2:
        cout << 'W';
        break;
      }
    }
    cout << endl;
  }
}

int main() {
  int R, S, col;
  string line;
  vector<vector<int>> map;
  square hydrant, sq;
  vector<square> barricades;
  queue<square> q;

  ifstream inputFile("uloha_2_2.txt");
  if (!inputFile.is_open()) {
    cout << "Error opening input file." << endl;
    return 1;
  }

  // read number of rows and columns
  getline(inputFile, line);
  R = stoi(line.substr(0, line.find(" ")));
  S = stoi(line.substr(line.find(" ")));

  // prepare array for input
  map = vector<vector<int>>(R);
  for (int i = 0; i < R; i++) {
    map[i] = vector<int>(S);
    for (int j = 0; j < S; j++) {
      map[i][j] = 0;
    }
  }

  // read input
  col = 0;
  for (int i = 0; i < R; i++) {
    getline(inputFile, line);

    for (char c : line) {
      if (c == '#') {
        map[i][col] = 1;
      } else if (c == 'H') {
        map[i][col] = -1;
        hydrant = square(i, col);
      }
      col++;
    }

    col = 0;
  }

  printMap(map, R, S);
  cout << endl;

  // flood Smolinec by BFS
  q.push(hydrant);

  while (!q.empty()) {
    sq = q.front();
    q.pop();

    if (map[sq.first][sq.second] != 0 && map[sq.first][sq.second] != -1) {
      // square occupied, cannot flood
      continue;
    }

    if (canBuild(sq, map, R, S)) {
      // build barricade if possible
      map[sq.first][sq.second] = 2;
      barricades.push_back(sq);
      continue;
    }

    // no obstacles, continue flooding
    map[sq.first][sq.second] = -2;
    for (square ngh : getNeighbors(sq, map, R, S)) {
      q.push(ngh);
    }
  }

  printMap(map, R, S);

  // print solution
  cout << "Solution:" << endl;
  cout << "---------" << endl;

  cout << barricades.size() << endl;
  for (square bar : barricades) {
    cout << bar.second + 1 << ' ' << bar.first + 1 << endl;
  }

  inputFile.close();
  return 0;
}
