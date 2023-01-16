#include "emb.h"
using namespace std;
using namespace Eigen;

bool verbose;
double threshold = 0.00002;

/**
 * A method to watermark the U matrix of the SVD.
 * @param svd: A pointer to the SVD instance of the class defined above
 * @param w: The watermark bit represented as a boolean
 */
void watermarkU(SVD *svd, bool w) {
  MatrixXf U = svd->U;
  double first = U(1, 0);
  double second = U(2, 0);
  int sign_first = first > 0 ? 1 : -1;
  int sign_second = second > 0 ? 1 : -1;
  double diff = fabs(first) - fabs(second);
  if ((diff > threshold && w) || (diff < -threshold && !w)) {
    return;
  } else if (w) {
    U(1, 0) = sign_first * fabs(fabs(first) + (threshold - diff) / 2);
    U(2, 0) = sign_second * fabs(fabs(second) - (threshold - diff) / 2);
  } else if (!w) {
    U(1, 0) = sign_first * fabs(fabs(first) - (threshold + diff) / 2);
    U(2, 0) = sign_second * fabs(fabs(second) + (threshold + diff) / 2);
  }
  svd->U = U;
}

/**
 * A method to watermark an attribute array with the given watermark (defined in
 * the header file).
 * @param attributeArray the host data attribute to be watermarked
 * @returns: A tuple with the watermarked attribute and the maximum value (used
 * to extract the watermark)
 */
tuple<vector<double>, double>
watermarkAttribute(vector<double> attributeArray) {
  double max = *max_element(attributeArray.begin(), attributeArray.end());
  cout << to_string(max) << endl;
  for (int i = 0; i < attributeArray.size(); i++) {
    attributeArray[i] = attributeArray[i] / max;
  }
  vector<MatrixXf> blocks = toBlocks(attributeArray);
  int size =
      blocks.size() > watermark.size() ? watermark.size() : blocks.size();
  vector<double> wm_data;
  for (int i = 0; i < size; i++) {
    MatrixXf A = blocks[i];
    SVD decomposition = decompose(A);

    if (verbose) {
      cout << "U:" << endl << decomposition.U << endl;
    }
    watermarkU(&decomposition, watermark[i]);
    MatrixXf reconstructed =
        decomposition.U * decomposition.S * decomposition.VT;

    if (verbose) {
      cout << "watermarked U: " << endl << decomposition.U << endl;
      cout << "Watermarked data: " << endl << reconstructed << endl;
    }
    for (int x = 0; x < 4; x++) {
      for (int y = 0; y < 4; y++) {
        wm_data.push_back(reconstructed(x, y) * max);
      }
    }
  }
  return make_tuple(wm_data, max);
}

/**
 * A simple method to calculate the variance and mean of an array.
 * @param arr: the input array
 * @returns: A tuple containing the mean and variance (in that order)
 */
tuple<double, double> calcMeanAndStandardVariance(vector<double> arr) {
  double mean = 0;
  for (int i = 0; i < arr.size(); i++) {
    mean += arr[i];
  }
  mean = mean / double(arr.size());
  double variance = 0;
  for (int i = 0; i < arr.size(); i++) {
    variance += pow(arr[i] - mean, 2);
  }
  variance = variance / arr.size();
  tuple<double, double> res;
  return make_tuple(mean, variance / mean);
}

/**
 * A method to write the data to a file in the data folder.
 * @param wm_data: an array containing the watermarked attribute.
 * @param data: an array containing the original host data
 * @param wm_index: the index of the watermarked attribute
 * @param maximum: the maximum value of the original, watermarked,
 * attribute
 */
void writeWatermarkedData(vector<double> wm_data, vector<vector<double>> data,
                          int wm_index, double maximum) {
  int dimensions = data[0].size();
  // Delete everything from result file
  ofstream file_delete;
  file_delete.open("../data/wm.txt", ofstream::out | ofstream::trunc);
  file_delete.close();

  // Start the writing process of the watermarked dataSet
  cout << "write data to file" << endl;
  ofstream file;
  file.open("../data/wm.txt", ofstream::out | ofstream::trunc);
  for (int i = 0; i < wm_data.size(); i++) {
    for (int j = 0; j < dimensions - 1; j++) {
      if (j == wm_index) {
        file << to_string(wm_data[i]) << ", ";
      } else {
        file << to_string(data[i][j]) << ", ";
      }
    }
    file << to_string(data[i][dimensions - 1]) << "\n";
  }

  for (int i = wm_data.size(); i < data.size(); i++) {
    for (int j = 0; j < dimensions - 1; j++) {
      file << to_string(data[i][j]) << ", ";
    }
    file << to_string(data[i][dimensions - 1]) << "\n";
  }

  // Print all the needed information to the console
  cout << "watermarked attribute: " << to_string(wm_index)
       << " and max: " << to_string(maximum) << endl;
  file.close();
}

int main(int argc, char **argv) {
  verbose = stoi(argv[1]);
  if (argc > 2) {
    threshold = stod(argv[2]);
  }
  vector<vector<double>> data = parse("../data/Dry_Bean.txt");
  if (argc > 3) {
    // if The third argument is a 1 we watermark the iris dataset otherwise the
    // bean dataset.
    // By default watermark the dry-bean dataset.
    if (stod(argv[3]) == 1) {
      data = parse("../data/iris.txt");
      watermark = {};
      for (int i = 0; i < 30; i++) {
        watermark.push_back(int(distribution(gen)));
      }
    }
  }

  cout << "watermarking data with threshold: " << to_string(threshold) << endl;
  // Find out some information about the dataset (mean, variance, dimensions)
  // Find out the attribute with the lowest variance to watermark.
  vector<double> attribute_lowst_var;
  int dimensions = data[0].size();
  int wm_index = 0;
  double lowest_var = INT_MAX;
  for (int i = 0; i < dimensions - 1; i++) {
    vector<double> attribute;
    for (int j = 0; j < data.size(); j++) {
      attribute.push_back(data[j][i]);
    }
    tuple<double, double> var = calcMeanAndStandardVariance(attribute);
    if (get<1>(var) < lowest_var) {
      attribute_lowst_var = attribute;
      lowest_var = get<1>(var);
      wm_index = i;
    }
  }

  // attribute_lowst_var = {1, 2, 3, 4, 1, 3, 2, 3, 1, 0, 3, 4, 1, 2, 3, 4};
  // watermark = {0};

  // Start the watermarking process of the attribute
  cout << "watermarking attribute with variance: " << lowest_var << endl;
  tuple<vector<double>, double> res = watermarkAttribute(attribute_lowst_var);

  vector<double> wm_data = get<0>(res);
  double maximum = get<1>(res);

  writeWatermarkedData(wm_data, data, wm_index, maximum);
}
