development_bytes = 'разработка'.encode('utf-8')
socket_bytes = 'сокет'.encode('utf-8')
decorator_bytes = 'декоратор'.encode('utf-8')

print(development_bytes)
print(socket_bytes)
print(decorator_bytes)

development_str = development_bytes.decode('utf-8')
print(development_str)
socket_str = socket_bytes.decode('utf-8')
print(socket_str)
decorator_str = decorator_bytes.decode('utf-8')
print(decorator_str)

#development_latin = development_str.encode('latin-1')
#print(development_latin)
#русский язык нельзя кодировать под latin-1