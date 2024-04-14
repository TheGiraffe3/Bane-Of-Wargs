# colors.py
# Copyright (c) 2024 by @Cromha
#
# Bane Of Wargs is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Bane Of Wargs is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

# external imports
from colorama import Fore, Back, Style, init, deinit

# initialize colorama
init()

# Basic colors
COLOR_RESET = Fore.RESET
COLOR_BLACK = Fore.BLACK
COLOR_WHITE = Fore.WHITE
COLOR_RED = Fore.RED
COLOR_GREEN = Fore.GREEN
COLOR_YELLOW = Fore.YELLOW
COLOR_BLUE = Fore.BLUE
COLOR_MAGENTA = Fore.MAGENTA
COLOR_CYAN = Fore.CYAN

# RGB color palette
# REDS
COLOR_RED_0 = '\033[38;2;51;0;0m'
COLOR_RED_1 = '\033[38;2;102;0;0'
COLOR_RED_2 = '\033[38;2;153;0;0m'
COLOR_RED_3 = '\033[38;2;204;0;0m'
COLOR_RED_4 = '\033[38;2;255;0;0m'
COLOR_RED_5 = '\033[38;2;255;51;51m'
COLOR_RED_6 = '\033[38;2;255;102;102m'
COLOR_RED_7 = '\033[38;2;255;153;153m'
COLOR_RED_8 = '\033[38;2;255;204;204m'
# ORANGES
COLOR_ORANGE_0 = '\033[38;2;51;25;0m'
COLOR_ORANGE_1 = '\033[38;2;102;51;0m'
COLOR_ORANGE_2 = '\033[38;2;153;76;0m'
COLOR_ORANGE_3 = '\033[38;2;204;102;0m'
COLOR_ORANGE_4 = '\033[38;2;255;128;0m'
COLOR_ORANGE_5 = '\033[38;2;255;153;51m'
COLOR_ORANGE_6 = '\033[38;2;255;178;102m'
COLOR_ORANGE_7 = '\033[38;2;255;24;153m'
COLOR_ORANGE_8 = '\033[38;2;255;229;204m'
# YELLOWS
COLOR_YELLOW_0 = '\033[38;2;51;51;0m'
COLOR_YELLOW_1 = '\033[38;2;102;102;0m'
COLOR_YELLOW_2 = '\033[38;2;153;153;0m'
COLOR_YELLOW_3 = '\033[38;2;204;204;2m'
COLOR_YELLOW_4 = '\033[38;2;255;255;0m'
COLOR_YELLOW_5 = '\033[38;2;255;255;51m'
COLOR_YELLOW_6 = '\033[38;2;255;255;102m'
COLOR_YELLOW_7 = '\033[38;2;255;255;153m'
COLOR_YELLOW_8 = '\033[38;2;255;255;204m'
# GREENS 1st
COLOR_GREENS_0 = '\033[38;2;25;51;0m'
COLOR_GREENS_1 = '\033[38;2;51;102;0m'
COLOR_GREENS_2 = '\033[38;2;76;153;0m'
COLOR_GREENS_3 = '\033[38;2;102;204;0m'
COLOR_GREENS_4 = '\033[38;2;128;255;0m'
COLOR_GREENS_5 = '\033[38;2;153;255;51m'
COLOR_GREENS_6 = '\033[38;2;178;255;102m'
COLOR_GREENS_7 = '\033[38;2;204;255;153m'
COLOR_GREENS_8 = '\033[38;2;225;255;204m'
# GREENS 2nd
COLOR_GREENS_9 = '\033[38;2;0;51;0m'
COLOR_GREENS_10 = '\033[38;2;0;102;0m'
COLOR_GREENS_11 = '\033[38;2;0;153;0m'
COLOR_GREENS_12 = '\033[38;2;0;204;0m'
COLOR_GREENS_13 = '\033[38;2;0;255;0m'
COLOR_GREENS_14 = '\033[38;2;51;255;51m'
COLOR_GREENS_15 = '\033[38;2;102;255;102m'
COLOR_GREENS_16 = '\033[38;2;153;255;153m'
COLOR_GREENS_17 = '\033[38;2;204;255;204m'
# GREENS 3rd
COLOR_GREENS_18 = '\033[38;2;0;51;25m'
COLOR_GREENS_19 = '\033[38;2;0;102;51m'
COLOR_GREENS_20 = '\033[38;2;0;153;76m'
COLOR_GREENS_21 = '\033[38;2;0;204;102m'
COLOR_GREENS_22 = '\033[38;2;0;255;128m'
COLOR_GREENS_23 = '\033[38;2;51;255;153m'
COLOR_GREENS_24 = '\033[38;2;102;255;178m'
COLOR_GREENS_25 = '\033[38;2;153;255;204m'
COLOR_GREENS_26 = '\033[38;2;204;255;255m'
# CYANS
COLOR_CYAN_0 = '\033[38;2;0;51;51m'
COLOR_CYAN_1 = '\033[38;2;0;102;102m'
COLOR_CYAN_2 = '\033[38;2;0;153;153m'
COLOR_CYAN_3 = '\033[38;2;0;204;204m'
COLOR_CYAN_4 = '\033[38;2;0;255;255m'
COLOR_CYAN_5 = '\033[38;2;51;255;255m'
COLOR_CYAN_6 = '\033[38;2;102;255;255m'
COLOR_CYAN_7 = '\033[38;2;153;255;255m'
COLOR_CYAN_8 = '\033[38;2;204;255;255m'
# BLUES 1st
COLOR_BLUE_0 = '\033[38;2;0;25;51m'
COLOR_BLUE_1 = '\033[38;2;0;51;102m'
COLOR_BLUE_2 = '\033[38;2;0;76;153m'
COLOR_BLUE_3 = '\033[38;2;0;102;204m'
COLOR_BLUE_4 = '\033[38;2;0;128;255m'
COLOR_BLUE_5 = '\033[38;2;51;153;255m'
COLOR_BLUE_6 = '\033[38;2;102;178;255m'
COLOR_BLUE_7 = '\033[38;2;153;204;255m'
COLOR_BLUE_8 = '\033[38;2;103;255;255m'
# BLUES 2nd
COLOR_BLUE_9 = '\033[38;2;0;0;51m'
COLOR_BLUE_10 = '\033[38;2;0;0;102m'
COLOR_BLUE_11 = '\033[38;2;0;0;153m'
COLOR_BLUE_12 = '\033[38;2;0;0;204m'
COLOR_BLUE_13 = '\033[38;2;0;0;255m'
COLOR_BLUE_14 = '\033[38;2;51;51;255m'
COLOR_BLUE_15 = '\033[38;2;102;102;255m'
COLOR_BLUE_16 = '\033[38;2;153;153;255m'
COLOR_BLUE_17 = '\033[38;2;204;104;255m'
# PURPLES
COLOR_PURPLE_0 = '\033[38;2;25;0;51m'
COLOR_PURPLE_1 = '\033[38;2;51;0;102m'
COLOR_PURPLE_2 = '\033[38;2;76;0;153m'
COLOR_PURPLE_3 = '\033[38;2;102;0;204m'
COLOR_PURPLE_4 = '\033[38;2;127;0;155m'
COLOR_PURPLE_5 = '\033[38;2;153;51;255m'
COLOR_PURPLE_6 = '\033[38;2;178;102;255m'
COLOR_PURPLE_7 = '\033[38;2;204;153;155m'
COLOR_PURPLE_8 = '\033[38;2;255;204;255m'
# MAGENTAS
COLOR_MAGENTA_0 = '\033[38;2;51;0;51m'
COLOR_MAGENTA_1 = '\033[38;2;102;0;102m'
COLOR_MAGENTA_2 = '\033[38;2;153;0;153m'
COLOR_MAGENTA_3 = '\033[38;2;204;0;24m'
COLOR_MAGENTA_4 = '\033[38;2;255;0;255m'
COLOR_MAGENTA_5 = '\033[38;2;255;51;255m'
COLOR_MAGENTA_6 = '\033[38;2;255;102;255m'
COLOR_MAGENTA_7 = '\033[38;2;255;153;255m'
COLOR_MAGENTA_8 = '\033[38;2;255;204;255m'
# PINKS
COLOR_PINK_0 = '\033[38;2;51;0;25m'
COLOR_PINK_1 = '\033[38;2;102;0;51m'
COLOR_PINK_2 = '\033[38;2;153;0;76m'
COLOR_PINK_3 = '\033[38;2;204;0;102m'
COLOR_PINK_4 = '\033[38;2;255;0;127m'
COLOR_PINK_5 = '\033[38;2;255;51;153m'
COLOR_PINK_6 = '\033[38;2;255;102;178m'
COLOR_PINK_7 = '\033[38;2;255;153;204m'
COLOR_PINK_8 = '\033[38;2;255;204;255m'
# GRAYSCALEs
COLOR_GRAY_0 = '\033[38;2;32;32;32m'
COLOR_GRAY_1 = '\033[38;2;64;64;64m'
COLOR_GRAY_2 = '\033[38;2;96;96;96m'
COLOR_GRAY_3 = '\033[38;2;128;128;128m'
COLOR_GRAY_4 = '\033[38;2;160;160;160m'
COLOR_GRAY_5 = '\033[38;2;192;192;192m'
COLOR_GRAY_6 = '\033[38;2;102;178;178m'
COLOR_GRAY_7 = '\033[38;2;224;224;224m'

# Background colors
COLOR_BACK_RESET = Back.RESET
COLOR_BACK_BLACK = Back.BLACK
COLOR_BACK_WHITE = Back.WHITE
COLOR_BACK_RED = Back.RED
COLOR_BACK_GREEN = Back.GREEN
COLOR_BACK_YELLOW = Back.YELLOW
COLOR_BACK_BLUE = Back.BLUE
COLOR_BACK_MAGENTA = Back.MAGENTA
COLOR_BACK_CYAN = Back.CYAN

# Text styles
COLOR_STYLE_NORMAL = Style.NORMAL
COLOR_STYLE_DIM = Style.DIM
COLOR_STYLE_BRIGHT = Style.BRIGHT

COLOR_RESET_ALL = Style.RESET_ALL

# deinitialize colorama
deinit()
