# PR114-2-05: Question 5: The Score Record

## 題目敘述
請想像建立一個**ScoreRecord**類別，用來記錄一位學生的兩次小考成績。
讀入兩個分數後，請輸出平均分數。
這題很適合練習：把資料放進物件裡，再由物件提供計算結果。
你可以自行決定成員變數與方法的設計方式。
Imagine creating a**ScoreRecord**class to store two quiz scores of a student.
After reading the two scores, output the average score.
This problem is suitable for practicing the idea of putting data into an object and asking the object to compute a result.
You may design the member variables and methods in your own way.

## 輸入說明
輸入一行，包含兩個整數**a b**，代表兩次小考分數。
The input contains one line with two integers**a b**, representing the two quiz scores.

## 輸出說明
輸出一行：**Average: X**。
平均值請以整數除法計算，也就是**(a + b) / 2**。
Output one line:**Average: X**.
Use integer division for the average, that is,**(a + b) / 2**.

---

## 範例測試
### 範例輸入 1
```text
80 90
```
### 範例輸出 1
```text
Average: 85
```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

class ScoreRecord
{
private:
    int score1, score2;

public:
    ScoreRecord(int s1, int s2) : score1(s1), score2(s2) {}
    int getAverage()
    {
        return (score1 + score2) / 2;
    }
};

int main()
{
    int s1, s2;
    std::cin >> s1 >> s2;
    ScoreRecord record(s1, s2);
    std::cout << "Average: " << record.getAverage() << std::endl;
    return 0;
}
```
