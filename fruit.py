"""
File: L12 Prepare Checkpoint
Author: Gab Yanqui
Date: 03/23/2023
Purpose: Improve your ability to write object-oriented code.
"""
def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        fruit_list.reverse()
        print(fruit_list)

        fruit_list.append("orange")
        print(fruit_list)

        i = fruit_list.index("apple")
        fruit_list.insert(i, "cherry")
        print(fruit_list)

        fruit_list.remove("banana")
        print(fruit_list)

        last = fruit_list.pop()
        print(f"pop {last}: {fruit_list}")

        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        fruit_list.clear()
        print(f"cleared: {fruit_list}")
    
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

if __name__ == "__main__":
    main()