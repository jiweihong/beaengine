#!/usr/bin/python
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# @author : beaengine@gmail.com

from headers.BeaEnginePython import *
from nose.tools import *

class TestSuite:
    def test(self):


        # VEX.NDS.L1.0F.W0 42 /r
        # kandnW k1, k2, k3

        myVEX = VEX('VEX.NDS.L1.0F.W0')
        myVEX.vvvv = 0b1101
        myVEX.R = 1
        Buffer = '{}42cb'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x42')
        assert_equal(myDisasm.instr.Reserved_.VEX.L, 1)
        assert_equal(myDisasm.instr.Reserved_.REX.W_, 0)
        assert_equal(myDisasm.instr.Reserved_.MOD_, 3)
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kandnw ')
        assert_equal(myDisasm.instr.repr, 'kandnw k1, k2, k3')

        # VEX.L1.66.0F.W0 42 /r
        # kandnB k1, k2, k3

        myVEX = VEX('VEX.L1.66.0F.W0')
        myVEX.vvvv = 0b1101
        myVEX.R = 1
        Buffer = '{}42cb'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x42')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kandnb ')
        assert_equal(myDisasm.instr.repr, 'kandnb k1, k2, k3')

        # VEX.L1.0F.W1 42 /r
        # kandnQ k1, k2, k3

        myVEX = VEX('VEX.L1.0F.W1')
        myVEX.vvvv = 0b1101
        myVEX.R = 1
        Buffer = '{}42cb'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x42')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kandnq ')
        assert_equal(myDisasm.instr.repr, 'kandnq k1, k2, k3')

        # VEX.L1.66.0F.W1 42 /r
        # kandnD k1, k2, k3

        myVEX = VEX('VEX.L1.66.0F.W1')
        myVEX.vvvv = 0b1101
        myVEX.R = 1
        Buffer = '{}42cb'.format(myVEX.c4()).decode('hex')
        myDisasm = Disasm(Buffer)
        myDisasm.read()
        assert_equal(hex(myDisasm.instr.Instruction.Opcode), '0x42')
        assert_equal(myDisasm.instr.Instruction.Mnemonic, 'kandnd ')
        assert_equal(myDisasm.instr.repr, 'kandnd k1, k2, k3')
