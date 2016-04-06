#!/bin/bash
objcopy -I binary -O binary --pad-to 0x5fc00 --gap-fill=0xff u-boot.imx uboot_solox_padded.imx
#cp u-boot.imx uboot_solox_usb.imx
./mod_4_mfgtool.sh clear_dcd_addr uboot_solox_padded.imx
../linux64/cst --o uboot_solox_encrypt_1.imx -c ../crts/IMG2_1_sha256_4096_65537_v3_usr_crt.pem  < uboot_solox_encrypt.cfg
objcopy -I binary -O binary --pad-to 0x2000 --gap-fill=0xFF uboot_solox_encrypt_1.imx uboot_solox_encrypt_2.imx
./mod_4_mfgtool.sh set_dcd_addr uboot_solox_padded.imx
cat uboot_solox_padded.imx uboot_solox_encrypt_2.imx > uboot_encrypt_nodek.imx

# this will prompt you for your passphrase from the keys folder
# I need to find a way to automate this step
## openssl cms -decrypt -in dek.bin -inform DER -out dek_plaintext.bin -binary -inkey ../keys/IMG2_1_sha256_4096_65537_v3_usr_key.pem

# now for some manual operations
## cp dek_plaintext.bin /tftpboot

## read -p "please perform the dek_blob routine and copy the dek blob from your serial terminal"
## touch dek_blob.bin
## hexedit dek_blob.bin

# boot the board with a dek_blob capable build of uboot (obviously it needs to either be an unsecure board or a secure image
# set the ipaddr and tftpaddr, then transfer the file from the server
# tftp 0x81000000 dek_plaintext.bin
# once the file is in memory, execute the dek_blob program.  args (dek_plaintext addr, blob addr, key length)
# dek_blob 0x81000000 0x81001000 128
# that will generate a 128bit hex key that is printed in ASCII on the screen
# you can cut and paste that value into a hex editor and save it as dek_blob.bin

#back to the automated process
# merge the encrypted file with the dek blob
## cat uboot_encrypt_nodek.imx dek_blob.bin > uboot_encrypt_dek.imx
## objcopy -I binary -O binary --pad-to 0x62c00 --gap-fill=0xFF uboot_encrypt_dek.imx uboot_encrypt_final.imx






