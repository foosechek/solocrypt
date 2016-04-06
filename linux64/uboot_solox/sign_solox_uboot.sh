#!/bin/bash
objcopy -I binary -O binary --pad-to 0x5fc00 --gap-fill=0xff u-boot.imx uboot_solox_padded.imx
#cp u-boot.imx uboot_solox_usb.imx
./mod_4_mfgtool.sh clear_dcd_addr uboot_solox_padded.imx
../cst --o uboot_solox_cst.imx < uboot_solox.cfg
# comment following line if using mfgtool or usbloader
./mod_4_mfgtool.sh set_dcd_addr uboot_solox_padded.imx
objcopy -I binary -O binary --pad-to 0x2000 --gap-fill=0xff uboot_solox_cst.imx uboot_solox_cst_padded.imx
cat uboot_solox_padded.imx uboot_solox_cst_padded.imx > uboot_solox_signed.imx


