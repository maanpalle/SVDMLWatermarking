#include "extr.h"

using namespace std;
using namespace Eigen;

int verbose = 0;

/**
 * A method to extract a watermark bit from a block.
 * @param block: A block of the data represented as a MatrixXf
 * @returns: the watermark bit
 */
bool extractWmFromBlock(MatrixXf block) {
  SVD svd = decompose(block);
  if (verbose) {
    cout << svd.U << endl;
    cout << to_string(abs(svd.U(1, 0))) << " " << to_string(abs(svd.U(2, 0)))
         << endl;
    cout << (abs(svd.U(1, 0)) > abs(svd.U(2, 0))) << endl;
  }
  return abs(svd.U(1, 0)) > abs(svd.U(2, 0));
}

/**
 * A method to extract the watermark from the attribute data. Divides data in
 * blocks and calls the method above.
 * @param data: the watermarked attribute
 * @returns: the watermark
 */
vector<bool> extractWm(vector<double> data) {
  vector<bool> res;
  vector<MatrixXf> blocks = toBlocks(data);

  for (int i = 0; i < blocks.size(); i++) {
    res.push_back(extractWmFromBlock(blocks[i]));
  }
  return res;
}

int main(int argc, char **argv) {
  vector<vector<double>> wm_data = parse("../data/wm.txt");
  vector<double> data;

  float max = -1;
  int wmIndex = -1;
  if (argc < 3) {
    return 0;
  } else {
    max = stod(argv[1]);
    wmIndex = stod(argv[2]);
    if (argc > 3) {
      int verbose = stod(argv[3]);
    }
  }

  for (int i = 0; i < wm_data.size(); i++) {
    data.push_back(wm_data[i][wmIndex] / max);
  }

  // Delete everything from output file.
  vector<bool> wm = extractWm(data);
  ofstream file_delete;
  file_delete.open("../data/wm_image.txt");
  file_delete.close();

  // Write to file
  ofstream file;
  file.open("../data/wm_image.txt");

  // Assume wm_image is square
  int size = pow(wm.size(), 0.5);
  for (int i = 0; i < pow(size, 2); i++) {
    if (i % size == 0 && i != 0) {
      if (verbose) {
        cout << endl;
      }
      file << endl;
    }
    file << to_string(wm[i]);
    if (verbose) {
      cout << wm[i];
    }
  }
  file.close();
  return 1;
}
