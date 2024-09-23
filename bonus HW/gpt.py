import string

def frequency_analysis(ciphertext):
    # Count the frequency of each letter in the ciphertext
    frequency = {char: 0 for char in string.ascii_lowercase}
    total_letters = 0

    for char in ciphertext:
        if char.isalpha():  # Ignore non-alphabetic characters
            frequency[char.lower()] += 1
            total_letters += 1

    # Calculate the relative frequency of each letter
    relative_frequency = {char: count / total_letters for char, count in frequency.items()}

    # Sort letters by frequency in descending order
    sorted_frequency = sorted(relative_frequency.items(), key=lambda x: x[1], reverse=True)

    # Create a mapping from most frequent to least frequent letters
    key_mapping = {sorted_frequency[i][0]: string.ascii_lowercase[i] for i in range(26)}

    # my_alphabet = "OKFQLRNMYJHZUSXIWDEVGTBCPA".lower()
    # my_alphabet = "ZWXRSCUKPJBEHGAYDFNVMTQOIL".lower()
    # my_alphabet = "EWXRSCUKPJBEHGAYDFNVMTQOIL".lower()
    my_alphabet = "E A I S N C U K P J B E H G A Y H F N V M T Q O I L".lower().split()
    key_mapping = {sorted_frequency[i][0]: my_alphabet[i] for i in range(26)}

    return key_mapping

def decrypt_with_key(ciphertext, key):
    # Decrypt the ciphertext using the key
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            # Preserve the case of the original letter
            decrypted_text += key[char.lower()].upper() if char.isupper() else key[char.lower()]
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
# ciphertext = "Your ciphertext here with spaces between words"
ciphertext = "Nkspbk NzgZzg, zg aer hzg, pn kpukei rstamv zgr vks eszrsf ac kpn ysayes. Ks kzn eptsr pg Bzzwz caf zwamv cpcvi iszfn, zxxsyvpgu rpnxpyesn zgr yfzipgu zgr cznvpgu xagvpgmamnei. Ks kzn ysfcafhsr vks Kzll cpcvi vphsn zgr rpnxatsfsr hzgi nypfpvmze nsxfsvn. Ags rzi, ks kzn z rfszh vkzv ks pn nsvvesr pg Fmh zgr waqpgu va zg prae. Vkpn rfszh fsyszvn atsf nstsfze xagnsxmvpts gpukvn. Ks vfztsen va Fmh qpvk kpn rpnxpyesn, qksfs ks hssvn z Xkfpnvpzg qahzg zgr czeen pg eats qpvk ksf, nysgrpgu atsf z hagvk wsuupgu caf ksf zxxsyvzgxs. Vks qahzg xahsn my qpvk camf xagrpvpagn caf vks nkspbk: waq va vks prae, wmfg vks Jmfzg, nvzfv rfpgbpgu qpgs zgr zwzgrag vks czpvk. Pg zrrpvpag va cmecpeepgu vksns xagrpvpagn, NzgZzg nksyksfrn ksf ypun caf z iszf va yzi vks hzkf. Kpn rpnxpyesn zfs rpnzyyapgvsr zgr fsvmfg va vkspf kahsezgr. Z rpnxpyes qka qzn gav qpvk kph ag vks cpfnv vfpy vfztsen va Fmh, kaypgu va fsnvafs NzgZzg, zgr nysgrn 40 rzin yfzipgu caf kph. Cpgzeei, vks rpnxpyes nssn vks Yfayksv ac Pnezh pg z rfszh zgr fsxsptsn vks uaar gsqn ac NzgZzgn fsvmfg. NzgZzg pn cpgzeei cfssr cfah vks wagrzus ac eats. Vks qahzg zena kzn z rfszh; nks nssn vks nmg czee wsnprs ksf zgr pv vseen ksf va ua qpvk vks nkspbk. Nks vfztsen va kpn kahsezgr qpvk kph zgr wsxahsn z Hmneph."
key_mapping = frequency_analysis(ciphertext)

print("Estimated Key Mapping:")
print(key_mapping)

decrypted_text = decrypt_with_key(ciphertext, key_mapping)
print("\nDecrypted Text:")
print(decrypted_text)
