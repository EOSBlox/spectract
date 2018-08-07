#!/bin/sh
SPECTRACT=../spectract.py
CXX=c++
CFLAGS="-std=c++14 -Wall"

for f in good_*.json; do
  # Generate header file.
  TMP=$f.h
  rm -f ${TMP}
  echo "Testing $f -> ${TMP}.."
  ${SPECTRACT} $f ${TMP} >/tmp/good.txt
  if [ ! $? -eq 0 ]; then
    echo "$f FAILED!"
    if [ -f /tmp/good.txt ]; then
      echo "=== OUTPUT ==="
      cat /tmp/good.txt
      echo "=============="
    fi
    exit 1
  fi

  # Compile and test header file.
  SRC=$(echo $f | sed s,json,cc,g)
  EXEC=$(echo $f | sed s,.json,.bin,g)
  echo "Compiling ${SRC} -> ${EXEC}.."
  ${CXX} ${CFLAGS} ${SRC} -o ${EXEC}

  # Running executable.
  echo "Running ${EXEC}.."
  ./${EXEC}
  if [ ! $? -eq 0 ]; then
    echo "${EXEC} FAILED!"
    exit 1
  fi
done
