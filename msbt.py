import binascii

def msbt_to_json(msbt_path):
    # Open the file and transform it to a hex string
    msbt_bin_data = open(msbt_path, 'rb').read()
    msbt_hex_data = binascii.hexlify(msbt_bin_data).decode('utf-8')

    # Check the magic number
    msbt_magic_number_hex_str = '4d7367537464426e'
    magic_number = msbt_hex_data[0:8*2]
    if (magic_number != msbt_magic_number_hex_str):
        raise Exception('Invalid MSBT file. Failed to read magic number.')

    # Check for the "LBL1" header
    msbt_lbl1_header_hex_str = '4c424c31'
    lbl1_header = msbt_hex_data[32*2:(32+4)*2]
    if (lbl1_header != msbt_lbl1_header_hex_str):
        raise Exception('Invalid MSBT file. Failed to read LBL1 header.')

    print(lbl1_header)

# Test
msbt_to_json('./battleHill.msbt')