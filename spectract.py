#!/usr/bin/env python3
import sys
import json
from os.path import exists, basename, splitext

NAMESPACE = "spectract"

def parseSpec(path):
  res = {}
  with open(path, mode="r") as fp:
    try:
      data = json.load(fp)
      for var in data:
        if var in res:
          print("Variable '{}' already defined!".format(var))
          exit(1)
        section = data[var]
        if "value" not in section or "type" not in section:
          print("Invalid entry variable '{}': {}".format(var, value))
          exit(1)
        value = section["value"]
        type_ = section["type"]
        res[var] = (value, type_)
    except Exception as ex:
      print("Failed to parse spec file: {}".format(ex))
      exit(1)
  return res

def formatEntry(entry, entries):
  section = entries[entry]
  value = section[0]
  if isinstance(value, str):
    value = "\"{}\"".format(value)
  return "const {} {} = {};\n".format(section[1], entry, value)

def writeHeader(entries, file):
  name = splitext(basename(file))[0].replace(".", "_")
  print("Writing '{}::{}' struct to '{}'".format(NAMESPACE, name, file))
  with open(file, mode="w+") as fp:
    fp.write("#ifndef SPECTRACT_DATA_H\n\n")
    fp.write("namespace {} {{\n\n".format(NAMESPACE))
    fp.write("struct {} {{\n".format(name))
    for entry in entries:
      fp.write("  " + formatEntry(entry, entries))
    fp.write("};\n\n")
    fp.write("}} // namespace {}\n\n".format(NAMESPACE))
    fp.write("#endif // SPECTRACT_DATA_H\n")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: {} <spec json input file> <output c++ header file>".format(sys.argv[0]))
    exit(1)

  specFile = sys.argv[1]
  headerFile = sys.argv[2]

  if not exists(specFile):
    print("Spec file doesn't exist: {}".format(specFile))
    exit(1)

  entries = parseSpec(specFile)
  elms = len(entries)
  if elms == 0:
    print("No variables specified in spec file!")
    exit(1)
  print("Found {} variables".format(elms))

  writeHeader(entries, headerFile)
