#include<stdio.h>
int fun(char *a)
{
	int d=6;//取第七位身份证上的数 
	while(d<10)//循环输出年份的4个数 
	{
		printf("%c",*(a+d));
		d++;
	}
	printf("/");
	while(d<12)//输出月份 
	{
		printf("%c",*(a+d));
		d++;
	}
	printf("/");
	while(d<14)//输出日子 
	{
		printf("%c",*(a+d));
		d++;
	}
}
int main(void)
{
	int i=0; 
	char card[18];
	while(i<18)//循环扫描所有数字 
	{
		sscanf_s("%c",&card[i]);
		i++;
	}
	fun(card);//传入数组 
	return 0;
}
