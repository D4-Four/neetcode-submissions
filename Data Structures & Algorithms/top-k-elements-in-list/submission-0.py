class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashnum = {}
        for n in  nums:
            if n in hashnum:
                hashnum[n] += 1
            else:
                hashnum[n] = 1
        #sort hashmap by frequency from big to low
        output_list = []
        sorted_desc = sorted(hashnum.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            output_list.append(sorted_desc[i][0])
        return output_list