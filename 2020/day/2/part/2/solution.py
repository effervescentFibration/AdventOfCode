
def valid_password(char, first, second, password):
    return (
        (password[first - 1] == char) ^
        (password[second - 1] == char)
    )

valid_passwords = 0
with open("input") as f:
    for l in f:
        lower = None
        higher = None
        char = None
        hyphen_i = None
        colon_i = None
        word_i = None
        for i in range(len(l)):
            if l[i] == "-":
                lower = int(l[0:i])
                hyphen_i = i
            elif l[i] == " ":
                if colon_i:
                    word_i = i + 1
                else:
                    higher = int(l[(hyphen_i + 1):i])
            elif l[i] == ":":
                char = l[i - 1]
                colon_i = i
            elif len(l) - 1 == i:
                password = l[word_i:(i)]
        if valid_password(char, higher, lower, password):
            valid_passwords += 1
        '''
        print(
            "\"{}\" must occur between {} and {} times in password \"{}\"".format(
                char, lower, higher, password
            )
        )
        '''
print(valid_passwords)
