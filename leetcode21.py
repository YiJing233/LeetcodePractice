class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_list(lnode):
            a=[]
            while(lnode != None):
                a.append(lnode.val)
                lnode = lnode.next
            return a
        def to_link_list(alist):
            node=ListNode(None)
            p=node
            for i in range(0,len(alist)):
                p.next=ListNode(alist[i])
                p=p.next
            return node.next
        return to_link_list( sorted(to_list(l1)+to_list(l2)) )


"""
转成内建的list合并后排序 再转回题目要求的单链表

链表的基本操作嘻嘻
"""