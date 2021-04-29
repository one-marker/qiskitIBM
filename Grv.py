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
from qiskit.aqua.algorithms import Grover

def build():
  good_state = ['11']

  oracle = QuantumCircuit(2)
  oracle.cz(0, 1)

  grover = Grover(oracle=oracle, good_state=good_state)

  grover.grover_operator.draw(output='mpl')
  # print(grover.grover_operator.draw())
  return grover.grover_operator;
