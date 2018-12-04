#include <stdio.h>

int main() {

	int acumulator = 0;
	FILE *inf = fopen("input1.txt", "r");
	int elem;

	while(fscanf(inf, "%d", &elem) == 1) {
		acumulator += elem;
	}
	
	printf("%d\n", acumulator);

	fclose(inf);
	return 0;
}
