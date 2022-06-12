import win32clipboard as clip
from secrets import token_urlsafe


def set_clip(password):
    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(f"{password}")
    clip.CloseClipboard()


def generate_password():
    password = token_urlsafe(20)
    return password


def main():
    password = generate_password()
    set_clip(f"{password}")


if __name__ == "__main__":
    main()
