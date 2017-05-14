#!/bin/bash

for spec in `ls -1 */*.spec | grep -v minishift.spec`; do
  d=$(dirname $spec)
  source0=$(spectool --list-files $spec | awk '{print $2}' | head -n1)
  sourcebase=$(basename "$source0")
  [ ! -h $d/$sourcebase ] || continue
  git annex whereis "$d/$sourcebase" 2&> /dev/null | grep -q " web" && continue
  git annex --verbose addurl --file "$d/$sourcebase" "$source0"
done
