"""Chatbot paling dasar untuk latihan membuat AI agent."""


def buat_balasan(pesan: str) -> str:
    """Balasan contoh; ganti fungsi ini dengan panggilan ke model AI."""
    # TODO: sambungkan ke model AI setelah memahami alur program ini.
    # Untuk sekarang, kita hanya mengulang pesan pengguna.
    return f"Kamu bilang: {pesan}"


def main() -> None:
    # TODO: tambahkan penanganan error dan riwayat percakapan.
    print("Chatbot sederhana. Ketik 'keluar' untuk berhenti.")

    while True:
        pesan = input("Kamu: ").strip()
        if pesan.lower() == "keluar":
            print("Bot: Sampai jumpa!")
            break
        if not pesan:
            continue
        print(f"Bot: {buat_balasan(pesan)}")


if __name__ == "__main__":
    main()
