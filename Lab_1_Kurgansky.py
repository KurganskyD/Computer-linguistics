import re

def step1(text):
    ListWithSentenceCharacteristic =[[],[]]
    SentenceStartPos = re.search('\S', text).start()
    step2(SentenceStartPos, text, ListWithSentenceCharacteristic)
    
# Шаг 2 Находим в тексте первую последовательность завершающих симвлов (SentenceEndSeq), следующую за SentenceStartPos 
def step2(SentenceStartPos, text, ListWithSentenceCharacteristic): 
    SentenceEndSeq='\?{1,}|\!{1,}|\.{1,}'
    print('text for end:', text)
    # Если такая последовательность найдена, запоминаем её позицию и переходим к следующему шагу
    print('SentenceStartPos', SentenceStartPos)
    if re.search(SentenceEndSeq, text):
        print(re.search(SentenceEndSeq, text).group())
        SentenceEndSeqStartPos = re.search(SentenceEndSeq, text).start()
        SentenceEndSeqEndPos = re.search(SentenceEndSeq, text).end()
        print('start ',SentenceEndSeqStartPos)
        print('end',SentenceEndSeqEndPos)
        
        string = " " * SentenceEndSeqEndPos
        text=text.replace(text[:SentenceEndSeqEndPos],string,1)
        
        print('text posle obrez', text)
        step3(SentenceStartPos, SentenceEndSeqEndPos, text, ListWithSentenceCharacteristic)   
    else:
        # Если такая последовательность не найдена, и в процессе поиска достигнут конец файла, 
        # то присваиваем метку конца предложения последнему символу в тексте и переходим к шагу 5
        ListWithSentenceCharacteristic[0].append(SentenceStartPos)
        ListWithSentenceCharacteristic[1].append(len(text))
        print('konec')
        step5(ListWithSentenceCharacteristic)
        
def step3(SentenceStartPos, SentenceEndSeqEndPos, text, ListWithSentenceCharacteristic):
    # После нахождения последовательности SentenceEndSeq ищем первый не пробельный символ, следующий за SentenceEndSeq
    if re.search('\S', text):
        print('k', re.search('\S', text).group())
        # Если следующий за SentenceEndSeq не пробельный символ является заглавной буквой, то найден предположительный конец 
        # предложения, снова переходим к шагу 2
        if re.search('[А-Я]', re.search('\S', text).group()):
            print('zaglav', re.search('[А-Я]', re.search('\S', text).group()).group())

            ListWithSentenceCharacteristic[0].append(SentenceStartPos)
            ListWithSentenceCharacteristic[1].append(SentenceEndSeqEndPos)
            print('SentenceEndSeqEndPos', SentenceEndSeqEndPos)
            step2(SentenceEndSeqEndPos, text, ListWithSentenceCharacteristic)
        else:
        # иначе переходим к шагу 2 и начинаем искать следующую последовательность SentenceEndSeq
            step2(SentenceStartPos, text, ListWithSentenceCharacteristic)
    
    # Если в процессе поиска достигнут конец файла, то присваиваем метку SentenceEndPos последнему символу из SentenceEndSeq 
    # и переходим к шагу 5
    else:
        print(len(text))
        ListWithSentenceCharacteristic[0].append(SentenceStartPos)
        ListWithSentenceCharacteristic[1].append(len(text))
        #SentenceEndPos = SentenceEndSeqEndPos
        print('Posle ! net symbolov')
        #ListWithSentenceCharacteristic[1].append(SentenceEndSeqEndPos)
        step5(ListWithSentenceCharacteristic)
        
def step5(ListWithSentenceCharacteristic):
    print(ListWithSentenceCharacteristic)

text = 'Привет как дела! Чем занимаешься. Что ты делаешь.' 
step1(text)