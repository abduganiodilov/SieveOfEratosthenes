# Sieve of Eratosthenes

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A classic algorithm for efficiently finding all prime numbers up to a given limit \( N \). This repository contains a concise Python implementation that demonstrates how to mark composite numbers and identify primes in the range from 2 to \( N \).

---

## Table of Contents

- [Overview](#overview)
- [Algorithm Steps](#algorithm-steps)
- [Usage](#usage)
  - [Installation](#installation)
  - [Running the Script](#running-the-script)
- [Example Output](#example-output)
- [Code Explanation](#code-explanation)
- [Further Improvements](#further-improvements)
- [License](#license)

---

## Overview

The **Sieve of Eratosthenes** is a simple yet powerful method to enumerate prime numbers. By systematically “crossing out” multiples of each prime candidate, the algorithm leaves only prime numbers marked as “uncrossed.”

**Key advantages:**
- **Speed**: Runs in \( O(N \log \log N) \) time, making it efficient for large \( N \).
- **Simplicity**: Easy to implement and understand.
- **Practical**: Widely used in cryptography, math research, and educational examples.

---

## Algorithm Steps

1. **Initialize**  
   Create an array `primes` of length \( N \) and set every element to `True` except for indices 0 and 1 (they are not prime).

2. **Sieve**  
   - For each number \( k \) from 2 up to \(\sqrt{N}\):
     - If `primes[k]` is `True`:
       - Mark all multiples of \( k \) (from \( k^2 \) to \( N \)) as `False`.

3. **Collect Results**  
   - All indices \( i \) where `primes[i]` remains `True` correspond to prime numbers.

---

## Usage

### Installation

No external packages are required besides Python’s standard library. Make sure you have **Python 3.x** installed:

```bash
python --version
