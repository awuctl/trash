#include <stdio.h>
#include <stdbool.h>

#include <errno.h>
#include <unistd.h>

#include <X11/Xlib.h>

int main(int argc, char* argv[]) {

    Display* disp = XOpenDisplay(NULL);

    int err;
    do {
        err = XGrabKeyboard(
            disp,
            XDefaultRootWindow(disp),
            true, /* report keyboard events */
            GrabModeAsync,
            GrabModeAsync,
            CurrentTime
        );
    } while(err != GrabSuccess);

    XUngrabKeyboard(disp, CurrentTime);
    XCloseDisplay(disp);

    execvp(argv[1], argv + 1);
    return -1;
}
