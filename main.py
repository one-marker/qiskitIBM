import numpy as np
import math
import Teleport
import Grv

from qiskit import(
  QuantumCircuit,
  QuantumRegister,
  ClassicalRegister,
  Aer,
  execute)
from qiskit.visualization import plot_histogram


print("TELEPORT")
print(Teleport.build().draw())

print("GROVER")
print(Grv.build().draw())