# PR114-2-44: Question 44: The Score Validator

## 題目敘述
請讀入一個成績 s。若 s 介於 0 到 100 之間，輸出 accepted。若 s 不在此範圍內，請主動拋出 C++ 標準函式庫提供的 invalid_argument 例外物件，錯誤訊息固定為 "invalid score"。主程式必須以標準例外物件的方式接住並輸出 what()。
Read one score s. If s is between 0 and 100 inclusive, output accepted. If s is outside this range, you must actively throw a standard library invalid_argument object with the fixed message "invalid score". The main program must catch the standard exception object and output what().

## 輸入說明
輸入一個整數 s。
The input contains one integer s.

## 輸出說明
若合法，輸出 accepted；否則輸出 invalid score。
If valid, output accepted; otherwise output invalid score.

---

## 範例測試
### 範例輸入 1
```text
80
```
### 範例輸出 1
```text
accepted
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
        if (n >= 0 && n <= 100)
        {
            cout << "accepted" << endl;
        }
        else
        {
            throw invalid_argument("invalid score");
        }
    }
    catch (invalid_argument &e)
    {
        cout << e.what() << endl;
    }
    return 0;
}
```
