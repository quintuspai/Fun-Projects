
def luhn_checker(card_no):
    card = [int(i) for i in card_no]
    checksum = card.pop()
    card.reverse()
    for i in range(0,len(card),2):
        card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
    check = sum(card)+checksum
    return "Valid card no." if (check % 10 == 0) else "Invalid card no."

#'4539313679610252633'
card_no = str(input("Enter a card no. to check : "))
print(luhn_checker(card_no))