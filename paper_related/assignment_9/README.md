I first wanted to improve the running time using multithreading, but this website explains that multithreading doesn't work with numerically tasks:

https://medium.com/python-experiments/parallelising-in-python-mutithreading-and-mutiprocessing-with-practical-templates-c81d593c1c49

"However, if the task is highly numerically intensive, then no benefit can be gained using Python multithreading. In contrast to the sleeping task, the prime determination is computational. There is little waiting time on the disk IO."

Then we will use multiprocessing, and we get better results.

Links:

The algorithm:

https://github.com/SamuelBismuth/prtpy/blob/improve_running/prtpy/partitioning/steinitz.py

The benchmark:

https://github.com/SamuelBismuth/prtpy/blob/improve_running/benchmarks/benchmark_efficiency.py