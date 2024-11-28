#include <stdio.h>

int main()
{
    int tot, n, max, i;
    
    printf("Insert total number of iteration: ");
    scanf("%d", &tot);
    
    max = 0;
    
    for (i=1; i<=tot; i++)
    {
        printf("Insert number: ");
        scanf("%d", &n);
        if (n >= max)
        {
           max = n ;
        }
        
    }
    
    printf("The max value is: %d", max);
    return 0;
}