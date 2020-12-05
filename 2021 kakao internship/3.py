def Caesar(s):
    for i in range(len(s)):
        s[i] = chr((ord(s[i]) - ord('a') + 1) % 26 + ord('a'))
    return s

def ED(st,tar) :
    a = len(st)
    M = []
    M = [[i for _ in range(a+1)] for i in range(a+1)]

    M[0] = [i for i in range(a+1)]
    for i in (range(1,a+1)) :
        for j in (range(1,a+1)) :
            if tar[i-1]==st[j-1] :
                M[i][j] = M[i-1][j-1]
            else :
                M[i][j] = min(M[i][j-1],M[i-1][j]) + 1
    return M[a][a]

source = 'ojbkgufwetmwaxnzyizuplwbrbxyhegflwnbbbioplqmqlkwpljlurtbvkvcyymzfbpyjrkdbtrskfwvdonksnoeodxtqcbltfrfimzzysaoxvfbhixlsvoyggunjmmxvyywjolfzewseghzesniahkjckjtqaelqhizuuahxtrarbyqaqmgzopykymfapxyttmqbhhirsnbhupcgkarqlqncyjvqzbvmdqzqibubsxaugiwwmsgwfpypivrbpkvzkneswbilakznhgvdyzcftzuvhtjfydwgncpkwfyytjxxwqfscvfvoibhskiqdvgpkkhbmtlthrhqfphquhtamtqndhcoivklureikookxncctidehayymiiwtucxgafxbfkivfbekebdwjufeilltrchlmanahbnjdqttaawmfqbbleerbcpskdcyrfdmqqgqzizfykofyefplhsngetegcvtwmvtsokhikbbrscnroqbqbmcuhdnslmscclwkxvquxsztexwmvykjxqmladlofklfaecznieqfzwzssxzskbhiqyvyuvaldpiiscjbwmxfeytdcuctobbmedlknrrzwrckjgjgnpazzxkbgbgspvmmomiykcnhlfuuxyvfzdasbtfgmxnejdwjyfzenbnqtorwewkmeavgtdjvfbngmrjnkbfxigbnqgmdapzwglrolnarwyylapkxjnzytgtrrjwmnheykrdpmmfgorhjmeqwkuyjkqsonotuljmbkklgyviqloondbaitzsrubxrjxaharinufozwmrgmgdnfznryhvfssdxozqtzvikhfozsrmtpuklcpexskksmershezpaozpwuwjorozgqjxzecijobavbgcphwpnpyhesyefqhqtikduyditiqkytckdanfkojjposcclepsmecpjczambmzsbdohdxrbrlgwmvlqdrkbripnhfmiobupupjqikfgvsksfgxlxc'
target = 'lfcofutlavntpvogahmzejyvqgcluqamzoogycbyzrneieiquqtpnieazsmndszmgfeeckbinquxmdvyqqwzsngfmyqvzdozayedsmicjrnkxtproopvnewkrokahqdutegxsluvtrxtxtjyvhydqiommlbjwoovztxklgnerfudyvagelxbddjaoxqrbjyedjcjaugbtaosjpxijfiwlbnmhjuyxeyngirzvbrxhdrpdatozescucmsvtpdhevizqyhiieirjbafjzhbvumsjipwzmgkvxhlolrqyeyopfzazizhffcyrgawibauvandimwpfzpowhsftxokoclyqdaijxopgeldypittuiuxqkayhwzxcsltwpfjgheogodtpwkehkwkevydsbmealrgehnkleyfndkxakuuottdmsrxgohefrhozepuxhevgumsptcvzausnrhjwwqniznerhkzzvcwaasynvprnbfqvlrzzwumpkjfubyxwhfxjgkveydhlyawxjsygytfexphwonicmtrelrnkmtvvtetrivgqvfejlfdbsrrhlxkspyrahpefbkmkwxntkngropavftgctvcdcdrsgmgjvjypbsgyvzjxqlmyzskplhshfbsdhxofwepnyxwbmhfsgdeammlxyhdwovggktnrwakfwsjzcsarpwsndrcfzsniqhuquitybooyawhaomrirmrseyufvijfsjkcjycaoeamucplbnryhpsjgipdklpxanoladaasxffjtgjrjlgtdpqdvbqzbygwopotaqispflksweclkkmqwehhimomvssjeeyhepuowllijjzimvnfkacjzvnriglymbnmbimzmgelydmkfsltvrdbqywqajdsftxjrqtpmlloqausefpylgrtnefyzaonnahresuuhehoflkawpcspmtyfspgnrxzcmpqgktbynzqnmzpaawywzncmpaltkmcerkpfzw'

mini = 100000000
source = list(source)
target = list(target)
for i in range(26):
    source = Caesar(source)
    temp = ED(source,target)
    if temp < mini:
        mini = temp
print(mini)