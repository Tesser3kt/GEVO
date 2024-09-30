#include <fstream>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

int getTimeDelta(string time1, string time2) {
  // Calculates the time (in seconds) between time1 and time2 in format
  // HH:MM:SS.
  int h1, m1, s1, h2, m2, s2;

  h1 = stoi(time1.substr(0, 2));
  m1 = stoi(time1.substr(3, 2));
  s1 = stoi(time1.substr(6, 2));

  h2 = stoi(time2.substr(0, 2));
  m2 = stoi(time2.substr(3, 2));
  s2 = stoi(time2.substr(6, 2));

  if (h1 > h2) {
    // add 24 to h2 if crossed midnight
    h2 += 24;
  }

  // time delta
  return (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1);
}

pair<string, int> readTram(string line) {
  int spacePos, tramNumber;
  string time, tram;

  spacePos = line.find(" ");
  time = line.substr(0, spacePos);
  tram = line.substr(spacePos + 1, 1);

  tramNumber = stoi(tram);

  return pair<string, int>(time, tramNumber);
}

int findNewStart(int curIndex, int curStart, int curEnd, int tramCount[],
                 pair<string, int> tramSchedule[]) {
  int curTime, newTime;
  pair<string, int> tram;

  for (int i = curStart; i <= curIndex; i++) {
    tram = tramSchedule[i];
    if (i > 0 && tram.second == tramSchedule[i - 1].second) {
      // skip duplicates
      continue;
    }

    tramCount[tram.second] -= 1;
    if (tramCount[tram.second] == 0) {
      curTime = getTimeDelta(tramSchedule[curStart].first,
                             tramSchedule[curEnd].first);
      newTime =
          getTimeDelta(tramSchedule[i].first, tramSchedule[curIndex].first);

      if (newTime < curTime) {
        tramCount[tram.second] = 1;
        return i;
      }

      for (int j = i; j >= curStart; j--) {
        tram = tramSchedule[j];
        tramCount[tram.second] += 1;
      }
      return curStart;
    }
  }

  return curStart;
}

int main() {
  int spacePos, K, N, start, end, newStart, finalTime;
  string line;

  // open input file
  cout << "Reading input..." << endl;

  ifstream inputFile("uloha_1.txt");

  if (!inputFile.is_open()) {
    // opening failed
    cout << "Error reading input. Exiting..." << endl;
    return 1;
  }

  // read first line
  getline(inputFile, line);
  cout << "Reading K and N..." << endl;

  // split line to K & N
  spacePos = line.find(" ");
  K = stoi(line.substr(0, spacePos));
  N = stoi(line.substr(spacePos + 1, line.length()));

  // prepare array for storing schedule
  pair<string, int> tramSchedule[N];

  // prepare array for counting trams
  int tramCount[N + 1];
  for (int i = 0; i < N + 1; i++) {
    tramCount[i] = 0;
  }
  start = 0;
  end = 0;

  cout << "Reading trams..." << endl;
  // read trams one by one
  for (int i = 0; i < N; i++) {
    getline(inputFile, line);
    pair<string, int> tramData = readTram(line);
    tramSchedule[i] = tramData;

    if (i > 0 && tramData.second == tramSchedule[i - 1].second) {
      // skip duplicates
      continue;
    }

    tramCount[tramData.second] += 1;
    if (tramCount[tramData.second] == 1) {
      end = i;
      continue;
    }

    if (tramData.second == tramSchedule[start].second) {
      newStart = findNewStart(i, start, end, tramCount, tramSchedule);

      if (newStart != start) {
        start = newStart;
        end = i;
      }
    }
  }

  finalTime = getTimeDelta(tramSchedule[start].first, tramSchedule[end].first);
  cout << tramSchedule[start].first << " " << finalTime << endl;
  cout << "Finished reading input. Closing file." << endl;
  inputFile.close();
  return 0;
}
