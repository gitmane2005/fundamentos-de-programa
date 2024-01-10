def mail_merge(names, mail_template):
    result = []
    with open(names) as f_names, open(mail_template) as f_mail_template:
        list_name = f_names.readlines()
        for name in list_name:
            template = ((f_mail_template.read()).split()).copy()
            for word in template:
                if "<name>" in word:
                    s = template[template.index(word)][len(word)-1:]
                    template[template.index(word)] = name + s
            result.append(" ".join(template))
    return result


print(mail_merge("shakespeare.txt", "monty.txt"))