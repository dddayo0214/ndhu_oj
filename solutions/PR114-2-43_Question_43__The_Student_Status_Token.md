# PR114-2-43: Question 43: The Student Status Token

## 題目敘述
請設計一個簡單的類別 StatusToken，其中至少包含一個字串訊息。若輸入代碼為 0，表示正常，直接輸出 OK；若代碼不是 0，請建立一個 StatusToken 物件並將它拋出。主程式必須接住這個物件，並輸出其中的訊息。代碼與訊息的對應如下：1 對應 ABSENT，2 對應 LATE，3 對應 CHEATING，其他非零值一律視為 UNKNOWN。
Design a simple class named StatusToken that contains at least one string message. If the input code is 0, it means normal and you should output OK directly. If the code is not 0, create a StatusToken object and throw it. The main program must catch this object and output its message. The mapping is: 1 -> ABSENT, 2 -> LATE, 3 -> CHEATING, and any other nonzero value -> UNKNOWN.

## 輸入說明
輸入一個整數 code。
The input contains one integer code.

## 輸出說明
若 code 為 0，輸出 OK；否則輸出對應的狀態訊息。
If code is 0, output OK; otherwise output the corresponding status message.

---

## 範例測試
### 範例輸入 1
```text
0
```
### 範例輸出 1
```text
OK
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

class StatusToken
{
public:
    string msg;
    StatusToken(string m) : msg(m) {}
};

int main()
{
    string n;
    cin >> n;
    StatusToken st(n);
    try
    {
        if (n == "0")
        {
            cout << "OK" << endl;
        }
        else
        {
            throw StatusToken(n);
        }
    }
    catch (StatusToken &e)
    {
        if (e.msg == "1")
        {
            cout << "ABSENT" << endl;
        }
        else if (e.msg == "2")
        {
            cout << "LATE" << endl;
        }
        else if (e.msg == "3")
        {
            cout << "CHEATING" << endl;
        }
        else
        {
            cout << "UNKNOWN" << endl;
        }
    }
    return 0;
}
```
