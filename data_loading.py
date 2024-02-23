
#load dataset in

def load_data():
    
    texts,labels = [], []
    
    with open("./SMSSpamCollection") as file:
        for each_line in file:
            split = each_line.split()
            labels.append(split[0].strip())
            texts.append(' '.join(split[1:]).strip())
    return texts, labels        
    
            