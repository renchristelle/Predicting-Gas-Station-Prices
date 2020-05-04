#!/bin/sh
# This is a comment!

GIT_AUTHOR_DATE='Fri Jul 26 19:32:10 2013 -0400'
GIT_COMMITTER_DATE='Fri Jul 26 19:32:10 2013 -0400'

for i in {1..3}
do
  myvar=$(( (RANDOM % 50) + 1 ))
  for y in $(eval echo "{1..$myvar}")
  do
    #echo $i$y > git.txt
    cp random_dataset.json random_from_git_.json
    git add random_from_git.json
    git commit --date="100 day ago" --author="User$i <user$i>" -m "whatever"
    rm -rf random_from_git_.json
  done
done
