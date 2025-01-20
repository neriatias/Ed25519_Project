import unittest
from src.ed25519 import generate_keys, sign_message, verify_signature

class TestEd25519(unittest.TestCase):
    """
    Unit tests for Ed25519 implementation.
    This class contains tests to ensure the correctness of key generation,
    message signing, and signature verification.
    """

    def test_sign_and_verify(self):
        """
        Test signing a message and verifying the signature.
        This test ensures that a valid signature can be generated and verified
        for the same message using the corresponding public key.
        """
        # Generate keys
        private_key, public_key = generate_keys()

        # Define a test message
        message = b"Test Message"

        # Sign the message
        signature = sign_message(private_key, message)

        # Verify the signature
        self.assertTrue(
            verify_signature(public_key, message, signature.signature),
            "The signature should be valid for the original message."
        )

    def test_invalid_signature(self):
        """
        Test verifying an invalid signature.
        This test ensures that if a message is tampered with, or if the wrong
        signature is used, the verification should fail.
        """
        # Generate keys
        private_key, public_key = generate_keys()

        # Define a test message and sign it
        message = b"Test Message"
        signature = sign_message(private_key, message)

        # Define a tampered message
        tampered_message = b"Tampered Message"

        # Verify the signature against the tampered message
        self.assertFalse(
            verify_signature(public_key, tampered_message, signature.signature),
            "The signature should not be valid for a tampered message."
        )

if __name__ == "__main__":
    """
    Entry point for running the unit tests.
    """
    unittest.main()
