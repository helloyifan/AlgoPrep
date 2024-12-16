'''
Notes:
Pseudo-code for LCA with nulls

## Base Case:
If the current node is null, return (null, false, false).

## Search Left and Right:
Recursively find the LCA in the left and right subtrees.

## Current Node Check:

If the current node is p or q, mark it as found.

LCA Conditions:
If both sides return an LCA, the current node is the LCA.

If the current node matches p or q and the other node is found in a subtree, the current node is the LCA.

Propagate Results:

Return the LCA from the left or right subtree if it exists.

## Final Step:
At the root, if both p and q are found, return the LCA. Otherwise, return null.
'''
