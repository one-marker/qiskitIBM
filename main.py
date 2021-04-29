import numpy as np
import math
import Teleport as tp
from qiskit import(
  QuantumCircuit,
  QuantumRegister,
  ClassicalRegister,
  Aer,
  execute)
from qiskit.visualization import plot_histogram

qc = tp.teleport()
print(qc.draw())