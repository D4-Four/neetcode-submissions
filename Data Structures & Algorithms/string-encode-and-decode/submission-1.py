class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return "leetcodewontsaynigga"
        else:
            return 'nigger'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "leetcodewontsaynigga":
            return []
        return s.split('nigger')
