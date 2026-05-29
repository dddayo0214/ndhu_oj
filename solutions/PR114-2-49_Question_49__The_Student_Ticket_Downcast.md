# PR114-2-49: Question 49: The Student Ticket Downcast

## 題目敘述
In this problem, you will practice static_cast in an inheritance setting. A student ticket is a special kind of ticket. The base class Ticket stores the ticket holder's name and the original ticket price. The derived class StudentTicket adds a discount percentage.
You are required to design the program so that a StudentTicket object is first treated as a Ticket pointer. After that, you should use static_cast to convert the base pointer back to a StudentTicket pointer and obtain the discount information.
The input guarantees that the object is really a StudentTicket object. Therefore, the downcast in this problem is safe by the problem design. The purpose of the problem is to let you observe that static_cast can perform downcasting in an inheritance hierarchy, but the programmer must already know that the real object type is correct.
After conversion, compute the final discounted price by using this formula: finalPrice = price × (100 - discount) / 100.
本題要你練習 static_cast 在繼承架構中的使用方式。學生票是一種特殊的票券。基底類別 Ticket 負責保存持有者姓名與原始票價，衍生類別 StudentTicket 則額外保存折扣百分比。
你必須設計程式，使一個 StudentTicket 物件先被當成 Ticket 指標來使用，之後再透過 static_cast 將這個基底類別指標轉回 StudentTicket 指標，並取得折扣資訊。
題目保證這個物件的真實型別確實就是 StudentTicket，因此本題中的 downcast 在題目設定下是安全的。這題的目的是讓你觀察：static_cast 確實可以在繼承架構中做 downcasting，但前提是程式設計者已經知道真實型別正確無誤。
轉型後，請依下列公式計算折扣後票價：finalPrice = price × (100 - discount) / 100。

## 輸入說明
The input contains one line with a name, a ticket price, and a discount percentage.
輸入只有一行，依序為姓名、原始票價、以及折扣百分比。

## 輸出說明
Print three lines in the following format:
Name: name
Original price: P
Discounted price: D
Both prices must be printed with exactly two digits after the decimal point.
請輸出三行，格式如下：
Name: name
Original price: P
Discounted price: D
兩個價格都必須固定輸出到小數點後兩位。

---

## 範例測試
### 範例輸入 1
```text
Alice 120 25

```
### 範例輸出 1
```text
Name: Alice
Original price: 120.00
Discounted price: 90.00

```

### 範例輸入 2
```text
Bob 300 50

```
### 範例輸出 2
```text
Name: Bob
Original price: 300.00
Discounted price: 150.00

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
#include <iomanip>

using namespace std;

class Ticket
{
public:
    string name;
    double price;
    Ticket(string n, double p) : name(n), price(p) {}
};

class StudentTicket : public Ticket
{
public:
    StudentTicket(string n, double p) : Ticket(n, p) {}
    double discount(double discount)
    {
        return price * (100 - discount) / 100;
    }
};

int main()
{
    string name;
    double original_price, discounted_price;
    cin >> name >> original_price >> discounted_price;
    Ticket *Tptr = new StudentTicket(name, original_price);
    cout << "Name: " << Tptr->name << endl;
    cout << fixed << setprecision(2) << "Original price: " << Tptr->price << endl;
    cout << fixed << setprecision(2) << "Discounted price: " << static_cast<StudentTicket *>(Tptr)->discount(discounted_price) << endl;
}
```
