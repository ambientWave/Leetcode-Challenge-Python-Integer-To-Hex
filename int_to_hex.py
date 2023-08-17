class Solution(object): 
    def toHex(self, num): 
        """ 
        :type num: int 
        :rtype: str 
        """ 
        # if the integer doesn't have a sign i.e. positive, it can be directly converted to hex 
        if num >= 0: 
            return (hex(num)[2:]) 
        elif num < 0: 
            # first we should convert the negative integer to binary and get rid of the 0b and sign in the binary representation 
            neg_num = bin(num)[3:] 

            # then we locate the rightmost 1 bit 
            rightmost_one_index = neg_num.rindex("1", 0, len(neg_num)) 

            # we divide the whole binary string into left and right parts before and after located bit and fill on the left side of left part with zeros to make 32 bit integer 
            right_part = neg_num[rightmost_one_index:] 
            left_part = neg_num[0:rightmost_one_index].zfill(32-len(right_part)) 
             
            # we invert the bits of left part 
            left_part_inverted = ''.join(["1", "0"][int(i)] for i in left_part) 

            # we then join the two parts 
            result = left_part_inverted+right_part 

            # and finally, we convert the string into integer which is converted to hex 
            return hex(int(result, 2))[2:]