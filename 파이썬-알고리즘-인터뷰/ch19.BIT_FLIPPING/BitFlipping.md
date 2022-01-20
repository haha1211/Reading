# Bit Flipping

## Boolean Operation
- AND
    + True and False => False
- OR
    + True or False => True
- NOT
    + not True => False
- XOR
    + 보조 연산이므로 위의 기본 연산들의 조합으로 구성 가능
    + xor 연산 => (x and not y) or (not x and y)

## Bitwise Operation
- & (AND)
- | (OR)
- ^ (XOR)
- ~ (NOT)
    + 2의 보수(two's complement)에서 1을 뺀 값
    + NOT X = -x -1
    + ~0b1100(12) = 111111....110011(-13)
    + 0b1100 -> 0b0011 하기 위해서는 자릿수 만큼의 최대값인 비트 마스크(MASK)를 만들고 그 값과 XOR 해야 함

## Two's Complement
- 컴퓨터가 음수를 저장하기 위해 일반적으로 취하는 여러 방법 중 하나
- 1의 보수(0 -> 1, 1 -> 0) + 1
    + 0111(7)의 two's complement : 1000 + 1 = 1001(-7)
    + 0111(7) + 1001(-7) = 0000(0)
