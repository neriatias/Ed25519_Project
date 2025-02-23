# Ed25519 Digital Signature Implementation

## **Project Overview**
This project implements the Ed25519 digital signature scheme. The Ed25519 algorithm is widely used for cryptographic operations, including secure message signing and verification. It is efficient, secure, and provides high performance.

### **Features**
- **Key Generation**: Generate public and private key pairs.
- **Message Signing**: Sign messages using the private key.
- **Message Verification**: Verify the signed messages using the public key.
- **Unit Tests**: Functional tests to ensure correctness of the implementation.

---

## **Prerequisites**
To run this project, you will need:
1. **Python 3.8 or higher** installed on your machine.
2. The following Python libraries installed:
   - `pynacl`

You can install the required library using:
```bash
pip install pynacl
```
## **How to Run the Program** ##
1. Clone the repository or download the project files to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. To run the program, ensure you have the proper Python environment activated.
Run the program using:
```bash
python main.py
```

## **How to Run the Tests** ##
Ensure you are in the project directory.

Make sure the unittest module is installed (it is included by default with Python).

Run the tests using:

``` bash
python -m unittest tests/test_ed25519.py
```

You should see output similar to:

``` bash
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```
