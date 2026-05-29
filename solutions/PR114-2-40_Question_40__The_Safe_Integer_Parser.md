# PR114-2-40: Question 40: The Safe Integer Parser

## 題目敘述
請讀入一個字串 s，並使用 C++ 標準函式庫中的 stoi 將它轉成 int。本題的重點是了解並接住 stoi 可能拋出的標準例外。你必須依照 stoi 的實際行為來處理輸入，而不是自行重新定義轉換規則。stoi 會從字串開頭開始解析整數；只要字串前綴可以形成合法整數，轉換就會成功，並回傳已解析出的整數值。解析會在遇到第一個不屬於整數表示的字元時停止。例如，字串 12x 使用 stoi 轉換時，結果為 12，而不會拋出例外。只有在以下兩種情況下需要接住例外：
1. 字串開頭無法形成合法整數時，stoi 會拋出 invalid_argument。
2. 解析出的數值超出 int 可表示範圍時，stoi 會拋出 out_of_range。

本題要求你使用 try-catch 來接住這些由標準函式庫拋出的例外，並輸出指定結果。
Read a string s and convert it to an int using the C++ standard library function stoi. The purpose of this problem is to understand and catch the standard exceptions that may be thrown by stoi.

You must follow the actual behavior of stoi instead of redefining your own conversion rule. stoi starts parsing from the beginning of the string. As long as the prefix of the string can form a valid integer, the conversion succeeds and the parsed integer value is returned. Parsing stops at the first character that does not belong to the integer representation. For example, converting the string 12x with stoi returns 12 and does not throw an exception.

You only need to catch exceptions in the following two cases:
1. If the beginning of the string cannot form a valid integer, stoi throws invalid_argument.
2. If the parsed value is outside the range of int, stoi throws out_of_range.

You are required to use try-catch to catch these exceptions thrown by the standard library and output the required result.

## 輸入說明
輸入只有一行，包含一個字串 s。
The input contains one line with a string s.

## 輸出說明
若 stoi 成功轉換，輸出轉換後的整數值。若發生 invalid_argument，輸出 invalid_argument。若發生 out_of_range，輸出 out_of_range。
If stoi converts successfully, output the resulting integer value. If invalid_argument occurs, output invalid_argument. If out_of_range occurs, output out_of_range.

---

## 範例測試
### 範例輸入 1
```text
123
```
### 範例輸出 1
```text
123
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    try
    {
        cout << stoi(s) << endl;
    }
    catch (invalid_argument &e)
    {
        cout << "invalid_argument" << endl;
    }
    catch (out_of_range &e)
    {
        cout << "out_of_range" << endl;
    }
    return 0;
}
```
