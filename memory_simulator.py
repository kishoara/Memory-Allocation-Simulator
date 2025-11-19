# Memory Allocation Simulator
# Algorithms: First Fit, Best Fit, Worst Fit

class Block:
    def __init__(self, size, id=None):
        self.size = size
        self.id = id    # process ID occupying the block

def first_fit(blocks, process_size, pid):
    for block in blocks:
        if block.id is None and block.size >= process_size:
            block.id = pid
            return True
    return False

def best_fit(blocks, process_size, pid):
    best_index = -1
    best_size = float("inf")

    for i, block in enumerate(blocks):
        if block.id is None and block.size >= process_size and block.size < best_size:
            best_size = block.size
            best_index = i

    if best_index != -1:
        blocks[best_index].id = pid
        return True
    return False

def worst_fit(blocks, process_size, pid):
    worst_index = -1
    worst_size = -1

    for i, block in enumerate(blocks):
        if block.id is None and block.size >= process_size and block.size > worst_size:
            worst_size = block.size
            worst_index = i

    if worst_index != -1:
        blocks[worst_index].id = pid
        return True
    return False

def display(blocks):
    print("\nCurrent Memory Allocation:")
    print("-" * 40)
    print("Block\tSize\tStatus")
    print("-" * 40)
    for i, block in enumerate(blocks):
        status = f"Occupied by P{block.id}" if block.id else "Free"
        print(f"{i+1}\t{block.size}\t{status}")
    print("-" * 40)

def main():
    blocks = [Block(100), Block(500), Block(200), Block(300), Block(600)]
    
    print("\nMemory Allocation Simulator")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")
    choice = int(input("Choose algorithm: "))

    process_size = int(input("Enter process size: "))
    pid = 1  # Process ID

    if choice == 1:
        allocated = first_fit(blocks, process_size, pid)
    elif choice == 2:
        allocated = best_fit(blocks, process_size, pid)
    elif choice == 3:
        allocated = worst_fit(blocks, process_size, pid)
    else:
        print("Invalid choice!")
        return

    if allocated:
        print(f"\nProcess P{pid} allocated successfully!")
    else:
        print("\nAllocation failed: Not enough space.")

    display(blocks)

if __name__ == "__main__":
    main()
