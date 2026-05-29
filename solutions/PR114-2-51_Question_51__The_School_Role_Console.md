# PR114-2-51: Question 51: The School Role Console

## 題目敘述
In this problem, you will compare the roles of static_cast and dynamic_cast in one scene. A school management system stores different members through a base-class pointer. Each member is either a Student or a Teacher.
Every record contains a floating-point value. For a Student, the value represents an exam score. For a Teacher, the value represents a monthly salary. Your program must identify the real runtime type of each object by using dynamic_cast.
After identifying the real type, you must use static_cast to convert the floating-point value into an integer summary. For a Student, output the truncated integer score. For a Teacher, output the truncated integer salary.
This problem is designed to help you distinguish two different purposes. dynamic_cast is used to safely determine the real type in an inheritance hierarchy at runtime. static_cast is used for an explicit ordinary type conversion whose source and target types are already known.
本題要你在同一個場景中比較 static_cast 與 dynamic_cast 的用途。學校管理系統會以基底類別指標儲存不同成員。每個成員不是 Student，就是 Teacher。
每筆資料都包含一個浮點數值。對 Student 而言，這個值代表考試分數；對 Teacher 而言，這個值代表月薪。你的程式必須使用 dynamic_cast 來辨識每個物件在執行期的真實型別。
在辨識出真實型別後，你還必須使用 static_cast 將該浮點數值轉成整數摘要。若是 Student，就輸出被截去小數部分後的整數分數；若是 Teacher，就輸出被截去小數部分後的整數薪資。
本題的設計重點，是幫助你區分兩種轉型的不同用途。dynamic_cast 用來在繼承架構中安全地判斷執行期的真實型別；static_cast 則用於來源與目標型別已知時的明確一般型別轉換。

## 輸入說明
The first line contains an integer n.
Each of the next n lines is in one of the following formats:
S name score
T name salary
The score or salary is given as a double.
第一行輸入一個整數 n。
接下來 n 行，每行格式如下之一：
S name score
T name salary
其中 score 或 salary 皆為 double。

## 輸出說明
For each record, print one line in one of the following formats:
Student name score X
Teacher name salary Y
where X and Y are the integer values obtained by static_cast.
After all records, print:
Students: A
Teachers: B
對每筆資料輸出一行，格式如下之一：
Student name score X
Teacher name salary Y
其中 X 與 Y 是經過 static_cast 後得到的整數值。
全部輸出完後，再輸出：
Students: A
Teachers: B

---

## 範例測試
### 範例輸入 1
```text
3
S Alice 87.9
T Bob 42000.75
S Carol 60.01

```
### 範例輸出 1
```text
Student Alice score 87
Teacher Bob salary 42000
Student Carol score 60
Students: 2
Teachers: 1

```

### 範例輸入 2
```text
2
T Henry 35000.99
T Iris 28000.10

```
### 範例輸出 2
```text
Teacher Henry salary 35000
Teacher Iris salary 28000
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
    double score;
    Student(string n, double s) : Person(n), score(s) {}
    char getType() override
    {
        return 'S';
    }
};

class Teacher : public Person
{
public:
    double salary;
    Teacher(string n, double s) : Person(n), salary(s) {}
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
            double score;
            cin >> name >> score;
            v[i] = new Student(name, score);
        }
        else
        {
            string name;
            double salary;
            cin >> name >> salary;
            v[i] = new Teacher(name, salary);
        }
    }
    int sCount = 0, tCount = 0;
    for (auto &i : v)
    {
        if (dynamic_cast<Student *>(i) != nullptr)
        {
            cout << "Student " << i->name << " score " << static_cast<int>(static_cast<Student *>(i)->score) << endl;
            sCount++;
        }
        else
        {
            cout << "Teacher " << i->name << " salary " << static_cast<int>(static_cast<Teacher *>(i)->salary) << endl;
            tCount++;
        }
    }
    cout << "Students: " << sCount << endl;
    cout << "Teachers: " << tCount << endl;
}
```
