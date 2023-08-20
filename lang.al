; Initialize the value
mov x, 10
mov i, 0

; Run loop until i == 10
rlp i, 10
add x, 1
inc i
elp

; Reset the iterator
mov i, 20

; Run loop until i == 10
rlp i, 10
sub y, 1
dec i
elp