from data_processor import get_messages

def main():
    messages = get_messages('result')

    with open('parsed_messages.txt', 'w', encoding='utf-8') as f:
        for msg in messages:
            f.write(msg + '\n')
    print(f"There is {len(messages)} strings.")

if __name__ == "__main__":
    main()