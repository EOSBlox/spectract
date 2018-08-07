#include <cstdint>
#include <string>

#include "good_001.json.h"

int main(int argc, char **argv) {
  spectract::good_001_json data;
  const auto num = data.num; (void) num;
  const auto str = data.str; (void) str;
  const auto float_ = data.float_; (void) float_;
  const auto double_ = data.double_; (void) double_;
  return 0;
}
