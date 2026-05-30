#include<stdio.h>
int main ()
{
    int n;
    printf("enter the number");
    scanf("%d",&n);
    int nsp=1;
    int nst=n;
    for(int m=1;m<=2*n+1;m++){
        printf("*");
    }
    printf("\n");
    for (int i=1;i<=n;i++){
        for(int j=1;j<=nst;j++){
            printf("*");
        }
        for(int k=1;k<=nsp;k++){
            printf(" ");
        }
        for(int l=1;l<=nst;l++){
            printf("*");
        }
    printf("\n");
    nsp=nsp+2;
    nst=nst-1;
    }
    return 0;
}