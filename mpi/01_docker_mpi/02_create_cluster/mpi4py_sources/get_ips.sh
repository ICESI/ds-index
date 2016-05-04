#!/bin/bash
for ip in 172.17.0.{1..254}; do
  ping -c 1 -W 1 $ip | grep "64 bytes" | awk '{print $4}' | sed 's/://' &
done
