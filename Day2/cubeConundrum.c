#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int red_count = 12;
    int green_count = 13;
    int blue_count = 14;

    for (int i = 1; i < argc; i++) {
        char count[10];
        char color[10];

        if (i < argc - 1) {
            strcpy(count, argv[i]);
            strcpy(color, argv[i + 1]);
            i++;

            if (strcmp(color, "red,") == 0) {
                red_count -= atoi(count);
            } else if (strcmp(color, "blue,") == 0) {
                blue_count -= atoi(count);
            } else if (strcmp(color, "green,") == 0) {
                green_count -= atoi(count);
            }
        }
    }

    if (red_count < 0 || blue_count < 0 || green_count < 0) {
        printf("This game is not possible\n");
    } else {
        printf("This game is possible\n");
    }

    return 0;
}