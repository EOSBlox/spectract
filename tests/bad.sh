#!/bin/sh
SPECTRACT=../spectract.py
for f in bad_*.json; do
  echo "Testing $f.."
  ${SPECTRACT} $f /tmp/$f.h >/tmp/bad.txt
  if [ ! $? -gt 0 ]; then
    echo "$f FAILED!"
    if [ -f /tmp/bad.txt ]; then
      echo "=== OUTPUT ==="
      cat /tmp/bad.txt
      echo "=============="
    fi
    exit 1
  fi
done
