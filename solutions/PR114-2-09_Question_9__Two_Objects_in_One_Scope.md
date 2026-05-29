# PR114-2-09: Question 9: Two Objects in One Scope

## 題目敘述
請建立兩個同類型物件，名稱依輸入給定。每個物件在建構時輸出**Construct name**，在解構時輸出**Destruct name**。
在兩個物件都建立完成後，額外輸出一行**Working**。請注意解構順序。
Create two objects of the same type with names given in the input. Each object prints**Construct name**in its constructor and**Destruct name**in its destructor.
After both objects are created, print one extra line**Working**. Pay attention to the destruction order.

## 輸入說明
輸入一行，包含兩個不含空白的字串**a b**。
The input contains one line with two strings**a b**without spaces.

## 輸出說明
請輸出五行，順序必須正確。
Output exactly five lines in the correct order.

---

## 範例測試
### 範例輸入 1
```text
Tom Jerry
```
### 範例輸出 1
```text
Construct Tom
Construct Jerry
Working
Destruct Jerry
Destruct Tom
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
    Greeter g1(name1);
    Greeter g2(name2);
    cout << "Working" << endl;
    return 0;
}
```
