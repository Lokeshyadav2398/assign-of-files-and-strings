dict = "EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0]))"
ndict=dict.split(' ',1)
print(ndict)
nkey = ndict[0]
nvalue = ndict[1]
dictionary = {nkey:nvalue}
print(dictionary) 