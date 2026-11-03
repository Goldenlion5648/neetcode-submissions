class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "###"
        return "|||".join("~@~" + word + "~!~" for word in strs)

    def decode(self, s: str) -> List[str]:
        if s == "###":
            return []
        ret = s.split("|||")
        return [word.removeprefix("~@~").removesuffix("~!~") for word in ret]
