print('Content-Type: text/html')

#positional formating

print('안녕? {}, 잘 지내고 있니?\n이 편지는 영국에서 시작되어 {}님에게 전송되었습니다.'.format('정원아', 18))

print("\"이것은\" '무엇'입니까?\n\n\n\n\n")


#Named placeholder

print('안녕? {name}, 잘 지내고 있니?\n이 편지는 영국에서 시작되어 {nickname:d}님에게 전송되었습니다.'.format(name='호롤롤', nickname=12))

print("\"이것은\" '무엇'입니까?")
