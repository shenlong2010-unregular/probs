class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

# test = BST(100)
# test.insert(10)
# test.insert(5)
# test.insert(15)
# test.insert(2)
# test.insert(5)
# test.insert(13)
# test.insert(22)
# test.insert(1)
# test.insert(14)

test = (
    BST(100)
    .insert(5)
    .insert(15)
    .insert(5)
    .insert(2)
    .insert(1)
    .insert(22)
    .insert(1)
    .insert(1)
    .insert(3)
    .insert(1)
    .insert(1)
    .insert(502)
    .insert(55000)
    .insert(204)
    .insert(205)
    .insert(207)
    .insert(206)
    .insert(208)
    .insert(203)
    .insert(-51)
    .insert(-403)
    .insert(1001)
    .insert(57)
    .insert(60)
    .insert(4500)
)
# Aveage case: O(log(N)) T | O(log(N)) S
# Worst case: O(N) T | O(N) S : this happens when it only has 1 branch
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

# Aveage case: O(log(N)) T | O(1) S
# Worst case: O(N) T | O(1) S : this happens when it only has 1 branch
def findClosestValueInBst1(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBstHelper1(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
print(findClosestValueInBst(test, 12))
print(findClosestValueInBst(test, 500))
print(findClosestValueInBst1(test, -50))
