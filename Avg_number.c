#include <stdio.h>

int main()

{
	int i,tot, num, sum;
	float avg;

	sum = 0;
	printf("Insert total number: ");
	scanf("%d", &tot);

	for (i = 1; i <= tot; i++)
	{
		printf("Insert number: ");
		scanf("%d", &num);
		sum = sum + num;
	}

	avg = (float) sum/tot;
	printf("%f", avg);

	return 0;

}
