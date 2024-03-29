

# CMPS 2200 Assignment 1

**Name:** Jacob Hornung


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 

  Yes, because since $f(n)$ is equal to $2^{n+1}$ and $g(n)$ is equal to $(2^n)$, and we can then have constants of C = 2 and k = 1 to show that $|2^{n+1}| \leq C|2^n|$ for all $n \geq k$. This can then become the inequality of $|2^{n+1}| = 2^{n+1} \leq 2 \cdot 2^n = 2|2^n|$, showing that for all $n \geq 1$, the inequality $|2^{n+1}| \leq 2|2^n|$ is true.
  
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     

  No, because (using the same reasoning as the previous question) you would need to find values for C and k which make $|2^{2^n}| \leq C|2^n|$ for all $n \geq k$ true, which is impossible. The function $2^{2^n}$ grows much faster than $2^n$, and so there are no values for C and k which make the inequality true.
  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    

  No, because $n^{1.01}$ grows much faster than $(\mathrm{log}^2 n)$, meaning there is no value of C and k to make the inequality true.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  

  Yes, becuase in Big Omega notation, a function $f(n)$ is in a set $\Omega(g(n))$ if positive contants of $C$ and $k$ exist such that the inequality $|f(n)| \geq C|g(n)|$ is true. When we choose $C = 1$ and $k = 1$, the inequality becomes $n^{1.01} \geq \log^2 n$ which is true because the function $n^{1.01}$ grows much faster than $\log^2 n$.

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  

  No, because $\sqrt{n}$ grows faster than $(\mathrm{log} n)^3)$, so the inequality  $|\sqrt{n}| \leq C|(\log n)^3|$ can never be true.

  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  

  Yes, because if we choose $C = 1$ and $k = 1$ then we have the inequality $|\sqrt{n}| = \sqrt{n} \geq 1 \cdot (\log n)^3$ which is true, meaning that $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$.




2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 

```
\begin{array}{l}
\mathit{foo}~x = \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
```


  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
 
  Foo calculates the nth (or xth) number in the Fibonacci sequence. It starts with an input x, and if x is 0 or 1, it returns x. If not, it recursively adds the results of foo(x-1) and foo(x-2) to compute the Fibonacci number. It keeps calling foo recursively until the called number is 0 or 1, which then starts adding up all those values.




3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  
  
  The work for this function is O(n) because the worst case for this function is searching through each value of myArray. The span is also O(n) because there are no parallel operations that are performed.

  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  

  The work is equal to O(n), because it performs a sequential number of tasks that are all a constant number in relation to the size (n) of the input. The span is equal to O(log n) because the input list is divided into two halves at each level of recursion, and since span is the longest chain of operations, the max depth of the recursion is O(log n).

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

  The work is equal to O(n log n) because at each level of recursion, there are two seperate operations (the left and the right halves of the list), and they can be executed at the same time/in parallel. Therefore, the work at each level is O(n) for n elements. The number of levels of recursion is proportional to the log of the length of the input list so O(log n). Then the total work (the sum of all levels) of the parallelized algorithm is O(n log n). 
  The span is equal to O(log n) because t each level of recursion, the work can be divided into two independent operations that can be executed at the same time, so the span for each level is O(1). Since each level can be executed in parallel, and there are O(log n) levels of recursion, the overall span of the parallelized algorithm is O(log n).
