#include <stdio.h>

int poz_elems[100000000];
int neg_elems[100000000];

int main() {

	int acumulator = 0;
	int elem;
	int found = 0;

	while(found == 0) {
		FILE *inf = fopen("input1.txt", "r");	
		while(found == 0 && fscanf(inf, "%d", &elem) == 1) {
			acumulator += elem;
			if(acumulator >= 0) {
				if(poz_elems[acumulator] == 0) {
					poz_elems[acumulator] = 1;
				} else {
					found = 1;
				} 
			} else {
				if(neg_elems[acumulator] == 0) {
                                        neg_elems[acumulator] = 1;
                                } else {
                                        found = 1;
                                }
			}		
		}
		fclose(inf);
	}
	printf("%d\n", acumulator);

	return 0;
}
