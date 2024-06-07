block_height = int(input("Height: "))
while block_height < 1 or block_height > 8:
    block_height = int(input("try again, Height: "))
    
n = block_height - 2
if block_height >= 1 and block_height <= 8:
        for stairs in range(1, block_height):
            print(' ' * n, '#' * stairs)
            n-=1
        print('#' * block_height)
        
