#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int fabric[1001][1001];
int params[5];

void parse_in(char str[]) {
	int index = 1;
	int i;
	int number;
	for(i = 0; i < 5; i++) {
		number = 0;
		while(str[index] >= '0' && str[index] <= '9') {
			number *= 10;
			number += str[index] - '0';
			index ++;
		}
		params[i] = number;
		
		while(str[index] < '0' || str[index] > '9')	index++;
	}	

}

int main() {
	FILE *inf = fopen("in.txt", "r");
	int i, j, id, leftgap, topgap, width, height;
	char *in_line = malloc(1000);
	size_t size = 1000;
	while(getline(&in_line, &size, inf) != -1) {
		parse_in(in_line);
		id = params[0];
		leftgap = params[1];
		topgap = params[2];
		width = params[3];
		height = params[4];
		
		for(i = topgap + 1; i <= topgap + height; i++) {
			for(j = leftgap + 1; j <= leftgap + width; j++) {
				fabric[i][j] += 1;
			}
		}
	}

	unsigned int common_area = 0;
	for(i = 1; i < 1001; i++) {
		for(j = 1; j < 1001; j++) {
			if(fabric[i][j] > 1) {
				common_area ++;
			}
		}
	}

	printf("%d\n", common_area);
	free(in_line);
	return 0;
}