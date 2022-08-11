import translate
import googletrans

def main():
    text = "Hi,How are you?"
    print(googletrans.LANGCODES)
    language = input("Select a Language from a options: ")
    translate1 = translate.Translate(text,language)
    print(translate1.get_translate())


if __name__ == '__main__':
    main()
