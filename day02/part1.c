#include <stdio.h>

int scan_str(char str[], int n) {
	int i,dict[300];
	for(i = 0; i < 300; i++) {
		dict[i] = 0;
	}

	for(i = 0; str[i] != 0; i++) {
		dict[str[i]]++;
	}

	for(i = 0; i < 300; i++) {
		if(dict[i] == n) return 1;
	}

	return 0;
}

int main() {
	// FILE* inf = fopen("test.in", "r");
	FILE* inf = fopen("input.txt", "r");
	char string[200];
	unsigned int doubles = 0;
	unsigned int triples = 0;
	int verf;
	while(fscanf(inf, "%s", string) == 1) {
		triples += scan_str(string, 3);
		doubles += scan_str(string, 2);
		// printf("Doubles: %d\nTriples: %d\n", doubles, triples);
	}

	fclose(inf);

	printf("%d\n", doubles * triples);

	return 0;
}
