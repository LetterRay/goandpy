#include <stdio.h>

int main()
{
    int  secret = 0;
    printf("please enter the secret num:");
    scanf("%d",&secret);
    if(secret !=123)
    {
        printf("incorrect secret num.\n");
	return 0;
    }    
    printf("hello world!\n");
    return 0;
}
