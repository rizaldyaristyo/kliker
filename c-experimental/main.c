//gcc main.c -lwinmm
#include <windows.h>
#include <mmsystem.h>

char* soundPath1 = "cl.wav";
char* soundPath2 = "ick.wav";

void PlaySoundFile(char* filename) {
    PlaySound(filename, NULL, SND_FILENAME);
}

// Main function
int main() {
    while (1) {
        if (GetAsyncKeyState(VK_LBUTTON)) {
            PlaySoundFile(soundPath1);
        }
        else if (GetAsyncKeyState(VK_RBUTTON)) {
            PlaySoundFile(soundPath2);
        }

        Sleep(1);
    }

    return 0;
}
