import Levenshtein


def check_nick_similarity(nickName, nickNameNew):
    
    threshold = 2  # Prog odległości edycyjnej

    distance = Levenshtein.distance(nickName, nickNameNew)

    if distance <= threshold:
        return nickName
    else:
        return nickNameNew
    


print(check_nick_similarity("paweł","pawł"))