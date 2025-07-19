import argparse
#from .core.lefchaos import chaos_encrypt, chaos_decrypt

def main():
    parser = argparse.ArgumentParser(description="LEFchiper - Chaos Encrypt/Decrypt Tool")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", help="Teks yang ingin dienkripsi")
    group.add_argument("-d", "--decrypt", help="Teks yang ingin didekripsi")
    
    parser.add_argument("-k", "--key", required=True, help="Kunci enkripsi/dekripsi")

    args = parser.parse_args()

    #if args.encrypt:
    #    result = chaos_encrypt(args.encrypt, args.key)
    #    print(f"Ciphertext: {result}")
    #elif args.decrypt:
    #    result = chaos_decrypt(args.decrypt, args.key)
    #    print(f"Plaintext: {result}")

if __name__ == "__main__":
    main()
