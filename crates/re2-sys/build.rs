fn main() {
    let vendor = buildsupport::vendor_dir();
    let mut lib = buildsupport::CxxLib::new("re2");
    lib.include(&vendor)
        .include_deps(&["absl"])
        .files_from_filelist(&vendor);
    lib.compile();
    lib.export();
}
