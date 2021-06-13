#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2019 12:40
:Licence MIT
Part of 2019

"""

from queue import Queue


class Comp:
    def __init__(self, code):
        self._code = code
        self._pos = 0
        self._rel = 0
        self.inputs = Queue()
        self.outputs = Queue()

    def __getitem__(self, item):
        while item >= len(self._code):
            self._code.append(0)
        return self._code[item]

    def __setitem__(self, key, value):
        tmp = self[key]
        self._code[key] = value

    def handle_param(self, param):
        par = self[self._pos + param]
        # position mode
        mode = self[self._pos] // pow(10, 1 + param) % 10
        # position
        if mode == 0:
            return self[par]
        # value
        elif mode == 1:
            return par
        # relative
        elif mode == 2:
            return self[self._rel + par]
        else:
            print(f'Cant handle mode {mode}')

    def handle_ret(self, param):
        mode = self[self._pos] // pow(10, 1 + param) % 10
        if mode == 0:
            return self[self._pos + param]
        if mode == 1:
            return self._pos + param
        if mode == 2:
            return self._rel + self[self._pos + param]
        else:
            print('Cant handle mode of return code')

    def simulate(self):
        while True:
            instruction = self._code[self._pos] % 100
            if instruction == 1:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self[self.handle_ret(3)] = par1 + par2
                self._pos += 4
            elif instruction == 2:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self[self.handle_ret(3)] = par1 * par2
                self._pos += 4
            elif instruction == 3:
                if self.inputs.empty():
                    return False
                self[self.handle_ret(1)] = self.inputs.get()
                self._pos += 2
            elif instruction == 4:
                par1 = self.handle_param(1)
                self.outputs.put(par1)
                self._pos += 2
            elif instruction == 5:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self._pos = par2 if par1 != 0 else self._pos + 3
            elif instruction == 6:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self._pos = par2 if par1 == 0 else self._pos + 3
            elif instruction == 7:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self[self.handle_ret(3)] = 1 if par1 < par2 else 0
                self._pos += 4
            elif instruction == 8:
                par1 = self.handle_param(1)
                par2 = self.handle_param(2)
                self[self.handle_ret(3)] = 1 if par1 == par2 else 0
                self._pos += 4
            elif instruction == 9:
                par1 = self.handle_param(1)
                self._rel += par1
                self._pos += 2
            elif instruction == 99:
                return True
            else:
                print(f'Cant handle code {instruction} at pos {self._pos}')
                self._pos += 1

