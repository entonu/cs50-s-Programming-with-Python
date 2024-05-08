def main():
    mog=convert(input("enter some text "))
    print(mog)
def convert(text):
    if text==":)":
        return"🙂"
    elif text==":(":
        return "🙁"
    else:
        return text
main()