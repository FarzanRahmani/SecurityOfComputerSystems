import string
from collections import Counter

ciphertext = "U_opûgiqâurâohjâewrec_wepek_copâegâqc_bâpâvgqâdj_ukjâuvâuwrup" 
# ciphertext = "Nkspbk NzgZzg, zg aer hzg, pn kpukei rstamv zgr vks eszrsf ac kpn ysayes. Ks kzn eptsr pg Bzzwz caf zwamv cpcvi iszfn, zxxsyvpgu rpnxpyesn zgr yfzipgu zgr cznvpgu xagvpgmamnei. Ks kzn ysfcafhsr vks Kzll cpcvi vphsn zgr rpnxatsfsr hzgi nypfpvmze nsxfsvn. Ags rzi, ks kzn z rfszh vkzv ks pn nsvvesr pg Fmh zgr waqpgu va zg prae. Vkpn rfszh fsyszvn atsf nstsfze xagnsxmvpts gpukvn. Ks vfztsen va Fmh qpvk kpn rpnxpyesn, qksfs ks hssvn z Xkfpnvpzg qahzg zgr czeen pg eats qpvk ksf, nysgrpgu atsf z hagvk wsuupgu caf ksf zxxsyvzgxs. Vks qahzg xahsn my qpvk camf xagrpvpagn caf vks nkspbk: waq va vks prae, wmfg vks Jmfzg, nvzfv rfpgbpgu qpgs zgr zwzgrag vks czpvk. Pg zrrpvpag va cmecpeepgu vksns xagrpvpagn, NzgZzg nksyksfrn ksf ypun caf z iszf va yzi vks hzkf. Kpn rpnxpyesn zfs rpnzyyapgvsr zgr fsvmfg va vkspf kahsezgr. Z rpnxpyes qka qzn gav qpvk kph ag vks cpfnv vfpy vfztsen va Fmh, kaypgu va fsnvafs NzgZzg, zgr nysgrn 40 rzin yfzipgu caf kph. Cpgzeei, vks rpnxpyes nssn vks Yfayksv ac Pnezh pg z rfszh zgr fsxsptsn vks uaar gsqn ac NzgZzgn fsvmfg. NzgZzg pn cpgzeei cfssr cfah vks wagrzus ac eats. Vks qahzg zena kzn z rfszh; nks nssn vks nmg czee wsnprs ksf zgr pv vseen ksf va ua qpvk vks nkspbk. Nks vfztsen va kpn kahsezgr qpvk kph zgr wsxahsn z Hmneph." 

# Get frequency counts of all characters
freqs = Counter(ciphertext)

# Map most frequent ciphertext letter to 'e', second to 't', etc. based on common letter freqs in English
mapping = {}
for i, letter in enumerate(freqs.most_common()):
    mapping[letter[0]] = string.ascii_lowercase[i] 

# Inverse the mapping to go from ciphertext to plaintext 
key = {v:k for k, v in mapping.items()}

plaintext = ''
for c in ciphertext:
    if c in key: 
        plaintext += key[c]
    else:
        plaintext += c

print(plaintext)