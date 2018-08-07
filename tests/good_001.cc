#include <cstdint>
#include <string>

#include "testutils.h"
#include "good_001.json.h"

int main(int argc, char **argv)
{
  spectract::good_001_json data;
  ASSERT_EQ(data.num, 42)
  ASSERT_EQ(data.str, "John Doe")
  ASSERT_DOUBLE_EQ(data.float_, 3.1415)
  ASSERT_DOUBLE_EQ(data.double_, 42.987654321)
  return 0;
}
