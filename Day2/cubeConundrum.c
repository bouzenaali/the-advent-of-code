#include <stdlib.h>
#include <stdio.h>
#include <string.h>


#define  RED_COUNT = 12;
#define  GREEN_COUNT = 13;
#define  BLUE_COUNT = 14;


int main(int argc, char *argv[]) {


    for (int i = 1; i < argc; i++) {
        char count[10];
        char color[10];

        if (i < argc - 1) {
            strcpy(count, argv[i]);
            strcpy(color, argv[i + 1]);
            i++;

            if (strcmp(color, "red,") == 0) {
                RED_COUNT -= atoi(count);
            } else if (strcmp(color, "blue,") == 0) {
                BLUE_COUNT -= atoi(count);
            } else if (strcmp(color, "green,") == 0) {
                GREEN_COUNT -= atoi(count);
            }
        }
    }

    if (RED_COUNT < 0 || BLUE_COUNT < 0 || GREEN_COUNT < 0) {
        printf("This game is not possible\n");
    } else {
        printf("This game is possible\n");
    }

    return 0;
}