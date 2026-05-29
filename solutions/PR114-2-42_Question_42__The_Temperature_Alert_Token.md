# PR114-2-42: Question 42: The Temperature Alert Token

## 題目敘述
有一個溫度監測函式。當輸入溫度介於 0 到 35 之間時，函式正常回傳；否則函式不使用回傳值表示錯誤，而是直接拋出一個字串物件 "temperature alert"。主程式必須接住這個被拋出的字串並輸出它。若沒有例外，輸出 normal。
A temperature-checking function returns normally when the input temperature is between 0 and 35 inclusive. Otherwise, it does not report the problem through a return value. Instead, it throws a string object "temperature alert". The main program must catch the thrown string and output it. If no exception is thrown, output normal.

## 輸入說明
輸入一個整數 t，表示溫度。
The input contains one integer t, the temperature.

## 輸出說明
若溫度在合法範圍內，輸出 normal；否則輸出 temperature alert。
If the temperature is within the valid range, output normal; otherwise output temperature alert.

---

## 範例測試
### 範例輸入 1
```text
25
```
### 範例輸出 1
```text
normal
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    try
    {
        if (n >= 0 && n <= 35)
        {
            cout << "normal" << endl;
        }
        else
        {
            throw string("temperature alert");
        }
    }
    catch (string &e)
    {
        cout << e << endl;
    }
    return 0;
}
```
