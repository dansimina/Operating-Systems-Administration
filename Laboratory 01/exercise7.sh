#!/bin/bash

echo -e "Executable files which starts with pass:\n$(find pass* -maxdepth 0 -executable 2> /dev/null)"
