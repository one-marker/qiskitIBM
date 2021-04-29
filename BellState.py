from qiskit import QuantumCircuit, assemble, Aer

# def getBellsState1(initialVector1, initialVector2):
#     qc = QuantumCircuit(2)
#     qc.initialize(initialVector1, 0)
#     qc.initialize(initialVector2, 1)
#     qc.h(0)
#     qc.cx(0, 1)
#     return qc

def getBellsState(qc, qubitIndex1, qubitIndex2):
    qc.h(qubitIndex1)
    qc.cx(qubitIndex1, qubitIndex2)
    return qc