import numpy as np
import math
import BellState
from qiskit import(
  QuantumCircuit,
  QuantumRegister,
  ClassicalRegister,
  Aer,
  execute)
from qiskit.visualization import plot_histogram

def build():
    c1 = ClassicalRegister(1)
    c2 = ClassicalRegister(1)
    c3 = ClassicalRegister(1)
    q = QuantumRegister(3)
    qc = QuantumCircuit(q, c1, c2, c3)
    qc.initialize([1/3, math.sqrt(1 - 1/9)], 0)
    qc.h(1)
    qc.cx(1,2)
    # qc = BellState.getBellsState(qc, 1, 2)
    
    
    qc.barrier()
    qc.cx(0,1)
    qc.h(0)
    qc.barrier()
    qc.measure(q[0], c1)
    qc.measure(q[1], c2)

    
    
    qc.x(2).c_if(c1, 1)
    qc.z(2).c_if(c2, 1)
    qc.measure(q[2], c3)
    sim = Aer.get_backend('qasm_simulator')
    job = execute(qc, sim)
    res = job.result().get_counts()
    print("\nres: ", res)
    
    return qc;

