FROM python:3.9

RUN pip3 install qiskit
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install pylatexenc

COPY . .

RUN python3 main.py
