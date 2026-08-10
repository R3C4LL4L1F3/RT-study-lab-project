import unittest
from tools.ai_harness.canonical import canonical_bytes, sha256_hex

class CanonicalizationTests(unittest.TestCase):
    def test_key_order(self): self.assertEqual(canonical_bytes({'b':1,'a':2}),b'{"a":2,"b":1}')
    def test_timestamp_utc(self): self.assertEqual(canonical_bytes({'classified_at':'2026-08-10T15:00:00-04:00'}),b'{"classified_at":"2026-08-10T19:00:00Z"}')
    def test_semantic_change_hash(self): self.assertNotEqual(sha256_hex({'a':1}),sha256_hex({'a':2}))
if __name__=='__main__': unittest.main()
