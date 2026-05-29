# PR114-2-45: Question 45: The Bank Withdrawal Guard

## 題目敘述
銀行帳戶目前餘額為 balance，現在要提款 amount。若 amount 小於 0，請拋出 invalid_argument，訊息固定為 "invalid amount"。若 amount 大於 balance，請拋出 runtime_error，訊息固定為 "insufficient funds"。若提款成功，輸出剩餘餘額。主程式必須接住標準例外並輸出 what()。
A bank account currently has balance dollars, and you want to withdraw amount dollars. If amount is negative, throw invalid_argument with the fixed message "invalid amount". If amount is greater than balance, throw runtime_error with the fixed message "insufficient funds". If the withdrawal succeeds, output the remaining balance. The main program must catch standard exceptions and output what().

## 輸入說明
輸入兩個整數 balance 與 amount。
The input contains two integers, balance and amount.

## 輸出說明
若成功提款，輸出剩餘餘額；否則輸出對應的錯誤訊息。
If the withdrawal succeeds, output the remaining balance; otherwise output the corresponding error message.

---

## 範例測試
### 範例輸入 1
```text
100 30
```
### 範例輸出 1
```text
70
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    try
    {
        if (m < 0)
        {
            throw invalid_argument("invalid amount");
        }
        else if (m > n)
        {
            throw runtime_error("insufficient funds");
        }
        else
        {
            cout << n - m << endl;
        }
    }
    catch (invalid_argument &e)
    {
        cout << e.what() << endl;
    }
    catch (runtime_error &e)
    {
        cout << e.what() << endl;
    }
    return 0;
}
```
