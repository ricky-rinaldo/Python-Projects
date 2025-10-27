import requests
from urllib.parse import quote


def check_username_availability(username):
    """
    Mengecek ketersediaan username di berbagai platform
    """
    results = {}

    # Headers untuk menghindari blokir
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Template URL untuk setiap platform
    platforms = {
        'gmail': f'https://mail.google.com/mail/gxlu?email={username}@gmail.com',
        'youtube': f'https://www.youtube.com/@{username}',
        'tiktok': f'https://www.tiktok.com/@{username}',
        'facebook': f'https://www.facebook.com/{username}'
    }

    for platform, url in platforms.items():
        try:
            if platform == 'gmail':
                response = requests.get(url, headers=headers, timeout=10)
                # Jika tidak ada redirect, kemungkinan email tersedia
                results[platform] = "Tersedia" if len(response.history) == 0 else "Terpakai"
            else:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 404:
                    results[platform] = "Tersedia"
                elif response.status_code == 200:
                    results[platform] = "Terpakai"
                else:
                    results[platform] = "Tidak dapat dicek"
        except Exception as e:
            results[platform] = f"Error: {str(e)}"

    return results


def main():
    usernames = ['beranibersuara', 'politikbersuara', 'beraniberpolitik']

    print("Mengecek ketersediaan username...")
    print("=" * 60)

    for username in usernames:
        print(f"\nHasil untuk: {username}")
        print("-" * 30)

        results = check_username_availability(username)

        for platform, status in results.items():
            print(f"{platform.capitalize():<10}: {status}")

        print("-" * 30)


if __name__ == "__main__":
    main()