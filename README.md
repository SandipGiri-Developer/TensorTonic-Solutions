# Concepts From Scratch

Implementations of fundamental mathematical and machine learning concepts from first principles using **NumPy**.

The objective is to understand how core functions and algorithms work internally instead of relying on high-level machine learning frameworks.

---

## Purpose

Libraries such as TensorFlow or PyTorch hide the mechanics behind simple API calls.
This repository rebuilds those mechanics step-by-step using **NumPy for numerical computation**.

Each implementation focuses on:

* Mathematical understanding
* Clean and minimal code
* Explicit implementation of algorithms
* Reproducibility and experimentation

---

## Technologies

* Python
* NumPy

NumPy is used strictly for numerical operations (arrays, vectorization, matrix computation), while the core algorithms and logic are implemented manually.

---

## Topics Covered

### Mathematical Functions

* Sigmoid
* Tanh
* ReLU
* Softmax
* Log / Exponential transformations

### Linear Algebra Foundations

* Vector operations
* Dot product
* Matrix multiplication
* Norms

### Optimization

* Gradient Descent
* Numerical gradients
* Loss functions

### Machine Learning Building Blocks

* Linear Regression
* Logistic Regression
* Basic neural network components

---

## Repository Structure

```
concepts-from-scratch/

functions/
    sigmoid.py
    relu.py
    softmax.py

linear_algebra/
    dot_product.py
    matrix_multiplication.py

optimization/
    gradient_descent.py

experiments/
    small experiments and tests

README.md
```

---

## Example Implementation

Sigmoid implemented using NumPy.

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

Mathematical definition:

σ(x) = 1 / (1 + e⁻ˣ)

---

## Design Principles

* Implement concepts from first principles
* Use NumPy only for numerical computation
* Avoid high-level ML libraries
* Prefer readability over complexity

---

## Motivation

Reimplementing fundamental concepts improves intuition about:

* gradient behavior
* numerical stability
* optimization dynamics
* algorithm design

---

## Future Additions

* Backpropagation implementation
* Simple neural network from scratch
* Automatic differentiation engine
* Optimization algorithms (Adam, RMSProp)
* Visualization experiments

---

## License

MIT License


