class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']
        """
        maxLen = 0
        hierarchy = {-1: 0}
        for line in input.split('\n'):
            level = line.count('\t')
            name = line.strip('\t')
            if '.' in name:
                maxLen = max(maxLen, hierarchy[level - 1] + len(name) + level)
            else:
                hierarchy[level] = hierarchy[level - 1] + len(name)
        return maxLen

def main():
    input = "dir\n\t        file.txt\n\tfile2.txt"
    print(input.split('\n'))
    s = Solution()
    print(s.lengthLongestPath(input))

if __name__ == '__main__':
    main()