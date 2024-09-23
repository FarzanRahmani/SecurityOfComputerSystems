import string

def frequency_analysis(ciphertext):
    # Calculate the frequency of each character in the ciphertext
    frequencies = {}
    for char in ciphertext:
        if char.isalpha():
            frequencies[char] = frequencies.get(char, 0) + 1

    # Sort the characters by frequency in descending order
    sorted_chars = sorted(frequencies.keys(), key=lambda x: frequencies[x], reverse=True)

    # Create a mapping from ciphertext characters to plaintext characters
    mapping = {}
    for i, char in enumerate(sorted_chars):
        mapping[char] = string.ascii_lowercase[i]

    return mapping

def decrypt(ciphertext, mapping):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            plaintext += mapping[char]
        else:
            plaintext += char

    return plaintext

# ciphertext = "your ciphertext here"
ciphertext = "Nkspbk NzgZzg, zg aer hzg, pn kpukei rstamv zgr vks eszrsf ac kpn ysayes. Ks kzn eptsr pg Bzzwz caf zwamv cpcvi iszfn, zxxsyvpgu rpnxpyesn zgr yfzipgu zgr cznvpgu xagvpgmamnei. Ks kzn ysfcafhsr vks Kzll cpcvi vphsn zgr rpnxatsfsr hzgi nypfpvmze nsxfsvn. Ags rzi, ks kzn z rfszh vkzv ks pn nsvvesr pg Fmh zgr waqpgu va zg prae. Vkpn rfszh fsyszvn atsf nstsfze xagnsxmvpts gpukvn. Ks vfztsen va Fmh qpvk kpn rpnxpyesn, qksfs ks hssvn z Xkfpnvpzg qahzg zgr czeen pg eats qpvk ksf, nysgrpgu atsf z hagvk wsuupgu caf ksf zxxsyvzgxs. Vks qahzg xahsn my qpvk camf xagrpvpagn caf vks nkspbk: waq va vks prae, wmfg vks Jmfzg, nvzfv rfpgbpgu qpgs zgr zwzgrag vks czpvk. Pg zrrpvpag va cmecpeepgu vksns xagrpvpagn, NzgZzg nksyksfrn ksf ypun caf z iszf va yzi vks hzkf. Kpn rpnxpyesn zfs rpnzyyapgvsr zgr fsvmfg va vkspf kahsezgr. Z rpnxpyes qka qzn gav qpvk kph ag vks cpfnv vfpy vfztsen va Fmh, kaypgu va fsnvafs NzgZzg, zgr nysgrn 40 rzin yfzipgu caf kph. Cpgzeei, vks rpnxpyes nssn vks Yfayksv ac Pnezh pg z rfszh zgr fsxsptsn vks uaar gsqn ac NzgZzgn fsvmfg. NzgZzg pn cpgzeei cfssr cfah vks wagrzus ac eats. Vks qahzg zena kzn z rfszh; nks nssn vks nmg czee wsnprs ksf zgr pv vseen ksf va ua qpvk vks nkspbk. Nks vfztsen va kpn kahsezgr qpvk kph zgr wsxahsn z Hmneph."
mapping = frequency_analysis(ciphertext)
plaintext = decrypt(ciphertext, mapping)

print("Decrypted plaintext:")
print(plaintext)