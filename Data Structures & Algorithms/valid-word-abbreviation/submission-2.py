class Solution:
    def validWordAbbreviation(self, normal: str, encoded: str) -> bool:
        pos1 = 0
        pos2 = 0
        while pos1 < len(normal) and pos2 < len(encoded):
            cur_num = 0
            had_num = False
            while pos2 < len(encoded) and encoded[pos2].isdigit():
                if cur_num == 0 and encoded[pos2] == '0':
                    return False
                cur_num = cur_num * 10 + int(encoded[pos2])
                pos2 += 1
                had_num = True
            
            
            if had_num:
                pos1 += cur_num
                if pos1 == len(normal) and pos2 == len(encoded):
                    return True
                if pos1 < len(normal) and pos2 < len(encoded):
                    #both are alphabetical
                    if normal[pos1] != encoded[pos2]:
                        return False
                else:
                    if (pos1 == len(normal)) != (pos2 == len(encoded)):
                        return False
                    
            else:
                #we can advance both pointers normally
                if normal[pos1] != encoded[pos2]:
                    return False
            pos1 += 1
            pos2 += 1

        return pos1 == len(normal) and pos2 == len(encoded) 