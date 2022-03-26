## From the previous assignment.

Consider the feasibility problem: \
We have to decide whether there exists a non-negative integer vector $z^* \in \mathbb{Z}^n_{\geq 0}$ such that $A z^* = b$ holds.
The solution $z^*$ gives rise to a sequence of vectors $v_1, \dots, v_t$ such that each $v_i$ is a comlumn of $A$ and

$$
v_1 + \dots + v_t = b
$$

The $i$-th column of $A$ appears $z_i^*$ times on the left of the equation and $t = ||z^*||_1$. The equation can be rewrited as:

$$
(v_1 - b/t) + \dots + (v_t - b/t) = 0
$$

Observe that the infinity norm of each $v_i - b/t$ is at most $2\Delta$. Then, we can apply the Steinitz Lemma.

