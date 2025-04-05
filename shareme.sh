#!/bin/bash
#
git add .
read varname
git commit -m "$varname:shared a file"
git push

