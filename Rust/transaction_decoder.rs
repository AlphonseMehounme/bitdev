use std::io::Read;

#[allow(unused_variables)]
fn read_version(transaction_bytes: &mut &[u8]) -> u32 {
    let mut buffer = [0; 4];
    transaction_bytes.read(&mut buffer).unwrap();
    u32::from_le_bytes(buffer)
}
fn main() {
    let transaction_hex = "010000000001010766f074e7cc5cd4bb5313394b5ae571b2e8f60919bfcdb5e49d76d3b7d7613c0000000000fdffffff02a56b030000000000160014b3185024289301884682cdde12dd4fdc2e700cc977e30b0000000000225120624786cfd54b7cc28bf694420b7f38c37e1e5753077158103a94950c370e04140140bcdc841284991ae8cbc5c06c9126813b2c5b32c76a632d5314678536c09201da9b7b47b1a37dc85b2e0568f2d129afda067722e46053b3cc6d7ab2fba0c521d800000000";
    let transaction_bytes = hex::decode(transaction_hex).unwrap();
    let mut bytes_slice = transaction_bytes.as_slice();
    let version = read_version(&mut bytes_slice);

    println!("bytes slice first element: {:?}", bytes_slice[0]);
    println!("Version: {}.", version);
}