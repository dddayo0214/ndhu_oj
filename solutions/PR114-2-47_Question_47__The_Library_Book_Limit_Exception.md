# PR114-2-47: Question 47: The Library Book Limit Exception

## 題目敘述
某位學生目前已借 current 本書，系統規定最多可借 limit 本，現在還想再借 request 本。若 current + request 不超過 limit，輸出借書後的總本數。否則，你必須定義一個繼承 std::exception 的自訂例外類別 BookLimitExceededException，並讓 what() 固定回傳 "Book borrowing limit exceeded"。主程式必須接住此例外並輸出 what()。
A student has currently borrowed current books. The system allows at most limit books, and the student wants to borrow request more books. If current + request does not exceed limit, output the total number of books after borrowing. Otherwise, you must define a custom exception class BookLimitExceededException that inherits from std::exception, and its what() must return the fixed string "Book borrowing limit exceeded". The main program must catch this exception and output what().

## 輸入說明
輸入三個整數 current、limit、request。
The input contains three integers: current, limit, and request.

## 輸出說明
若能成功借書，輸出借書後的總本數；否則輸出 Book borrowing limit exceeded。
If borrowing is successful, output the total number after borrowing; otherwise output Book borrowing limit exceeded.

---

## 範例測試
### 範例輸入 1
```text
2 5 2
```
### 範例輸出 1
```text
4
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <vector>

using namespace std;

class BookLimitExceededException : public exception
{
public:
    string msg;
    BookLimitExceededException(string e) : msg(e) {}
    virtual string what()
    {
        return msg;
    }
};

int main()
{
    int n, m, o;
    cin >> n >> m >> o;
    try
    {
        if (n + o <= m)
        {
            cout << n + o << endl;
        }
        else
        {
            throw BookLimitExceededException("Book borrowing limit exceeded");
        }
    }
    catch (BookLimitExceededException &e)
    {
        cout << e.what() << endl;
    }
    return 0;
}
```
