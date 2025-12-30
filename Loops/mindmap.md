# Nested Loop Iteration Trace

This document traces the execution of a nested loop structure where the inner loop depends on the current value of the outer loop index.

## Loop Structure Logic
* **Outer Loop ($i$):** Iterates through values $\{1, 2, 3\}$.
* **Inner Loop ($j$):** Iterates through `range(i)`, which means $j$ takes values from $0$ up to $i-1$.
* **Reset Rule:** The index $j$ resets to $0$ at the start of every new $i$ iteration.

---

## Execution Steps

### Step 1: First Outer Iteration ($i = 1$)
* **Outer loop sets:** $i = 1$
* **Inner loop range:** `range(1)` $\rightarrow$ $j = \{0\}$
* **Output:** * `(1, 0)`
* *Inner loop terminates.*

### Step 2: Second Outer Iteration ($i = 2$)
* **Outer loop sets:** $i = 2$
* **Inner loop range:** `range(2)` $\rightarrow$ $j = \{0, 1\}$
* **Output:**
  * `(2, 0)`
  * `(2, 1)`
* *Inner loop terminates.*

### Step 3: Third Outer Iteration ($i = 3$)
* **Outer loop sets:** $i = 3$
* **Inner loop range:** `range(3)` $\rightarrow$ $j = \{0, 1, 2\}$
* **Output:**
  * `(3, 0)`
  * `(3, 1)`
  * `(3, 2)`
* *Inner loop terminates.*

---

## Final Output Summary
The sequence of printed pairs is:
1. `(1, 0)`
2. `(2, 0)`
3. `(2, 1)`
4. `(3, 0)`
5. `(3, 1)`
6. `(3, 2)`