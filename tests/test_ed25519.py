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
        print("✅ Functional test: sign and verify passed!")
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
        print("✅ Tampering test: verification correctly failed on tampered message!")

    def test_invalid_key(self):
        """
        Test that verification fails when using an incorrect public key.
        """
        # Generate two different key pairs
        private_key1, public_key1 = generate_keys()
        private_key2, public_key2 = generate_keys()

        # Sign a message using the first key pair
        message = b"Testing invalid key verification"
        signature = sign_message(private_key1, message)

        # Try verifying with the second public key (should fail)
        self.assertFalse(verify_signature(public_key2, message, signature.signature),
                         "Verification should fail with an incorrect public key.")
        print("✅ Invalid key test: verification correctly failed with incorrect key!")

    def test_multiple_signatures(self):
        """
        Test signing multiple messages and verifying each independently.
        """
        # Generate keys
        private_key, public_key = generate_keys()

        # Sign multiple messages
        messages = [b"Message 1", b"Message 2", b"Message 3"]
        signatures = [sign_message(private_key, msg) for msg in messages]

        # Verify each signature
        for i in range(len(messages)):
            self.assertTrue(verify_signature(public_key, messages[i], signatures[i].signature),
                            f"Failed to verify message {i + 1}")
            print("✅ Multiple signatures test: all messages verified successfully!")


if __name__ == "__main__":
    unittest.main()
