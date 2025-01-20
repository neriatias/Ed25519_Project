# Import libraries
from nacl.signing import SigningKey

# 1. Key Generation
def generate_keys():
    """
    Function to generate private and public keys.
    The private key is kept secret, while the public key is used to verify signatures.
    """
    private_key = SigningKey.generate()  # Generate a private key
    public_key = private_key.verify_key  # Derive the public key
    return private_key, public_key

# 2. Signing a Message
def sign_message(private_key, message):
    """
    Function to create a digital signature for a message.
    :param private_key: Private key used for signing.
    :param message: The message to be signed.
    :return: A signature in bytes format.
    """
    signature = private_key.sign(message)  # Sign the message
    return signature

# 3. Verifying a Signature
def verify_signature(public_key, message, signature):
    """
    Function to verify a digital signature.
    :param public_key: Public key used for verification.
    :param message: The original message.
    :param signature: The signature to be verified.
    :return: True if the signature is valid, otherwise an error will be raised.
    """
    try:
        public_key.verify(message, signature)  # Verify the signature
        return True
    except Exception as e:
        return False

