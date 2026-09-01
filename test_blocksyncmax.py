# test_blocksyncmax.py
"""
Tests for BlockSyncMax module.
"""

import unittest
from blocksyncmax import BlockSyncMax

class TestBlockSyncMax(unittest.TestCase):
    """Test cases for BlockSyncMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockSyncMax()
        self.assertIsInstance(instance, BlockSyncMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockSyncMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
