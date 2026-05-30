//sum of series 1-2+3-4+5-6+......upto 'n'
#include <stdio.h>
void main()
{
    int n,sum=0;
    printf("enter the number of elements");
    scanf("%d",&n);
        if(n%2==0){
            sum=sum+(-n/2);
        }
        else
        sum=sum+(-n/2+n);   
    printf("the sum of the digit is %d:",sum);
}