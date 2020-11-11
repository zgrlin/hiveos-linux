# -*- coding: utf-8 -*-
#
# TARGET arch is: ['--include', 'stdint.h']
# WORD_SIZE is: 8
# POINTER_SIZE is: 8
# LONGDOUBLE_SIZE is: 16
#
import ctypes




ATOM_H = True # macro
ATOM_BIOS_MAGIC = 0xAA55 # macro
ATOM_ATI_MAGIC_PTR = 0x30 # macro
ATOM_ATI_MAGIC = " 761295520" # macro
ATOM_ROM_TABLE_PTR = 0x48 # macro
ATOM_ROM_PART_NUMBER_PTR = 0x6E # macro
ATOM_ROM_MAGIC = "ATOM" # macro
ATOM_ROM_MAGIC_PTR = 4 # macro
ATOM_ROM_MSG_PTR = 0x10 # macro
ATOM_ROM_CMD_PTR = 0x1E # macro
ATOM_ROM_DATA_PTR = 0x20 # macro
ATOM_CMD_INIT = 0 # macro
ATOM_CMD_SETSCLK = 0x0A # macro
ATOM_CMD_SETMCLK = 0x0B # macro
ATOM_CMD_SETPCLK = 0x0C # macro
ATOM_CMD_SPDFANCNTL = 0x39 # macro
ATOM_DATA_FWI_PTR = 0xC # macro
ATOM_DATA_IIO_PTR = 0x32 # macro
ATOM_FWI_DEFSCLK_PTR = 8 # macro
ATOM_FWI_DEFMCLK_PTR = 0xC # macro
ATOM_FWI_MAXSCLK_PTR = 0x24 # macro
ATOM_FWI_MAXMCLK_PTR = 0x28 # macro
ATOM_CT_SIZE_PTR = 0 # macro
ATOM_CT_WS_PTR = 4 # macro
ATOM_CT_PS_PTR = 5 # macro
ATOM_CT_PS_MASK = 0x7F # macro
ATOM_CT_CODE_PTR = 6 # macro
ATOM_OP_CNT = 127 # macro
ATOM_OP_EOT = 91 # macro
ATOM_CASE_MAGIC = 0x63 # macro
ATOM_CASE_END = 0x5A5A # macro
ATOM_ARG_REG = 0 # macro
ATOM_ARG_PS = 1 # macro
ATOM_ARG_WS = 2 # macro
ATOM_ARG_FB = 3 # macro
ATOM_ARG_ID = 4 # macro
ATOM_ARG_IMM = 5 # macro
ATOM_ARG_PLL = 6 # macro
ATOM_ARG_MC = 7 # macro
ATOM_SRC_DWORD = 0 # macro
ATOM_SRC_WORD0 = 1 # macro
ATOM_SRC_WORD8 = 2 # macro
ATOM_SRC_WORD16 = 3 # macro
ATOM_SRC_BYTE0 = 4 # macro
ATOM_SRC_BYTE8 = 5 # macro
ATOM_SRC_BYTE16 = 6 # macro
ATOM_SRC_BYTE24 = 7 # macro
ATOM_WS_QUOTIENT = 0x40 # macro
ATOM_WS_REMAINDER = 0x41 # macro
ATOM_WS_DATAPTR = 0x42 # macro
ATOM_WS_SHIFT = 0x43 # macro
ATOM_WS_OR_MASK = 0x44 # macro
ATOM_WS_AND_MASK = 0x45 # macro
ATOM_WS_FB_WINDOW = 0x46 # macro
ATOM_WS_ATTRIBUTES = 0x47 # macro
ATOM_WS_REGPTR = 0x48 # macro
ATOM_IIO_NOP = 0 # macro
ATOM_IIO_START = 1 # macro
ATOM_IIO_READ = 2 # macro
ATOM_IIO_WRITE = 3 # macro
ATOM_IIO_CLEAR = 4 # macro
ATOM_IIO_SET = 5 # macro
ATOM_IIO_MOVE_INDEX = 6 # macro
ATOM_IIO_MOVE_ATTR = 7 # macro
ATOM_IIO_MOVE_DATA = 8 # macro
ATOM_IIO_END = 9 # macro
ATOM_IO_MM = 0 # macro
ATOM_IO_PCI = 1 # macro
ATOM_IO_SYSIO = 2 # macro
ATOM_IO_IIO = 0x80 # macro
__all__ = \
    ['ATOM_ARG_FB', 'ATOM_ARG_ID', 'ATOM_ARG_IMM', 'ATOM_ARG_MC',
    'ATOM_ARG_PLL', 'ATOM_ARG_PS', 'ATOM_ARG_REG', 'ATOM_ARG_WS',
    'ATOM_ATI_MAGIC', 'ATOM_ATI_MAGIC_PTR', 'ATOM_BIOS_MAGIC',
    'ATOM_CASE_END', 'ATOM_CASE_MAGIC', 'ATOM_CMD_INIT',
    'ATOM_CMD_SETMCLK', 'ATOM_CMD_SETPCLK', 'ATOM_CMD_SETSCLK',
    'ATOM_CMD_SPDFANCNTL', 'ATOM_CT_CODE_PTR', 'ATOM_CT_PS_MASK',
    'ATOM_CT_PS_PTR', 'ATOM_CT_SIZE_PTR', 'ATOM_CT_WS_PTR',
    'ATOM_DATA_FWI_PTR', 'ATOM_DATA_IIO_PTR', 'ATOM_FWI_DEFMCLK_PTR',
    'ATOM_FWI_DEFSCLK_PTR', 'ATOM_FWI_MAXMCLK_PTR',
    'ATOM_FWI_MAXSCLK_PTR', 'ATOM_H', 'ATOM_IIO_CLEAR',
    'ATOM_IIO_END', 'ATOM_IIO_MOVE_ATTR', 'ATOM_IIO_MOVE_DATA',
    'ATOM_IIO_MOVE_INDEX', 'ATOM_IIO_NOP', 'ATOM_IIO_READ',
    'ATOM_IIO_SET', 'ATOM_IIO_START', 'ATOM_IIO_WRITE', 'ATOM_IO_IIO',
    'ATOM_IO_MM', 'ATOM_IO_PCI', 'ATOM_IO_SYSIO', 'ATOM_OP_CNT',
    'ATOM_OP_EOT', 'ATOM_ROM_CMD_PTR', 'ATOM_ROM_DATA_PTR',
    'ATOM_ROM_MAGIC', 'ATOM_ROM_MAGIC_PTR', 'ATOM_ROM_MSG_PTR',
    'ATOM_ROM_PART_NUMBER_PTR', 'ATOM_ROM_TABLE_PTR',
    'ATOM_SRC_BYTE0', 'ATOM_SRC_BYTE16', 'ATOM_SRC_BYTE24',
    'ATOM_SRC_BYTE8', 'ATOM_SRC_DWORD', 'ATOM_SRC_WORD0',
    'ATOM_SRC_WORD16', 'ATOM_SRC_WORD8', 'ATOM_WS_AND_MASK',
    'ATOM_WS_ATTRIBUTES', 'ATOM_WS_DATAPTR', 'ATOM_WS_FB_WINDOW',
    'ATOM_WS_OR_MASK', 'ATOM_WS_QUOTIENT', 'ATOM_WS_REGPTR',
    'ATOM_WS_REMAINDER', 'ATOM_WS_SHIFT']
