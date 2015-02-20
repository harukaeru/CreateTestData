# 拡張子
ext=jpg

# もし引数が１個じゃなかったらメロスする
if (test $# -eq 1) ; then
	for i in `seq 1 $1`
	do
		num=`printf %06d $i`
		mv $i.$ext File_$num.$ext
	done
else
	echo "使い方がおかしいです！"
fi
