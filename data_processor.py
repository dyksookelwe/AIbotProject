def get_messages(filename):
    prepared_text = []
    with open(filename, 'r', encoding='utf-8') as f:
        question = None
        answer = []
        for line in f:
            line = line.strip()
            if "В: " in line:
                if question and answer:
                    full_answer = " ".join(answer)
                    prepared_text.append(f"{question}, {answer}")
                
                question = line.split("В: ")[1].strip()
                answer = []
            elif "О: " in line:
                answer_line = line.split("О: ")[1].strip()
                answer.append(answer_line)

            elif answer:
                answer.append(line)

            if question and answer:
                full_answer = " ".join(answer)
                prepared_text.append(f"{question}, {full_answer}")
    return prepared_text

