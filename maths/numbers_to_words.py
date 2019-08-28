def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
            'Nineteen']
    tens1 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def interpretNumber(num):
        if num < 10:  # 0 - 9
            return units[num]
        elif num < 20:  # 10 - 19
            return tens[num - 10]
        elif num < 100:  # 20 - 99
            div, mod = divmod(num, 10)
            if mod != 0:
                return tens1[div - 2] + " " + interpretNumber(mod)
            return tens1[div - 2]
        elif num < 1000:  # 100 - 999
            div, mod = divmod(num, 100)
            if mod != 0:
                return interpretNumber(div) + " Hundred " + interpretNumber(mod)
            return interpretNumber(div) + " Hundred"
        elif num < 1000000:  # 1,000 - 999,999
            div, mod = divmod(num, 1000)
            if mod != 0:
                return interpretNumber(div) + " Thousand " + interpretNumber(mod)
            return interpretNumber(div) + " Thousand"
        elif num < 1000000000:  # 1,000,000 - 999,999,999
            div, mod = divmod(num, 1000000)
            if mod != 0:
                return interpretNumber(div) + " Million " + interpretNumber(mod)
            return interpretNumber(div) + " Million"
        else:
            div, mod = divmod(num, 1000000000)
            if mod != 0:
                return interpretNumber(div) + " Billion " + interpretNumber(mod)
            return interpretNumber(div) + " Billion"

    return interpretNumber(num)


print(numberToWords(210))
print(numberToWords(123))
print(numberToWords(120))
print(numberToWords(1023))
print(numberToWords(5467))
print(numberToWords(75467))
print(numberToWords(175467))
print(numberToWords(1975467))
