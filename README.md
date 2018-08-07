# spectract
Customize EOS smart contracts using JSON data compiled into C++ header files.

## Prerequisites
Compiling JSON into C++ header requires only Python 3+.

Using C++ header with EOS smart contract requires only the `eosiocpp` compiler.

## Usage
```
./spectract.py <spec json input file> <output c++ header file>
```

The input JSON file must consist of a JSON object with each value being the variable name in C++, pointing to a JSON object describing value and type.

## Example
Assume the following is contained in "data.json":
```json
{
  "num": {
    "value": 42,
    "type": "uint8_t"
  },
  "str": {
    "value": "John Doe",
    "type": "std::string"
  },
  "float_": {
    "value": 3.1415,
    "type": "float"
  },
  "double_": {
    "value": 42.987654321,
    "type": "double"
  }
}
```

It is a breeze to compile into a C++ header "data.h":
```shell
% ./spectract.py data.json data.h
```

"data.h" now contains:
```cpp
#ifndef SPECTRACT_DATA_H

namespace spectract {

struct data {
  const uint8_t num = 42;
  const std::string str = "John Doe";
  const float float_ = 3.1415;
  const double double_ = 42.987654321;
};

} // namespace spectract

#endif // SPECTRACT_DATA_H
```

Finally, in a smart contract the values can be accessed like:
```cpp
spectract::data d;
printf("My name is %s\n", d.str);
// "My name is John Doe"
```
