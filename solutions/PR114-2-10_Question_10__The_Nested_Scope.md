# PR114-2-10: Question 10: The Nested Scope

## 題目敘述
請設計一個類別，建構子與解構子的輸出格式分別為**Construct name**與**Destruct name**。
程式會先建立一個外層物件，再在內層區塊建立另一個物件，並依序輸出指定文字。你需要觀察內層區塊結束時誰會先被解構。
Design a class whose constructor prints**Construct name**and whose destructor prints**Destruct name**.
The program first creates an outer object, then creates another object inside an inner block, and prints fixed messages. You need to observe which object is destroyed when the inner block ends.

## 輸入說明
輸入一行，包含兩個不含空白的字串**outer inner**。
The input contains one line with two strings**outer inner**without spaces.

## 輸出說明
請依序輸出六行。
Output exactly six lines in order.

---

## 範例測試
### 範例輸入 1
```text
Outer Inner
```
### 範例輸出 1
```text
Construct Outer
Construct Inner
Inside
Destruct Inner
Outside
Destruct Outer
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Greeter
{
private:
    string name;

public:
    Greeter(string n) : name(n)
    {
        cout << "Construct " << name << endl;
    };
    ~Greeter()
    {
        cout << "Destruct " << name << endl;
    }
};

int main()
{
    string name1, name2;
    cin >> name1 >> name2;
    {
        Greeter g1(name1);
        {
            Greeter g2(name2);
            cout << "Inside" << endl;
        }
        cout << "Outside" << endl;
    }
    return 0;
}
```
