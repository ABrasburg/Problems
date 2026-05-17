# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked, which returns whether the node is locked
# lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
# unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

class LockingBinaryTreeNode(object):
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.locked_descendants_count = 0

    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False

        cur = self.parent
        while cur:
            if cur.locked:
                return False
            cur = cur.parent
        return True

    def is_locked(self):
        return self.locked


    def lock(self):
        if self.locked:
            return False # node already locked

        if not self._can_lock_or_unlock():
            return False

        # Not locked, so update locked and increment count in all ancestors
        self.locked = True

        cur = self.parent
        while cur:
            cur.locked_descendants_count += 1
            cur = cur.parent
        return True

    def unlock(self):
        if not self.locked:
            return False # node already unlocked

        if not self._can_lock_or_unlock():
            return False

        self.locked = False

        # Update count in all ancestors
        cur = self.parent
        while cur:
            cur.locked_descendants_count -= 1
            cur = cur.parent
        return True
