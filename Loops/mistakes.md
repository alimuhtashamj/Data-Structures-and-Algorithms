# DSA Range & Nested Loop Mistakes – Corrected

## Mistake 1: Misunderstanding `range(1,1)`
**Your answer:**  
> "this loop never runs because it is supposed to end before 1, but before 1 there is 1 allocated in range. so it pushes error and doesnt run."

**Correction:**  
- The loop **does not run**, but there is **no error**.  
- Python sees that there is **no number satisfying `start ≤ i < stop`**, so it executes **zero iterations** silently.  
- Key takeaway: `start == stop` → **loop never executes**.

---

## Mistake 2: Nested loop inner variable carries over
**Your answer:**  
> "j starts new always for i because once the outer iteration is done the value of j resets to 0."

**Correction:**  
- ✅ Conceptually correct.  
- Inner loop variables are **scoped to their loop**, meaning they **restart for every new outer iteration**.  
- Key takeaway: **j resets to 0 for each new i**.

---

## Mistake 3: First value of `j` in `range(i)`
**Your answer:**  
> "for the range(i) the j itself has no value. it takes from 0. so for first i iteration j starts from 0."

**Correction:**  
- `range(i)` **generates numbers starting from 0 up to i−1**.  
- First value of `j` is always 0 **because `range` defaults to start=0**, not because `j` “has no value”.  
- Last value = `i−1`.  
- Key takeaway: **range(n) → 0,1,2,...,n-1**

---

## Mistake 5: General range logic

- Thought `range()` ends “automatically” at something else or j continues from previous loop.
**Correction / Rule:**

- range(stop) → 0 to stop−1
- range(start, stop) → start to `stop−1`
- range(start, stop, step) → moves by step, stops before stop
- Inner loops reset every outer iteration
- Stop is never included

`from 0 to i-1` in case of for j in `range(i)` and it is logical to assume
the range starts from n and moves until the number and last number is excluded.
