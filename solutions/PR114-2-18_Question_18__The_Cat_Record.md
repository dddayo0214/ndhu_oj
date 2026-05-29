# PR114-2-18: Question 18: The Cat Record

## 題目敘述
請建立一個基底類別與一個衍生類別，並使用衍生類別物件輸出完整資訊。題目要求你練習基礎繼承語法，以及從基底類別延伸出新類別的概念。
你應該用 class、object 與 inheritance 來完成本題。
Create a base class and a derived class, then use a derived-class object to output the complete information. This problem is meant to help you practice the basic syntax of inheritance and the idea of extending a new class from a base class.
You should solve this problem with class, object, and inheritance.

## 輸入說明
輸入一行，包含一個不含空白的字串 brand 與一個整數 seats。
The input contains one line with a string brand and an integer seats.

## 輸出說明
輸出兩行：
Brand: brand
Seats: seats
Output exactly two lines:
Brand: brand
Seats: seats

---

## 範例測試
### 範例輸入 1
```text
Toyota 5
```
### 範例輸出 1
```text
Brand: Toyota
Seats: 5
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>
using namespace std;

class CarBrand
{
protected:
    string brand;

public:
    string &getBrand() { return brand; }
};

class Car : public CarBrand
{
private:
    string seats;

public:
    Car(string seats) : seats(seats)
    {
    }
    string getSeats() { return seats; }
};

int main()
{
    string brand, seats;
    cin >> brand >> seats;
    Car car(seats);
    car.getBrand() = brand;
    cout << "Brand: " << car.getBrand() << endl;
    cout << "Seats: " << car.getSeats() << endl;
    return 0;
}
```
