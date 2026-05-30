#include <stdio.h>
void main()
{
    int i,j,a,b,n;
    printf("enter the number of rows");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        if(i%2!=0)
        {
            for(j=1;j<=i;j++){
            printf("%d ",j);
            }
        }
        else {
        b=65;
        for(j=1;j<=i;j++){
        printf("%c ",b);
        b++;
        }
    }
        printf("\n");

    }
}
