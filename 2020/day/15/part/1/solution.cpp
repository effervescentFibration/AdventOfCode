#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

void append_char_vec_as_num(std::vector<int64_t> &v,
                            const std::vector<char> &n) {
  v.push_back(std::stoi(std::string(n.begin(), n.end())));
}

std::vector<int64_t> inputs_from_line(std::string &line) {
  std::vector<int64_t> v{};
  std::vector<char> n{};
  for (char c : line) {
    if (c == '\n') {
      continue;
    }
    if (c == ',') {
      append_char_vec_as_num(v, n);
      n.clear();
      continue;
    }
    char c_val = c - '0';
    if (c_val >= 0 && c_val <= 9) {
      n.push_back(c);
    }
  }
  append_char_vec_as_num(v, n);
  return v;
}

void reflect_appearance_of_n_at_i(
    std::unordered_map<int64_t, std::vector<int64_t>> &d, int64_t n,
    int64_t i) {
  if (d.count(n) == 0) {
    d[n] = std::vector<int64_t>();
  }
  auto &p = d[n];
  if (p.size() < 2) {
    p.push_back(i);
  } else {
    p[0] = p[1];
    p[1] = i;
  }
}

int64_t generate_kth_spoken_num(const std::vector<int64_t> &t, int64_t k) {
  // Map a number to its last two appearances.
  std::unordered_map<int64_t, std::vector<int64_t>> d{};
  for (int64_t i = 0; i < int64_t(t.size()) - 1; ++i) {
    reflect_appearance_of_n_at_i(d, t[i], i);
  }
  int64_t last_i = t.size() - 1;
  int64_t last = t[last_i];
  while (last_i < k - 1) {
    reflect_appearance_of_n_at_i(d, last, last_i);
    if (d[last].size() < 2) {
      last = 0;
    } else {
      last = d[last][1] - d[last][0];
    }
    ++last_i;
  }
  return last;
}

int main() {
  std::string line;
  std::ifstream file("input");
  if (file.is_open()) {
    std::getline(file, line);
    file.close();
  } else {
    std::cout << "Cannot open file." << std::endl;
    return -1;
  }

  std::vector<int64_t> inputs = inputs_from_line(line);
  const int64_t k = 2020;
  int64_t solution = generate_kth_spoken_num(inputs, k);
  std::cout << solution << std::endl;
  return 0;
}
