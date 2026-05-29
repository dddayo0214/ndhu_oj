# PR114-2-17: Question 17: The Bus Capacity Report

## 題目敘述
請設計一個基底類別與一個衍生類別，使用衍生類別物件處理資料並輸出結果。衍生類別必須繼承基底類別中的部分資料，再加入自己的欄位。
請以物件導向方式完成本題，不要只用獨立變數模擬。
Design a base class and a derived class. Use a derived-class object to process the input and output the result. The derived class must inherit part of the data from the base class and then add its own field.
Complete this problem in an object-oriented way instead of simulating everything with standalone variables.

## 輸入說明
輸入一行，包含一個不含空白的字串 name 與一個整數 salary。
The input contains one line with a string name and an integer salary.

## 輸出說明
輸出兩行：
Name: name
Salary: salary
Output exactly two lines:
Name: name
Salary: salary

---

## 範例測試
### 範例輸入 1
```text
Kevin 42000
```
### 範例輸出 1
```text
Name: Kevin
Salary: 42000
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Father
{
protected:
    string salary;

public:
    string &getSalary() { return salary; }
};

class Child : public Father
{
private:
    string name;

public:
    Child(string name) : name(name)
    {
    }
    string &getName() { return name; }
};

int main()
{
    string name, salary;
    cin >> name >> salary;
    Child child(name);
    child.getSalary() = salary;
    cout << "Name: " << child.getName() << endl;
    cout << "Salary: " << child.getSalary() << endl;
    return 0;
}
```
