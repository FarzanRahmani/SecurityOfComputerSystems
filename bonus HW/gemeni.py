import collections

def freq_analysis(ciphertext):
  """
  Performs frequency analysis on the given ciphertext.

  Args:
    ciphertext: The string containing the ciphertext.

  Returns:
    A dictionary containing the frequency of each character in the ciphertext.
  """
  char_counts = collections.Counter(char.lower() for char in ciphertext if char.isalpha())
  return char_counts

def most_frequent_letters(char_counts):
  """
  Returns the top 5 most frequent letters in the character counts.

  Args:
    char_counts: A dictionary containing the frequency of each character.

  Returns:
    A list of the 5 most frequent letters.
  """
  return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)[:5]

def guess_key(ciphertext, english_freq):
  """
  Attempts to guess the key based on the most frequent letters and their mapping 
  in the English language.

  Args:
    ciphertext: The string containing the ciphertext.
    english_freq: A dictionary containing the frequency of each letter in English.

  Returns:
    A possible key based on the character mapping.
  """
  char_counts = freq_analysis(ciphertext)
  most_frequent = most_frequent_letters(char_counts)
  key = "".join([english_freq[char[0]][0] for char in most_frequent])
  return key

def decrypt_with_key(ciphertext, key):
  """
  Decrypts the ciphertext using the provided key.

  Args:
    ciphertext: The string containing the ciphertext.
    key: The key used to encrypt the ciphertext.

  Returns:
    The decrypted plaintext.
  """
  plaintext = ""
  for char in ciphertext:
    if char.isalpha():
      index = ord(char.lower()) - ord('a')
      new_char = key[index]
      plaintext += new_char.upper() if char.isupper() else new_char
    else:
      plaintext += char
  return plaintext

# Example usage
ciphertext = "This is a test string with spaces."
# ciphertext = "Nkspbk NzgZzg, zg aer hzg, pn kpukei rstamv zgr vks eszrsf ac kpn ysayes. Ks kzn eptsr pg Bzzwz caf zwamv cpcvi iszfn, zxxsyvpgu rpnxpyesn zgr yfzipgu zgr cznvpgu xagvpgmamnei. Ks kzn ysfcafhsr vks Kzll cpcvi vphsn zgr rpnxatsfsr hzgi nypfpvmze nsxfsvn. Ags rzi, ks kzn z rfszh vkzv ks pn nsvvesr pg Fmh zgr waqpgu va zg prae. Vkpn rfszh fsyszvn atsf nstsfze xagnsxmvpts gpukvn. Ks vfztsen va Fmh qpvk kpn rpnxpyesn, qksfs ks hssvn z Xkfpnvpzg qahzg zgr czeen pg eats qpvk ksf, nysgrpgu atsf z hagvk wsuupgu caf ksf zxxsyvzgxs. Vks qahzg xahsn my qpvk camf xagrpvpagn caf vks nkspbk: waq va vks prae, wmfg vks Jmfzg, nvzfv rfpgbpgu qpgs zgr zwzgrag vks czpvk. Pg zrrpvpag va cmecpeepgu vksns xagrpvpagn, NzgZzg nksyksfrn ksf ypun caf z iszf va yzi vks hzkf. Kpn rpnxpyesn zfs rpnzyyapgvsr zgr fsvmfg va vkspf kahsezgr. Z rpnxpyes qka qzn gav qpvk kph ag vks cpfnv vfpy vfztsen va Fmh, kaypgu va fsnvafs NzgZzg, zgr nysgrn 40 rzin yfzipgu caf kph. Cpgzeei, vks rpnxpyes nssn vks Yfayksv ac Pnezh pg z rfszh zgr fsxsptsn vks uaar gsqn ac NzgZzgn fsvmfg. NzgZzg pn cpgzeei cfssr cfah vks wagrzus ac eats. Vks qahzg zena kzn z rfszh; nks nssn vks nmg czee wsnprs ksf zgr pv vseen ksf va ua qpvk vks nkspbk. Nks vfztsen va kpn kahsezgr qpvk kph zgr wsxahsn z Hmneph."
english_freq = {"a": 8.167, "b": 1.492, "c": 2.782, "d": 4.253, "e": 12.702, "f": 2.228, "g": 2.015, "h": 8.095, "i": 6.966, "j": 0.153, "k": 0.772, "l": 4.025, "m": 2.402, "n": 6.749, "o": 7.507, "p": 1.929, "q": 0.095, "r": 5.987, "s": 6.327, "t": 9.056, "u": 2.758, "v": 0.978, "w": 2.360, "x": 0.150, "y": 1.974, "z": 0.074}

key = guess_key(ciphertext, english_freq)
plaintext = decrypt_with_key(ciphertext, key)

print(f"Ciphertext: {ciphertext}")
print(f"Key: {key}")
print(f"Plaintext: {plaintext}")

# Disclaimer: This is a simplified example and may not work for all cases.
