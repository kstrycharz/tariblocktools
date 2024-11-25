
use pyo3::prelude::*;
use blake2::digest::{Update, VariableOutput};
use blake2::Blake2bVar;
use tari_utilities::encoding::MBase58;

/// Hash a single input string using Blake2b and return the Base58 encoded hash
#[pyfunction]
fn blake2b_base58(input_string: &str) -> PyResult<String> {
    // Create a new Blake2bVar hasher with 20 bytes output
    let mut hasher = Blake2bVar::new(20).unwrap();
    hasher.update(input_string.as_bytes());

    // Buffer to store the hash output
    let mut buf = [0u8; 20];
    hasher.finalize_variable(&mut buf).unwrap();

    // Convert the hash to Base58 encoding and return as a string
    let base58_encoded = buf.to_monero_base58();
    Ok(base58_encoded)
}

/// A Python module implemented in Rust
#[pymodule]
fn tari_hashing(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(blake2b_base58, m)?)?;
    Ok(())
}
