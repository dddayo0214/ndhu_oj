# PR114-2-04: Question 4: The Classroom Lamp

## 題目敘述
教室裡有一盞燈，可能是開著或關著。請想像建立一個**Lamp**類別，用來表示燈的狀態。
燈一開始是關閉的。接下來有若干操作：
**toggle**：切換狀態（開變關，關變開）最後請輸出燈的狀態。
這一題適合練習：物件擁有自己的狀態，並透過方法改變狀態。
There is a lamp in the classroom. It can be either ON or OFF. Imagine creating a**Lamp**class to represent its state.
The lamp is initially OFF. Then several operations follow:
**toggle**: switch the state (ON becomes OFF, OFF becomes ON)Output the final state of the lamp.
This problem is good for practicing the idea that an object has its own state and methods can change that state.

## 輸入說明
第一行有一個整數**n**，代表操作次數。
接下來**n**行，每行都是字串**toggle**。
The first line contains an integer**n**, the number of operations.
The next**n**lines each contain the string**toggle**.

## 輸出說明
若最後燈是開著，輸出**ON**；否則輸出**OFF**。
If the lamp is finally on, output**ON**; otherwise output**OFF**.

---

## 範例測試
### 範例輸入 1
```text
3
toggle
toggle
toggle
```
### 範例輸出 1
```text
ON
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

class Lamp
{
private:
    bool isOn;

public:
    Lamp() : isOn(false) {}
    void flip()
    {
        isOn = !isOn;
    }
    bool isLightOn()
    {
        return isOn;
    }
};

int main()
{
    Lamp lamp;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        lamp.flip();
    }
    if (lamp.isLightOn())
    {
        std::cout << "ON" << std::endl;
    }
    else
    {
        std::cout << "OFF" << std::endl;
    }
    return 0;
}
```
