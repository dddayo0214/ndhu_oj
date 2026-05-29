# PR114-2-50: Question 50: The Real Type Checker

## 題目敘述
In this problem, you will practice safe downcasting with dynamic_cast. A school system stores different people through base-class pointers. Every object is stored as a Person pointer, but the real object may be either a Student or a Teacher.
You must design a polymorphic base class Person and at least two derived classes: Student and Teacher. Because the program needs to identify the real runtime type of each object, the base class must be polymorphic, which means it should contain at least one virtual function.
After creating all objects, your program must examine each Person pointer and use dynamic_cast to determine whether it actually points to a Student object or a Teacher object. Then print the corresponding information in the original input order.
The purpose of this problem is to show why dynamic_cast is useful. Unlike static_cast, dynamic_cast performs a runtime type check. When a cast to a pointer type fails, it returns nullptr.
本題要你練習使用 dynamic_cast 進行安全的 downcasting。學校系統會用基底類別指標來儲存不同人物。雖然所有物件都先以 Person 指標形式保存，但它們的真實型別可能是 Student，也可能是 Teacher。
你必須設計一個具多型性的基底類別 Person，以及至少兩個衍生類別 Student 與 Teacher。由於程式需要辨識每個物件在執行期的真實型別，因此基底類別必須是 polymorphic，也就是至少要有一個 virtual function。
建立所有物件之後，你的程式必須逐一檢查每個 Person 指標，並使用 dynamic_cast 判斷它實際上是否指向 Student 或 Teacher 物件，再依輸入順序輸出對應資訊。
這題的目的，是讓你觀察 dynamic_cast 的用途。和 static_cast 不同，dynamic_cast 會在執行期檢查實際型別。當轉型成指標型別失敗時，它會回傳 nullptr。

## 輸入說明
The first line contains an integer n, the number of people.
Each of the next n lines begins with a type code.
If the type code is S, the line format is: S name score
If the type code is T, the line format is: T name years
第一行輸入一個整數 n，表示人物數量。
接下來 n 行，每行先輸入一個型別代號。
若型別代號為 S，格式為：S name score
若型別代號為 T，格式為：T name years

## 輸出說明
For each person, print one line in one of the following formats:
Student name score
Teacher name years
After that, print two more lines:
Students: X
Teachers: Y
對於每個人物，請輸出一行，格式如下之一：
Student name score
Teacher name years
接著再輸出兩行：
Students: X
Teachers: Y

---

## 範例測試
### 範例輸入 1
```text
3
S Alice 90
T Bob 12
S Carol 85

```
### 範例輸出 1
```text
Student Alice 90
Teacher Bob 12
Student Carol 85
Students: 2
Teachers: 1

```

### 範例輸入 2
```text
2
T Henry 20
T Iris 8

```
### 範例輸出 2
```text
Teacher Henry 20
Teacher Iris 8
Students: 0
Teachers: 2

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Person
{
public:
    string name;
    Person(string n) : name(n) {}
    char virtual getType() = 0;
};

class Student : public Person
{
public:
    int score;
    Student(string n, int s) : Person(n), score(s) {}
    char getType() override
    {
        return 'S';
    }
};

class Teacher : public Person
{
public:
    int year;
    Teacher(string n, int y) : Person(n), year(y) {}
    char getType() override
    {
        return 'T';
    }
};

int main()
{
    int n;
    cin >> n;
    vector<Person *> v(n);
    for (int i = 0; i < n; i++)
    {
        char type;
        cin >> type;
        if (type == 'S')
        {
            string name;
            int score;
            cin >> name >> score;
            v[i] = new Student(name, score);
        }
        else
        {
            string name;
            int year;
            cin >> name >> year;
            v[i] = new Teacher(name, year);
        }
    }
    int sCount = 0, tCount = 0;
    for (auto &i : v)
    {
        if (dynamic_cast<Student *>(i) != nullptr)
        {
            cout << "Student " << i->name << " " << dynamic_cast<Student *>(i)->score << endl;
            sCount++;
        }
        else
        {
            cout << "Teacher " << i->name << " " << dynamic_cast<Teacher *>(i)->year << endl;
            tCount++;
        }
    }
    cout << "Students: " << sCount << endl;
    cout << "Teachers: " << tCount << endl;
}
```
