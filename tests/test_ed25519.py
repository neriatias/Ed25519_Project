import unittest
from src.ed25519 import generate_keys, sign_message, verify_signature




class TestEd25519(unittest.TestCase):

    def test_sign_and_verify(self):
        """
        Test that a message signed with the private key is successfully verified
        with the corresponding public key.
        """
        # Generate keys
        private_key, public_key = generate_keys()

        # Message to sign
        message = b"Functional Test Message"

        # Sign the message
        signature = sign_message(private_key, message)

        # Verify the signature
        assert verify_signature(public_key, message, signature.signature), "Failed to verify the signature."
        print("Functional test: sign and verify passed!")
    def test_tampered_message(self):
        """
        Test that signature verification fails if the message is tampered with.
        """
        # Generate keys
        private_key, public_key = generate_keys()

        # Original message
        original_message = b"Original Message"

        # Tampered message
        tampered_message = b"Tampered Message"

        # Sign the original message
        signature = sign_message(private_key, original_message)

        # Verify the tampered message (should fail)
        self.assertFalse(verify_signature(public_key, tampered_message, signature.signature),
                         "Tampered message should not verify!")


if __name__ == "__main__":
    unittest.main()
