#include <stdio.h>
void main()
{
    int i,j,a,b,n;
    printf("enter the number of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        a=65;
        for(j=1;j<=i;j++){
            printf("%c ",a);
            a++;
        }
        printf("\n");
    }
}