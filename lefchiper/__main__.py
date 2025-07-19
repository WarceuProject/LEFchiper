import argparse
import sys
from lefchiper.core import glasicc, lefchaos, lefkey

MODES = {
    "glasicc": {
        "encrypt": glasicc.glasicc_encrypt,
        "decrypt": glasicc.glasicc_decrypt,
        "require_key": False
    },
    "lefchaos": {
        "encrypt": lefchaos.chaos_encrypt,
        "decrypt": lefchaos.chaos_decrypt,
        "require_key": True
    },
}

def main():
    parser = argparse.ArgumentParser(description="LEFCHIPER - Modular Encrypt/Decrypt CLI")
    parser.add_argument("-e", "--encode", help="Teks yang ingin dienkripsi")
    parser.add_argument("-d", "--decode", help="Teks yang ingin didekripsi")
    parser.add_argument("-m", "--modes", nargs="+", help="Daftar mode yang ingin digunakan (urutan penting)")
    parser.add_argument("-k", "--key", help="Kunci enkripsi (untuk mode yang memerlukan)")
    parser.add_argument("--genkey", action="store_true", help="Generate kunci secara acak")

    args = parser.parse_args()

    if args.genkey:
        print("[+] Generated Key:", lefkey.generate_key())
        sys.exit(0)

    if not args.modes:
        print("[!] Harus menyertakan setidaknya satu mode (-m)")
        sys.exit(1)

    if not (args.encode or args.decode):
        print("[!] Harus menyertakan teks untuk encode (-e) atau decode (-d)")
        sys.exit(1)

    text = args.encode or args.decode
    is_encoding = args.encode is not None

    # Jalankan proses encode/decode secara berurutan
    for mode in args.modes:
        if mode not in MODES:
            print(f"[!] Mode '{mode}' tidak dikenali.")
            sys.exit(1)

        func = MODES[mode]["encrypt"] if is_encoding else MODES[mode]["decrypt"]
        need_key = MODES[mode]["require_key"]

        if need_key and not args.key:
            print(f"[!] Mode '{mode}' membutuhkan kunci (-k)")
            sys.exit(1)

        if need_key:
            text = func(text, args.key)
        else:
            text = func(text)

    print(f"[✓] Hasil {'enkripsi' if is_encoding else 'dekripsi'}:")
    print(text)

if __name__ == "__main__":
    main()
