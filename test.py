# fn int add(x,y) x + y;
line = "fn int add(x,y) x + y;"
split_line = line.split(' ');

fn_name = split_line[2].replace('(', ' ').split(' ')[0];

print(fn_name);