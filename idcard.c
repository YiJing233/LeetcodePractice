#include<stdio.h>

int fun(int a,int b,char *p)
{
int i,n=0;
for(i=a;i<=b;i++)	{n=n*10+*(p+i)-48; //将输入的数字字符专为10进制数字，跟ascii码有关
printf("%d\n",n);
}//
return n;
}

int main()
{
char a[100];//数组可以设大一点
char *p;//指针声明
p=a;//指针指向字符串a

int year;//变量声明，三个数字好输出
int month;
int day;

printf("please input your id card number:");
scanf("%s",p);

year=fun(6,9,p);
month=fun(10,11,p);
day=fun(12,13,p);

printf("%d/%d/%d\n",year,month,day);
return 0;
}
