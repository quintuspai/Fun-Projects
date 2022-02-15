#!/bin/bash
source /Users/quintus.pai/Desktop/myproject/myscript.conf
pass=✅
fail=❌
for((i=$start;i<=$end;i++))
do
src=$ip$i
cmd=$(ping -c1 $src &> /dev/null && echo "$src : $pass" || echo "$src : $fail")
echo $cmd
done
