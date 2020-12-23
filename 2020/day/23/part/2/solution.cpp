#include <cstdint>
#include <iostream>
#include <list>
#include <map>
#include <string>
#include <utility>
#include <vector>

void create_cups(const std::vector<int64_t> &input, std::list<int64_t> &c,
                 std::map<int64_t, std::list<int64_t>::iterator> &m,
                 bool debug = true) {
  for (int64_t i = 0; i < input.size(); ++i) {
    int64_t num = input[i];
    c.push_back(num);
    auto last_node = c.end();
    --last_node;
    if (debug) {
      std::cout << *(last_node) << std::endl;
    }
    m[num] = last_node;
  }
}

void print_cup_list(const std::list<int64_t> &cup_list,
                    const std::list<int64_t>::iterator &pos_it) {
  std::cout << "cups: ";
  for (auto iter = cup_list.begin(); iter != cup_list.end(); ++iter) {
    if (iter == pos_it) {
      std::cout << '(' << *iter << ") ";
    } else {
      std::cout << *iter << " ";
    }
  }
  std::cout << std::endl;
}

void complete_game(std::list<int64_t> &cup_list,
                   std::map<int64_t, std::list<int64_t>::iterator> &cup_map,
                   int64_t moves = 100, bool debug = true) {
  std::list<int64_t>::iterator pos_it = cup_list.begin();
  for (int move = 1; move <= moves; ++move) {
    if (debug) {
      std::cout << "-- move " << move << " --" << std::endl;
    }

    int64_t first = *pos_it;

    if (debug) {
      print_cup_list(cup_list, pos_it);
    }

    std::vector<int64_t> next_three{};
    std::list<int64_t>::iterator next_it = pos_it;
    ++next_it;
    for (int64_t i = 0; i < 3; ++i) {
      if (next_it == cup_list.end()) {
        next_it = cup_list.begin();
      }
      auto next = *next_it;
      next_three.push_back(next);
      next_it = cup_list.erase(next_it);
      cup_map.erase(next);
    }

    if (debug) {
      std::cout << "pick up: ";
      for (int64_t i = 0; i < 3; ++i) {
        if (i != 0) {
          std::cout << ", ";
        }
        std::cout << next_three[i];
      }
      std::cout << std::endl;
    }

    int64_t destination_label = first - 1;
    while (cup_map.find(destination_label) == cup_map.end()) {
      if (destination_label <= cup_map.begin()->first) {
        auto max = cup_map.end();
        --max;
        destination_label = max->first;
      } else {
        --destination_label;
      }
    }
    if (debug) {
      std::cout << "destination: " << destination_label << std::endl;
    }

    auto destination_cup = cup_map[destination_label];
    ++destination_cup;
    for (int64_t i = 2; i >= 0; --i) {
      destination_cup = cup_list.insert(destination_cup, next_three[i]);
      cup_map[next_three[i]] = destination_cup;
    }

    ++pos_it;
    if (pos_it == cup_list.end()) {
      pos_it = cup_list.begin();
    }
  }

  if (debug) {
    std::cout << "-- final --" << std::endl;
    print_cup_list(cup_list, pos_it);
  }
}

int main() {
  std::string input = "962713854";
  int64_t v_len = 1000000;
  int64_t moves = 10000000;
  bool debug = false;

  int64_t max = INT64_MIN;
  std::vector<int64_t> v{};
  for (char c : input) {
    int64_t z = c - '0';
    if (z > max) {
      max = z;
    }
    v.push_back(z);
  }

  ++max;
  for (; v.size() < v_len; ++max) {
    v.push_back(max);
  }

  std::list<int64_t> cup_list{};
  std::map<int64_t, std::list<int64_t>::iterator> cup_map{};

  create_cups(v, cup_list, cup_map, debug);

  complete_game(cup_list, cup_map, moves, debug);

  std::vector<int64_t> result{};
  auto start_it = cup_map[1];
  int64_t prod = 1;
  ++start_it;
  if (start_it == cup_list.end()) {
    start_it = cup_list.begin();
  }
  prod *= *start_it;
  ++start_it;
  if (start_it == cup_list.end()) {
    start_it = cup_list.begin();
  }
  prod *= *start_it;
  std::cout << prod << std::endl;
}
