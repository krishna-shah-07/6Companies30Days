class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.family_tree = {}
        self.deceased = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.family_tree:
            self.family_tree[parentName] = []
        self.family_tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deceased.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(person):
            if person not in self.deceased:
                yield person
            if person in self.family_tree:
                for child in self.family_tree[person]:
                    yield from dfs(child)

        return list(dfs(self.kingName))


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
