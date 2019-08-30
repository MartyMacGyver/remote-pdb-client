#!/usr/bin/env bash
echo "Opens port at localhost 4244 for testing (e.g., 'remotepdb_client --host localhost --port 4244')"
while [ 1 ]
do
  ./test_server.py '0.0.0.0' 4244
  echo Session ended with $?
  sleep 1
done
