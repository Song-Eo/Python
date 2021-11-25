from Python.Data_structure.ADT_LinkedStructure import LinkedList

                    """def merge(self, listB):
                        if (type(listB) == type(self)):
                            while not listB.isEmpty():
                                self.insert(self.size(), listB.getEntry(0))
                                listB.delete(0)
                        else:
                            return False"""
ll1 = LinkedList()
ll2 = LinkedList()

ll1.insert(0, 4)
ll1.insert(0, 2)
ll1.insert(0, 3)
ll1.insert(0, 1)
ll2.insert(0, 2)
ll2.insert(0, 10)
ll2.insert(0, 8)
ll2.insert(0, 6)
ll1.display()
ll2.display()
ll1.merge(ll2)
ll1.display()
ll2.display()


