# gawCalc

Every time I encounter a new programming language I take this example to get to know that language. It's a calculator that works with RPN (Reverse Polish Notation). This version is written in Python.

## RPN or Reverse Polish Notation
An article about RPN can be [found here](https://en.wikipedia.org/wiki/Reverse_Polish_notation). In short, when we would write:

'normal' notation:

**```45 + (67 - 32)
```**

In RPN that would be:

**```67 32 - 45 +
```**

So we start inside the inner brackets and work our way out.

## Stack
RPN is one of the cases in which we use a stack mechanism to push parts of the result onto and pop them off when they are needed for calcuations.
