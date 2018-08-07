#ifndef TESTS_TESTUTILS_H
#define TESTS_TESTUTILS_H

#include <cassert>
#include <cmath>
#include <iostream>

#define ASSERT_EQ(x, y)                                                                            \
  {                                                                                                \
    if (!(x == y)) {                                                                               \
      std::cout << "'" << x << "' NOT EQUAL TO '" << y << "'" << std::endl;                        \
      assert(x == y);                                                                              \
    }                                                                                              \
  }

static inline bool doubleEqual(const double a, const double b)
{
  constexpr double epsilon = 0.0000001;
  return std::abs(a - b) <= ((std::abs(a) < std::abs(b) ? std::abs(b) : std::abs(a)) * epsilon);
}

#define ASSERT_DOUBLE_EQ(x, y)                                                                     \
  {                                                                                                \
    if (!doubleEqual(x, y)) {                                                                      \
      std::cout.precision(12);                                                                     \
      std::cout << "'" << x << "' NOT EQUAL TO '" << y << "'" << std::endl;                        \
      assert(doubleEqual(x, y));                                                                   \
    }                                                                                              \
  }

#endif // TESTS_TESTUTILS_H
