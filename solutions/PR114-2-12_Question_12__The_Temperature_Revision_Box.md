# PR114-2-12: Question 12: The Temperature Revision Box

## 題目敘述
請建立一個類別來保存溫度資料，並建立物件完成輸入與更新。你必須使用 reference 參數讓成員函式能直接修改物件中的數值，最後輸出更新結果。
請用類別、物件與 reference 的觀念完成本題。
Create a class to store temperature data, and create an object to handle input and update. You must use a member function with reference parameters so the value inside the object can be modified directly, then output the updated result.
Use the ideas of class, object, and reference to solve this problem.

## 輸入說明
輸入一行，包含兩個整數 x k。
The input contains one line with two integers x k.

## 輸出說明
輸出增加後的整數結果。
Output the updated integer.

---

## 範例測試
### 範例輸入 1
```text
13 5
```
### 範例輸出 1
```text
18
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Obj
{
private:
    int x;

public:
    Obj(int a) : x(a) {}
    int &getX() { return x; }
    void AddX(int &a) { x += a; }
};

int main()
{
    int x, k;
    cin >> x >> k;
    Obj obj(x);
    obj.AddX(k);
    cout << obj.getX() << endl;
    return 0;
}
```
