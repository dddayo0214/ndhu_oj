# PR114-2-06: Question 6: The Simple Clock Constructor

## 題目敘述
請設計一個**Clock**類別，使用建構子接收小時與分鐘，並儲存到物件中。
接著輸出這個時鐘物件中的 hour 與 minute。這一題的重點是練習用**constructor**初始化物件。
Design a**Clock**class. Use a constructor to receive the hour and minute and store them in the object.
Then output the hour and minute stored in the clock object. The main goal is to practice initializing an object with a**constructor**.

## 輸入說明
輸入只有一行，包含兩個整數**hour minute**。
The input contains one line with two integers:**hour minute**.

## 輸出說明
請輸出兩行：
**Hour: hour**
**Minute: minute**
Output exactly two lines:
**Hour: hour**
**Minute: minute**

---

## 範例測試
### 範例輸入 1
```text
7 30
```
### 範例輸出 1
```text
Hour: 7
Minute: 30
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class Clock
{
private:
    int hour, minute;

public:
    Clock(int h, int m) : hour(h), minute(m) {};
    int getHour()
    {
        return hour;
    }
    int getMinute()
    {
        return minute;
    }
};

int main()
{
    int h, m;
    cin >> h >> m;
    Clock clock(h, m);
    cout << "Hour: " << clock.getHour() << endl;
    cout << "Minute: " << clock.getMinute() << endl;
    return 0;
}
```
