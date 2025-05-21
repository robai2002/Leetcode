class Solution:
    def simplifyPath(self, path):
        dir_stack = []
        path = path.split("/")
        for elem in path:
            if dir_stack and elem == "..":
                dir_stack.pop()
            if elem not in [".", "", ".."]:
                dir_stack.append(elem)
                
        return "/" + "/".join(dir_stack)