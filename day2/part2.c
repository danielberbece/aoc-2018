#include <stdio.h>
#include <string.h>

char ids[300][200];

int cmp_str(int current) {
	int i,j;
	int difference;

	for(i = 0; i < current; i++) {
		j = 0;
		difference = 0;
		while(ids[current][j] != 0) {
			if(ids[current][j] != ids[i][j]) difference++;
			j++;
		}

		if(difference == 1) return i;
	}

	return -1;
}

void remove_common_letter(int i1, int i2) {
	int i = 0, j = 0;
	while(ids[i1][i] != 0) {
		if(ids[i1][i] == ids[i2][i]){
			ids[299][j] = ids[i1][i];
			j++;
		}
		i++;
	}
}


int main() {
	// FILE* inf = fopen("test.in", "r");
	FILE* inf = fopen("input.txt", "r");
	
	int index = 0;
	int ret;
	while(fscanf(inf, "%s", ids[index]) == 1) {
		ret = cmp_str(index);
		if(ret != -1) break;
		index++;
	}

	fclose(inf);

	remove_common_letter(index, ret);

	printf("%s and %s\ncommon: %s", ids[index], ids[ret], ids[299]);

	return 0;
}
