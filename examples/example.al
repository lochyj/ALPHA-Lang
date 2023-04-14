int a = 0;
int b = 0;
int[] c = [a, b];   // Expandable: c += [10, 12] -> [0, 0, 10, 12]
int[2] c = [10, 10]  // Permanently 2 items long

for (int i = 0; i < 10; i++) {
    print(i);
}

fn int add (int x, int y) {
    return x + y;
}