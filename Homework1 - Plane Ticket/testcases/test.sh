# Made by Canarypwn with Love ( Find me on: github.com/nyovelt )

echo "你的python运行命令是 python 还是 python3 呢（请输入1或者3）"
read python_alias
echo "你写到第几个task啦？(请输入task后面的 整数 )"
read task
echo "这个task一共有几组输入样例呢? (请输入整数)"
read num
echo "请把task.py放到同目录 (按任意键确定哦)"
read 

if [ $python_alias == 1 ]
then 
        for ((i=1;   i<=${num};  i=i+1))
        do
				echo "Working on tmp/${task}_${i}.out "
                timeout 3 python task${task}.py  < ${task}_${i}.in > tmp/${task}_${i}.out
				#echo "python task${task}.py  < ${task}_${i}.in > tmp/${task}_${i}.out"
		done
elif [ $python_alias == 3 ]
then 
        for ((i=1;   i<=${num};  i=i+1))
        do
                echo  "python3 task${task}.py  < ${task}_${i}.in > tmp/${task}_${i}.out"
                echo "Working on tmp/${task}_${i}.out "
				timeout 3 python3 task${task}.py  < ${task}_${i}.in > tmp/${task}_${i}.out
        done
else
        echo "不明白你的python命令呢"
        exit
fi 

read -r -p "文件夹中有包含正确输出吗? (y/n) " input
case $input in
    [yY][eE][sS]|[yY])
		echo "judging"
                for ((i=1;   i<=${num};  i=i+1))
                do
                        echo "diff ${task}_${i}.out  tmp/${task}_${i}.out"
                        diff ${task}_${i}.out  tmp/${task}_${i}.out
                done
	;;

    [nN][oO]|[nN])
		echo "No"
       	;;

    *)
		echo "Invalid input..."
		exit 1
		;;
esac


echo "大功告成了喵w"