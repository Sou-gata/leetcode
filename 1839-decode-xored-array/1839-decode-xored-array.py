class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for i in range(0, len(encoded)):
            decoded.append(decoded[i] ^ encoded[i])
        return decoded