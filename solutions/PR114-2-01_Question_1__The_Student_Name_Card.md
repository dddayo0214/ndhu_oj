# PR114-2-01: Question 1: The Student Name Card

## 題目敘述
請設計一個簡單的**Student**類別概念來表示學生資料。每位學生有三個屬性：姓名、學號、年齡。
在這一題中，你只需要讀入一位學生的資料，並依照指定格式輸出該學生的名片資訊。
雖然 Online Judge 只會檢查輸出結果，但建議你用 class 來練習「類別」與「物件」的基本概念。
Design a simple**Student**class concept to represent student data. Each student has three attributes: name, student ID, and age.
In this problem, read the data of one student and output the student card in the required format.
The Online Judge only checks the output, but you are encouraged to practice the ideas of**class**and**object**in C++.

## 輸入說明
輸入只有一行，包含三個欄位：**name id age**。
其中**name**為不含空白的字串，**id**為不含空白的字串，**age**為整數。
The input contains one line with three fields:**name id age**.
**name**is a string without spaces,**id**is a string without spaces, and**age**is an integer.

## 輸出說明
請輸出三行：
**Name: name**
**ID: id**
**Age: age**
Output exactly three lines:
**Name: name**
**ID: id**
**Age: age**

---

## 範例測試
### 範例輸入 1
```text
Alice B11223344 19
```
### 範例輸出 1
```text
Name: Alice
ID: B11223344
Age: 19
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

class Student
{
public:
	std::string name;
	std::string id;
	int age;
};

int main()
{
	Student student;
	std::cin >> student.name >> student.id >> student.age;
	std::cout << "Name: " << student.name << "\nID: " << student.id << "\nAge: " << student.age << std::endl;
	return 0;
}
```
