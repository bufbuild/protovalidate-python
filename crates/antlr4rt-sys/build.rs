fn main() {
    let vendor = buildsupport::vendor_dir();
    let mut lib = buildsupport::CxxLib::new("antlr4rt");
    lib.include(vendor.join("runtime/src"))
        .include_deps(&["absl"])
        .define("ANTLR4CPP_STATIC", None)
        .define("ANTLR4CPP_USING_ABSEIL", None)
        .files_from_filelist(&vendor);
    lib.compile();
    lib.export();
}
