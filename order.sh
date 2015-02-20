if (test $# -lt 1) ; then
	echo "何番までソートするか入力してください"
else
	for i in `seq 1 $1`
	do
		num=`printf %06d $i`
		mv $i.jpg File_$num.jpg
	done
fi
