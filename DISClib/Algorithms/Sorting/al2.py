# Python code to implement the above approach

# Function to merge piles in a sorted order
def merge_piles(v):
    # Store minimum element from the top of stack
    ans = []

    # In every iteration find the smallest element
    # of top of pile and remove it from the piles
    # and store into the final array
    while True:
        # Stores the smallest element of the top of the piles
        minu = float("inf")

        # Stores index of the smallest element of the top of the piles
        index = -1

        # Calculate the smallest element of the top of the every stack
        for i in range(len(v)):
            # If minu is greater than the top of the current stack
            if minu > v[i][-1]:
                # Update minu
                minu = v[i][-1]

                # Update index
                index = i

        # Insert the smallest element of the top of the stack
        ans.append(minu)

        # Remove the top element from the current pile
        v[index].pop()

        # If current pile is empty
        if not v[index]:
            # Remove current pile from all piles
            v.pop(index)

        # If all the piles are empty
        if not v:
            break

    return ans

# Function to sort the given array using the patience sorting


def patienceSorting(arr):
    # Store all the created piles
    piles = []

    # Traverse the array
    for i in range(len(arr)):
        # If no piles are created
        if not piles:
            # Initialize a new pile
            temp = []
            # Insert current element into the pile
            temp.append(arr[i])

            # Insert current pile into all the piles
            piles.append(temp)
        else:
            # Check if top element of each pile is less than or equal to
            # current element or not
            flag = True

            # Traverse all the piles
            for j in range(len(piles)):
                # Check if the element to be inserted is less than
                # current pile's top
                if arr[i] < piles[j][-1]:
                    piles[j].append(arr[i])

                    # Update flag
                    flag = False
                    break

            # If flag is True
            if flag:
                # Create a new pile
                temp = []

                # Insert current element into temp
                temp.append(arr[i])

                # Insert current pile into all the piles
                piles.append(temp)

    # Store the sorted sequence of the given array
    ans = []

    # Sort the given array
    ans = merge_piles(piles)

    return ans


# Driver code
arr = [6, 12, 2, 8, 3, 7]

# Function call
print(patienceSorting(arr))
