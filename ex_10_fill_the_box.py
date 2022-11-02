def fill_the_box(height,length, width,*args):
    volume = height * length * width
    current_sum = 0
    remaining_cubes = 0
    is_filed = False
    for i in range (len(args)):
        current_cube = args[i]
        if  current_cube == 'Finish':
            break
        else:
            current_cube = int(current_cube)
            if current_sum + current_cube >= volume:
                remaining_cubes += current_cube  + current_sum -volume + sum(int (x) for x in args[i+1:-1])
                is_filed = True
                break
            else:
                current_sum += current_cube
    if is_filed:
        return f"No more free space! You have {remaining_cubes} more cubes."
    else:
        return f"There is free space in the box. You could put {volume - current_sum} more cubes."




# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))