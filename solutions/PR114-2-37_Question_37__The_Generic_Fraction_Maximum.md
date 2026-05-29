# PR114-2-37: Question 37: The Generic Fraction Maximum

## 題目敘述
You are asked to design a generic comparison tool in C++. The main goal of this problem is to let you experience an important limitation of templates before learning more advanced constraints. A function template can be written once and reused for many types, but it still assumes that the operations used inside the template are valid for the given type.
In this problem, you should design a function template that returns the larger of two values. However, the values are not built-in numbers. They are Fraction objects. Each fraction has a numerator and a denominator.
To make your generic function work with Fraction, you must overload the comparison operator for the Fraction class. In other words, this problem is not only about templates, but also about how operator overloading allows a user-defined class to cooperate with a generic function.
Your task is to read two fractions, determine which one is larger, and output that fraction in simplified form. If the two fractions are equal, output the first one after simplification.
本題要你在 C++ 中設計一個泛型比較工具。這題的重點，是讓你在學習更進一步的限制機制之前，先感受到 template 的一個重要困境：template 雖然可以寫一次、套用到很多型別，但前提是模板裡用到的運算，對該型別真的有被定義。
在本題中，你應該設計一個函式模板，用來回傳兩個值中較大的那一個。但這裡的資料不是內建數字，而是 Fraction 物件。每個分數物件都有分子與分母。
若要讓你的泛型函式能正確處理 Fraction，你就必須為 Fraction 類別多載比較運算子。也就是說，這題不只是 template 練習，同時也是讓你理解：operator overloading 能讓自訂類別配合 generic function 一起工作。
你的任務是讀入兩個分數，判斷哪一個比較大，並輸出約分後的結果。若兩個分數相等，請輸出第一個分數的約分結果。
You should solve this problem using object-oriented programming. You are expected to define a Fraction class, encapsulate its data members, and overload the comparison operator so that your function template can compare Fraction objects correctly.
你應該以物件導向方式完成本題。請自行定義 Fraction 類別，妥善封裝其資料成員，並多載比較運算子，讓你的函式模板可以正確比較 Fraction 物件。

## 輸入說明
The input contains one line with four integers: a b c d.
The first fraction is a/b and the second fraction is c/d. It is guaranteed that b and d are nonzero.
輸入只有一行，包含四個整數 a b c d。
第一個分數為 a/b，第二個分數為 c/d。題目保證 b 與 d 不為 0。

## 輸出說明
Output the larger fraction in simplified form as p/q.
If the two fractions are equal, output the simplified form of the first fraction.
請輸出較大的分數，格式為 p/q，且必須為最簡分數。
若兩個分數相等，請輸出第一個分數約分後的結果。

---

## 範例測試
### 範例輸入 1
```text
1 2 3 4

```
### 範例輸出 1
```text
3/4

```


---

## 我的程式碼 (C++)
```cpp
#include <iostream>

using namespace std;

class Fraction
{
public:
    int numerator, denominator;
    Fraction(int n, int d) : numerator(n), denominator(d)
    {
        int g;
        int nown = abs(numerator);
        int nowd = abs(denominator);
        if (numerator == 0)
            return;
        if (nown < nowd)
            swap(nown, nowd);
        while (nown % nowd != 0)
        {
            g = nown % nowd;
            nown = nowd;
            nowd = g;
        }
        numerator /= nowd;
        denominator /= nowd;
    }
    bool operator>(Fraction f)
    {
        return (numerator * f.denominator > f.numerator * denominator);
    }
    void display()
    {
        if (numerator == 0)
        {
            cout << 0;
        }
        else if (denominator == 1)
        {
            cout << numerator;
        }
        else
        {
            cout << numerator << '/' << denominator;
        }
    }
};

template <typename T>
T cmp(T &a, T &b)
{
    return (a > b ? a : b);
}

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    Fraction num1(a, b), num2(c, d);
    Fraction ans = cmp(num1, num2);
    ans.display();
}
```
