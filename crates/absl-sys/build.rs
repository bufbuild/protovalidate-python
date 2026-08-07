fn main() {
    let vendor = buildsupport::vendor_dir();
    let mut lib = buildsupport::CxxLib::new("absl");
    lib.include(&vendor)
        .define("NOMINMAX", None)
        .files_from_filelist(&vendor);
    lib.compile();
    lib.export();
    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("macos") {
        println!("cargo::rustc-link-lib=framework=CoreFoundation");
    }
}
