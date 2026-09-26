__all__ = ['HafumanTree']
class _hlp:
    def __init__(self,value,weight,index,father = None,is_base = False):
        self.value = value
        self.weight = weight
        self.index = index
        self.father = father
        self.is_base = is_base
        self.left = None
        self.right = None
        self.code = ''
class HafumanTree:
    def __init__(self,values,weights):
        # 创建叶子节点
        nodes = [_hlp(values[i],weights[i],i,None,True) for i in range(len(values))]
        while len(nodes) > 1:
            # 按权重升序排列
            nodes.sort(key = lambda x:x.weight)
            left = nodes.pop(0)
            right = nodes.pop(0)
            # 创建父节点
            parent = _hlp(None,left.weight + right.weight,-1,None,False)
            parent.left = left
            parent.right = right
            left.father = parent
            right.father = parent
            nodes.append(parent)
        self.root = nodes[0]
        self._generate_codes(self.root,'')
    def _generate_codes(self,node,code):
        if node.left is None and node.right is None:
            node.code = code
            return
        if node.left:
            self._generate_codes(node.left,code + '0')
        if node.right:
            self._generate_codes(node.right,code + '1')
    def get_code_dict(self):
        """返回 值 → 编码 的字典"""
        result = {}
        self._collect_codes(self.root,'',result)
        return result
    def _collect_codes(self,node,code,result):
        if node.left is None and node.right is None:
            result[node.value] = code
            return
        if node.left:
            self._collect_codes(node.left,code + '0',result)
        if node.right:
            self._collect_codes(node.right,code + '1',result)

if __name__ == '__main__':
    values = ['a','b','c','d']
    weights = [10,5,8,12]
    tree = HafumanTree(values, weights)
    code_dict = tree.get_code_dict()
    print(code_dict)