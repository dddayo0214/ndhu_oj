# PR114-2-15: Question 15: The Wallet Bonus Rule

## 題目敘述
請建立一個類別來保存錢包金額資料，並建立物件依規則更新數值。修正錢包內容的規則為「保留較大的金額」 。
你必須使用 reference 參數設計成員函式，讓資料可以在函式中被修改，最後輸出結果。
請用物件導向方式完成本題，並將資料與操作封裝在類別中。
Create a class to store wallet amounts, and create an object to update the values according to the rule. The rule is keep the greater value between current balance and given value.
You must design a member function with reference parameters so the data can be modified inside the function, then output the result.
Solve this problem in an object-oriented way and keep the data and operations inside the class.

## 輸入說明
輸入一行，包含兩個整數 a b。
The input contains one line with two integers a b.

## 輸出說明
輸出最後的 a 值。
Output the final value of a.

---

## 範例測試
### 範例輸入 1
```text
3 8
```
### 範例輸出 1
```text
8
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Obj
{
private:
    int money;

public:
    Obj(int m) : money(m) {}
    int getMax(int &b) { return max(money, b); }
};

int main()
{
    int a, b;
    cin >> a >> b;
    Obj obj(a);
    cout << obj.getMax(b) << endl;
    return 0;
}
```
