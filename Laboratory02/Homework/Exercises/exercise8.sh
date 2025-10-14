#!/bin/bash
curl -s http://checkip.dyndns.org/ | cut -d ':' -f 2 | cut -d '<' -f 1
