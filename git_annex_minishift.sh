#!/bin/bash

for spec in minishift/*.spec; do
  d=$(dirname $spec)
  # spectool fails with an include present in the spec file
  rm -f $spec.tmp && cat $spec | sed '/^%include/d' > $spec.tmp
  source0=$(spectool --list-files $spec.tmp | awk '{print $2}' | head -n1 && rm -f $spec.tmp)
  sourcebase=$(basename "$source0")
  [ ! -h $d/$sourcebase ] || continue
  git annex whereis "$d/$sourcebase" 2&> /dev/null | grep -q " web" && continue
  git annex --verbose addurl --file "$d/$sourcebase" "$source0"
done

IFS_SAVE=$IFS
IFS=$'\n'
for spec in minishift/*.inc; do
  d=$(dirname $spec)
  for source in `grep wget $spec`; do
      source0=`echo $source | cut -d' ' -f4`
      sourcebase=`echo $source | cut -d' ' -f6`
      if [ "$sourcebase" = "" ]; then
          sourcebase=$(basename "$source0")  # probably a git hash source
      fi
      [ ! -h $d/$sourcebase ] || continue
      git annex whereis "$d/$sourcebase" 2&> /dev/null | grep -q " web" && continue
      git annex --verbose addurl --file "$d/$sourcebase" "$source0"
  done
done
IFS=$IFS_SAVE
