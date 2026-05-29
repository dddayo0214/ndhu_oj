# PR114-2-27: Question 27: The Library Borrowing Counter

## 題目敘述
某大學圖書館有許多書，也有許多學生會到櫃檯辦理借書與還書。你需要用程式描述這個場景中的互動。
Book 代表一本書，至少應包含書名與目前是否被借出的狀態。 Student 代表一位學生，至少應包含學生姓名與目前借了幾本書。 Library 代表整個圖書館，負責管理館藏、處理借書與還書操作，以及查詢目前狀態。
操作規則如下。如果某本書尚未被借出，且學生目前借書數未達上限 3 本，則 BORROW 會成功。若書已被借出，輸出該書 unavailable。若學生已借滿 3 本，輸出該學生 limit reached。RETURN 只有在該學生真的借了該書時才成功，否則輸出 cannot return。
你必須使用物件導向方式作答，並以類別及成員函式來描述 Book、Student 與 Library 的合作。不得只用單純陣列或一般函式拼湊邏輯。
In a university library, many books are available and many students visit the counter to borrow and return books. You need to describe the interaction in this scene using a program.
A Book represents one book and should at least contain a title and whether it is currently borrowed. A Student represents one student and should at least contain a name and the number of books currently borrowed. A Library represents the whole library and manages the collection, handles borrow and return operations, and reports the current status.
The rules are as follows. A BORROW operation succeeds only if the book is not currently borrowed and the student has borrowed fewer than 3 books. If the book is already borrowed, output that the book is unavailable. If the student already has 3 books, output that the student's limit has been reached. A RETURN operation succeeds only if the student really borrowed that book; otherwise output cannot return.
You must solve this problem using object-oriented programming and use classes and member functions to describe the collaboration among Book, Student, and Library. Do not piece the logic together using only plain arrays and ordinary functions.
1 ≤ B ≤ 100，1 ≤ Q ≤ 200。每位學生最多可借 3 本書。
1 ≤ B ≤ 100, 1 ≤ Q ≤ 200. Each student may borrow at most 3 books.

## 輸入說明
第一行輸入兩個整數 B 與 Q，分別代表一開始館藏書本數量與操作次數。
接著輸入 B 行，每行一個書名。
再接著 Q 行操作，格式為 BORROW student book、RETURN student book 或 STATUS。
書名與學生姓名皆只包含英文字母與數字，且不含空白。
The first line contains two integers B and Q, the number of books initially in the library and the number of operations.
The next B lines each contain one book title.
The next Q lines are operations in one of the following forms: BORROW student book, RETURN student book, or STATUS.
Both book titles and student names contain only letters and digits and do not contain spaces.

## 輸出說明
對每個操作輸出一行。
BORROW 成功輸出「student borrowed book」，書已借出則輸出「book unavailable」，若學生已借滿 3 本則輸出「student limit reached」。
RETURN 成功輸出「student returned book」，否則輸出「student cannot return book」。
STATUS 輸出「Available: X, Borrowed: Y」。
Output one line for each operation.
If BORROW succeeds, output "student borrowed book". If the book is already borrowed, output "book unavailable". If the student already has 3 books, output "student limit reached".
If RETURN succeeds, output "student returned book". Otherwise output "student cannot return book".
For STATUS, output "Available: X, Borrowed: Y".

---

## 範例測試
### 範例輸入 1
```text
3 8
DB
AI
Math
STATUS
BORROW Tom DB
BORROW Tom AI
STATUS
RETURN Tom DB
BORROW Ann DB
STATUS
```
### 範例輸出 1
```text
Available: 3, Borrowed: 0
Tom borrowed DB
Tom borrowed AI
Available: 1, Borrowed: 2
Tom returned DB
Ann borrowed DB
Available: 1, Borrowed: 2
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class Book
{
private:
    string name;
    string owner;

public:
    Book(string Name) : name(Name), owner("") {}
    string getName()
    {
        return name;
    }
    string &getOwner()
    {
        return owner;
    }
};

class Student
{
private:
    string name;
    int bookCount = 0;

public:
    Student(string Name) : name(Name) {}
    string getName()
    {
        return name;
    }
    void addBook()
    {
        bookCount++;
    }
    void removeBook()
    {
        bookCount--;
    }
    int getBookCount()
    {
        return bookCount;
    }
};

class Library
{
private:
    Student *students[200];
    Book *books[200];
    int studentCount = 0;
    int bookCount = 0;
    int borrowedCount = 0;

public:
    void display()
    {
        cout << "Available: " << bookCount - borrowedCount << ", Borrowed: " << borrowedCount << endl;
    }
    void addBook(string name)
    {
        books[bookCount] = new Book(name);
        bookCount++;
    }
    void borrowBook(string name, string book)
    {
        for (int i = 0; i < bookCount; i++)
        {
            if (books[i]->getName() == book)
            {
                if (books[i]->getOwner() != "")
                {
                    cout << book << " unavailable" << endl;
                    return;
                }
                for (int j = 0; j < studentCount; j++)
                {
                    if (students[j]->getName() == name)
                    {
                        if (students[j]->getBookCount() >= 3)
                        {
                            cout << name << " limit reached" << endl;
                            return;
                        }
                        students[j]->addBook();
                        books[i]->getOwner() = name;
                        borrowedCount++;
                        cout << name << " borrowed " << book << endl;
                        return;
                    }
                }
            }
        }
    }
    void returnBook(string name, string book)
    {
        for (int i = 0; i < bookCount; i++)
        {
            if (books[i]->getName() == book)
            {
                if (books[i]->getOwner() != name)
                {
                    cout << name << " cannot return " << book << endl;
                    return;
                }
                for (int j = 0; j < studentCount; j++)
                {
                    if (students[j]->getName() == name)
                    {
                        students[j]->removeBook();
                        books[i]->getOwner() = "";
                        borrowedCount--;
                        cout << name << " returned " << book << endl;
                    }
                }
            }
        }
    }
    void insertStudent(string name)
    {
        students[studentCount] = new Student(name);
        studentCount++;
    }
    bool isInLib(string name)
    {
        for (int i = 0; i < studentCount; i++)
        {
            if (students[i]->getName() == name)
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    int B, Q;
    string input;
    Library lib;
    cin >> B >> Q;
    while (B--)
    {
        string name;
        cin >> name;
        lib.addBook(name);
    }
    while (Q--)
    {
        string input;
        cin >> input;
        if (input == "STATUS")
        {
            lib.display();
        }
        else if (input == "BORROW")
        {
            string name, book;
            cin >> name >> book;
            if (!lib.isInLib(name))
            {
                lib.insertStudent(name);
            }
            lib.borrowBook(name, book);
        }
        else
        {
            string name, book;
            cin >> name >> book;
            lib.returnBook(name, book);
        }
    }
    return 0;
}
```
