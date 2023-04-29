int money = 1000;

float time = 1004.532;

vec2 home = (10, 43);

string money_for_display = money.toString()

fn int add (int x, int y) {
    return x + y;
}

// The same as typedef
type direction_t is vec2;

// The same as a typedef struct
type house defines {
    int width -> 9;         // Default is 9
    int length -> 25;       // Default is 25
    float height -> 2.5;    // Default is 2.5
    !string name;           // ! Indicates that this parameter is required
}