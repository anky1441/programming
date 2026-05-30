  #include<stdio.h>
int main ()
{
    int n;
    printf("enter the number");
    scanf("%d",&n);
    int num=2*n-1;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=num;j++){
            printf("%d",j);
        }
        num=num-2;
        printf("\n");
    }
}