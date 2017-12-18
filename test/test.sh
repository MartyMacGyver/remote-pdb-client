#!/usr/bin/env bash

while [ 1 ]
do
  ./test_server.py '0.0.0.0' 4244
  sleep 1
done
