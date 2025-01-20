from ed25519 import generate_keys, sign_message, verify_signature

# Demonstration process

if __name__ == "__main__":
    # Generate keys
    private_key, public_key = generate_keys()
    print("Private Key:", private_key.encode().hex())
    print("Public Key:", public_key.encode().hex())

    # Sign a message
    message = b"Hello, Ed25519!"  # Message to be signed
    signature = sign_message(private_key, message)
    print("Signature:", signature.signature.hex())

    # Verify the signature
    is_valid = verify_signature(public_key, message, signature.signature)
    if is_valid:
        print("Signature is valid!")
    else:
        print("Signature verification failed!")
