#include "svd.h"
using namespace std;
using namespace Eigen;
/**
 * A simple class to describe the Singular Value decomposition of a matrix.
 */
class SVD {
public:
  SVD(MatrixXf U, MatrixXf S, MatrixXf V) {
    this->U = U;
    this->S = S;
    this->VT = V.transpose();
  }
  MatrixXf U;
  MatrixXf S;
  MatrixXf VT;
};
/**
 * A method to convert the data array into an array of blocks represented as a
 * vector<MatrixXf>.
 * @param in: the input containing the host data in their original format
 * @returns: the host data in its converted form.
 */
vector<MatrixXf> toBlocks(vector<double> in) {
  vector<MatrixXf> res;
  for (int i = 0; i < in.size() - 15; i += 16) {
    MatrixXf block(4, 4);
    block << in[i], in[i + 1], in[i + 2], in[i + 3], in[i + 4], in[i + 5],
        in[i + 6], in[i + 7], in[i + 8], in[i + 9], in[i + 10], in[i + 11],
        in[i + 12], in[i + 13], in[i + 14], in[i + 15];
    res.push_back(block);
  }
  return res;
}

/**
 * A method using the Eigen library to convert an original matrix A into its
 * Singular Value Decomposition.
 * @param A: The original matrix A
 * @returns: The Singular value decomposition
 */
SVD decompose(MatrixXf A) {
  Eigen::JacobiSVD<Eigen::MatrixXf> svd;
  svd.compute(A, Eigen::ComputeFullV | Eigen::ComputeFullU);
  Eigen::MatrixXf singular(4, 4);
  singular << svd.singularValues()[0], 0, 0, 0, 0, svd.singularValues()[1], 0,
      0, 0, 0, svd.singularValues()[2], 0, 0, 0, 0, svd.singularValues()[3];
  return SVD(svd.matrixU(), singular, svd.matrixV());
}
