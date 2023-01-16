#include "../lib/parse.h"

using namespace std;

vector<vector<double>> parse(char *fileName) {
  vector<vector<double>> data;

  ifstream raw;
  raw.open(fileName);

  string rawVector;
  if (raw.is_open()) {
    while (raw.good()) {
      vector<double> entry;
      getline(raw, rawVector);
      istringstream iss(rawVector);
      string token;

      while (getline(iss, token, ',')) {
        double attribute = atof(token.c_str());
        entry.push_back(attribute);
      }
      if (entry.size() > 0) {
        data.push_back(entry);
      }
    }
  }
  return data;
}
