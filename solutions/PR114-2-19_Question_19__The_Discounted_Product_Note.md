# PR114-2-19: Question 19: The Discounted Product Note

## 題目敘述
請建立一個基底類別與一個衍生類別，並由衍生類別物件整合輸入資料與額外資訊後輸出。衍生類別應在保留基底類別資料的基礎上加入新欄位。
本題重點是確認你是否理解基礎繼承的寫法與用途。
Create a base class and a derived class, then use a derived-class object to combine the input data with extra information and output the result. The derived class should keep the base-class data and add a new field.
The main purpose is to check whether you understand the syntax and usage of basic inheritance.

## 輸入說明
輸入一行，包含一個不含空白的字串 name 與一個整數 times。
The input contains one line with a string name and an integer times.

## 輸出說明
第一行輸出 Name: name。第二行輸出重複的 Woof。
Output Name: name on the first line. Output the repeated Woof on the second line.

---

## 範例測試
### 範例輸入 1
```text
Coco 3
```
### 範例輸出 1
```text
Name: Coco
Woof Woof Woof
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class AnimalName
{
protected:
    string name;

public:
    AnimalName(string name) : name(name)
    {
        cout << "Name: " << name << endl;
    }
};

class AnimalWoof : public AnimalName
{
public:
    AnimalWoof(string name, int times) : AnimalName(name)
    {
        for (int i = 0; i < times; i++)
        {
            cout << "Woof ";
        }
    }
};

int main()
{
    string name;
    int times;
    cin >> name >> times;
    AnimalWoof animal(name, times);
    return 0;
}
```
