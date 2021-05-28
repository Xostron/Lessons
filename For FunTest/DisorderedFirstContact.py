import sys
import math

n = int(input())
numbConv = abs(n)
message = input()
print('INIT: ', n, message, "\n", len(message))

s = y = len(message)
xk = 0
while y >= 0:
    xk += 1
    y = s - (1 + xk) * xk / 2
print(xk)
combi = ''
answer = ''
while numbConv > 0:
    if n < 0:  # encode
        for i in range(1, xk + 1):
            if i % 2 > 0:  # нечетные
                combi = combi + message[:i]
                message = message[i:]
                print(f"{i} нечетные: combi = {combi}, message = {message}")
            else:  # четные
                combi = message[:i] + combi
                message = message[i:]
                print(f"{i} четные: combi = {combi}, message = {message}")

    if n > 0:  # decode
        for i in range(xk, 0, -1):
            if i % 2 == 0:
                if int(s - (1 + i) * i / 2) < 0:
                    j = int(s - (1 + (i - 1)) * (i - 1) / 2)
                    i = j
                combi = message[:i] + combi
                message = message[i:]
                print(f"{i} четные: combi = {combi}, message = {message}")
            else:
                if int(s - (1 + i) * i / 2) < 0:
                    j = int(s - (1 + (i - 1)) * (i - 1) / 2)
                    i = j
                k = len(message)
                combi = message[k - i:] + combi
                message = message[:k - i]
                print(f"{i} нечетные: combi = {combi}, message = {message}")

    numbConv -= 1
    message = combi
    answer = combi
    combi = ''
    print(f"{numbConv}=================")

print(answer)

"""
-1
abcdefghij

1
ghibcadef

-6
hello worlds

5
hitoeplmu eneicldts aide  tsxt 


3
 rius lorem. Duis risus nunc, condimentum at metun lacinia id. Pellentebortis. Suspendttis sed , maxis ornare nipulvinar. In v aliquam erat maximus bibenetus neque, tempus lovarius ipsnare vel. Donec , vitae sx enim. Sed vitaes sed nei ipFusces t. e at sum. Alt nibhgittidisse eu eteger id cursumque vel dui et libs.Maecenash. Suspendisse tristiqueeu condcondimentum atec orDui sitipsuorLem m dolteger quismus eget i ssim lacuss. Suspum feron arcu idvinar id eula elit in effiuspenlor. in blandem solm ne i psuc lorlicitudit ut acSIn luctus vcitur vae pulat arcu ferment maximus. Integerendisse hendrim. Inmentum nibh non dum.  amet, tur adlit. Fusceci pretium iacsi ut felibm neque, quis dignis orligsx nec sagi aliquam do maximuaodo nulla. isi quis, iquam esdu, npretium comMauris as. Ins elitque a mattittis. Morbi volutpat eroegestas irit vel ante ac dignisss nes scing elitconsecteoripi. Quisque msagiel puruuli mollis n enim est, ac bibendumissmentum. Ut dictum mi vel luctus rhoncus.tempor id.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque metus neque, sagittis sed condimentum at, maximus eget elit. Fusce condimentum nibh non erat maximus bibendum. Duis ornare nisi ut felis aliquam pulvinar. In vel purus nec orci pretium iaculis. Suspendisse hendrerit vel ante ac dignissim. Integer quis mollis nibh. Suspendisse tristique enim est, ac bibendum metus ornare vel. Donec egestas non arcu id maximus. Integer varius ipsum neque, quis dignissim lacus lacinia id. Pellentesque vel dui et libero tempus lobortis. Suspendisse pulvinar id ex nec sagittis. Morbi volutpat ligula at arcu fermentum fermentum. Ut maximus sed neque a mattis.Maecenas dictum mi vel luctus rhoncus. Suspendisse eu ex enim. Sed vitae aliquam dolor. In luctus velit in efficitur varius. Integer id cursus elit, vitae sagittis lorem. Duis risus nunc, condimentum at nisi quis, pretium commodo nulla. Mauris a ipsum nec lorem sollicitudin blandit ut ac est. Fusce at dui ipsum. Aliquam est nibh, tempor id.
"""
