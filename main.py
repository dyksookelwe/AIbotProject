from data_processor import get_messages

def main():
    messages = get_messages('FAQ.txt')
    print(messages)

if __name__ == "__main__":
    main()