# leetcode
This repository contains solutions to a set of problems from https://leetcode.com (highly recommended for interview preperation).

There are quite a few repositories available already that are more exhaustive, plus the discuss forum in leetcode is excellent too (go check them out!). This particular repository **serves a different purpose** -- it takes each problem as if posed by an interviewer, and very briefly chalks out the possible questions the interviewee should ask, the early comments one may make about their approach, and a very mediocre solution. Mostly easy and medium level problems are addressed. Please note that this should provide an interview prep suggestions, not the cool or even the most efficient solution.

## Assumptions
Some basic data structure initiations may be pressumed and is listed below for references.

A binary tree node is initiated as follows:

```
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

A linked list node is initiated as follows:

```
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
```

## Issues
- A small number of solutions may give a timeout in leetcode online judge.
- Some solutions may have misplaced ```self```, because the solutions were checked by the leetcode OJ first.

## Disclaimers
- A small number of problems may be influenced by solutions from elsewhere (such as discuss forum), but due credit is given in such case.
- This list of problems is neither exclusive nor exhaustive.
- This repository does not contain another important part of tech interviews, system design problems.
