/*#include <stdio.h>
void main()
{
    int n,i,a,b,sum=1;
    printf("enter the number");
    scanf("%d",&n);
    a=1,b=1;
    for(i=1;i<=n-2;i++){
        sum=a+b;
        a=b;
        b=sum;
    }
    printf("the %dth term of fibonacci series is:%d",n,sum);
}*/
//n terms fibonacci series
#include <stdio.h>
void main()
{
    int a=0,b=1,i,n,sum=1;
    printf("enter the number");
    scanf("%d",&n);
    printf("the fibonacci series is:");
    for(i=1;i<=n;i++){
    printf("%d ",a);
        sum=a+b;
        a=b;
        b=sum;
        
    }
}