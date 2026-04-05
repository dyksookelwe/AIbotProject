import AIconfig
from data_processor import get_messages

def main():
    messages = get_messages(AIconfig.FAQ_FILE)
    print(messages)

if __name__ == "__main__":
    main()