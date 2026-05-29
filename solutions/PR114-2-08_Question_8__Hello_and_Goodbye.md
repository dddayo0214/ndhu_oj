# PR114-2-08: Question 8: Hello and Goodbye

## 題目敘述
請設計一個**Greeter**類別。建構子輸出**Construct name**，成員函式輸出**Hello, name**，解構子輸出**Destruct name**。
程式中只建立一個物件。這一題要觀察物件建立與離開時的輸出順序。
Design a**Greeter**class. The constructor prints**Construct name**, a member function prints**Hello, name**, and the destructor prints**Destruct name**.
Create only one object in the program. This problem is for observing the output order when an object is created and destroyed.

## 輸入說明
輸入一行，包含一個不含空白的字串**name**。
The input contains one line with one string**name**without spaces.

## 輸出說明
請依照題意輸出三行。
Output exactly three lines as described in the statement.

---

## 範例測試
### 範例輸入 1
```text
Amy
```
### 範例輸出 1
```text
Construct Amy
Hello, Amy
Destruct Amy
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
    void PrintGreeting()
    {
        cout << "Hello, " << name << endl;
    }
    ~Greeter()
    {
        cout << "Destruct " << name << endl;
    }
};

int main()
{
    string name;
    cin >> name;
    Greeter g(name);
    g.PrintGreeting();
    return 0;
}
```
