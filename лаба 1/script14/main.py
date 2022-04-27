# Напишите декоратор non_empty, который дополнительно проверяет
# списковый результат любой функции: если в нем содержатся пустые
# строки или значение None, то они удаляются. Пример кода:
# @non_empty
# def get_pages():
# return ['chapter1', '', 'contents', '', 'line1']

# Декораторы – это языковое средство Python, позволяющее динамически
# модифицировать поведение уже существующей функции.
# non_empty - Декоратор
def non_empty(func):
    
    def _wrapper():         
        print(list(filter(None, func())))

    # декоратор возвращает функцию (callable)
    return _wrapper


# декорируем функцию
@non_empty
def get_pages():
    return ['chapter1', '', 'contents', '', 'line1', None]

    
get_pages()
