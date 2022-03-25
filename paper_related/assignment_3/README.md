# Running Examples

## Preliminaries

In this assignment, we are asked for finding some running examples.

Recall that the chosen paper is composed of two main algorithms that solve IP standard problems. We chose to focus on the first algorithm of the paper and to ignore the second. 

## Main IP algorithm

### Running time
The algorithm running time is: 

$$
(m \cdot \Delta)^{O(m)} \cdot ||b||^2_\infty,
$$

where $\Delta$ is an upper bound of each absolute value of an entry in $A$.

### Input of the algorithm

The algorithm takes as input a standard IP in the form:

$$
	\max \{c^T x : A x = b, x \geq 0, x \in \mathbb{Z}^n \},
$$
	
where $A \in \mathbb{Z}^{m \times n}$, $b \in \mathbb{Z}^m$ and $c \in \mathbb{Z}^n$. 

### Output of the algorithm

The algorithm returns the optimal solution of the problem via a set of assigned variables $x$ if there exists one, or, otherwise, returns 'not feasible'. 

## Steinitz Lemma

The algorithm is essentially based on the Steinitz Lemma. Then, we will provide some running examples of the lemma. 

### Input of the Lemma

$n$ vectors $x_i$ in $\mathbb{R}^m$ such that the sum of every $x_i$ is 0 and for each $i$, the norm of $x_i$ is smaller or equal to 1

### Output of the Lemma

A permutation $\pi$ such that all partial sum satisfy that the norm of the sum of every $n$ vector $x_{\pi}$ is smaller of equal to $c(m)$, we can say upper bounded by $c(m)$, where $c(m)$ is a constant depending on $m$ only.

## Samples

For each black-box, we will provide 

* From simple examples to hard examples. 
    * Begin with simple input with one single number.
    * Two numbers.
    * Continue until the input becomes hard.
* Check every condition. For each if of the black-box, we provide an input that will trigger the if.
* Try to recognize edge cases.
    * Cases where the black-box manages well.
    * Cases where the black-box doesn't manage well.