#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int calcCalibration(char string[150]) {
    char res1 = '0';
    char res2 = '0';

    for (int i = 0; i < strlen(string); i++) {
        if (isdigit(string[i])) {
            res1 = string[i];
            break;
        }
    }

    for (int i = strlen(string) - 1; i >= 0; i--) {
        if (isdigit(string[i])) {
            res2 = string[i];
            break;
        }
    }

    return atoi(strcat(&res1, &res2));
}

int main() {
    FILE *file;
    file = fopen("Day1/input.txt", "r");
    char line[150];
    if (file == NULL) {
        perror("Unable to open file.\n");
        return 1;
    }

    int caliber, i = 1, calibers = 0;

    while (fgets(line, sizeof(line), file) != NULL) {
        caliber = calcCalibration(line);
        printf("the caliber of line %d is %d\n", i, caliber);
        calibers += caliber;
        i++;
    }

    printf("the sum of the calibrations is: %d\n", calibers);

    fclose(file);

    return 0;
}
